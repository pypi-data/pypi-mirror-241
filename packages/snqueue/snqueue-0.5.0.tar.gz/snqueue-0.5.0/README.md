# SnQueue - An SNS/SQS Microservice Mechanism

## Installation

```shell
pip install snqueue
```

## A Dumb Service Example

```py3
import asyncio
import json
import logging
import random
import time

from threading import Thread

from snqueue.service import SnQueueServer, SqsVirtualQueueClient, SnQueueRequest, SnQueueResponse
from snqueue.service.helper import parse_raw_sqs_message, SqsConfig

""" Service setup """
lower_bound_proc_time = 4
upper_bound_proc_time = 10

def proc_time(batch: int) -> int:
  return sum(random.sample(range(lower_bound_proc_time, upper_bound_proc_time), batch))

def bad_request(
    res: SnQueueResponse=None,
    response_topic_arn: str=None,
    message: str=None
) -> None:
  if not res or not response_topic_arn:
    return logging.error(message or "Bad request")
  
  res.status(400).send(response_topic_arn, message)

def service_fn(req: SnQueueRequest, res: SnQueueResponse):  
  request_metadata = req.attributes.get("SnQueueRequestMetadata")
  response_topic_arn = request_metadata.get('ResponseTopicArn')
  batch = req.data.get('batch')
  processing_time = proc_time(batch)
  logging.info(f"Requested batch: {batch}; processing time: {processing_time} seconds.")
  time.sleep(processing_time)
  logging.info(f"Processed batch of {batch} in {processing_time} seconds.")
  res.status(200).send(response_topic_arn, { "ProcessingTime": processing_time })

""" Server side setup """
aws_profile_name = "xxxxxx"
service_topic_arn = "arn:aws:sns:us-east-1:xxxxxx:xxxxxx"
service_sqs_url = "https://sqs.us-east-1.amazonaws.com/xxxxxx/xxxxxx"
response_topic_arn = "arn:aws:sns:us-east-1:xxxxxx:xxxxxx"
response_sqs_url = "https://sqs.us-east-1.amazonaws.com/xxxxxx/xxxxxx"

message_attributes = {
  "SnQueueRequestMetadata": {
    "DataType": "String",
    "StringValue": json.dumps({ "ResponseTopicArn": response_topic_arn })
  }
}

server = SnQueueServer(aws_profile_name, sqs_config=SqsConfig(WaitTimeSeconds=1))
server.use(service_sqs_url, service_fn)

""" Client side setup"""
async def send_request(batch: int, timeout: int):
  try:
    async with SqsVirtualQueueClient(
      response_sqs_url,
      aws_profile_name,
      sqs_config=SqsConfig(MaxNumberOfMessages=10, WaitTimeSeconds=1)
    ) as client:
      logging.info(f"Sending a request with batch {batch}")
      start = time.perf_counter()
      response = await client.request(
        service_topic_arn,
        { "batch": batch },
        timeout=timeout,
        MessageAttributes=message_attributes
      )
      stop = time.perf_counter()
      logging.info(f"Received a response for batch {batch} after {stop - start} seconds.")
      logging.info(parse_raw_sqs_message(response).Body.Message)
  except asyncio.TimeoutError as e:
    logging.error(f"Timeout for task with batch of {batch} after {timeout} seconds.")
  except Exception as e:
    logging.exception(e)

# main thread
if __name__ == '__main__':
  # start server in another thread
  thread = Thread(target=server.start)
  thread.start()

  async def main():
    # send 3 requests
    batches, timeouts = [3, 1, 2], [10, 20, 40]
    tasks = list(map(send_request, batches, timeouts))
    return await asyncio.gather(*tasks)
  
  asyncio.run(main())

  # shut down the service
  server.shutdown()
```

The output would be like:

```console
[2023-11-16 16:04:34,467 - snqueue.service.server - INFO] The server is up and running.
[2023-11-16 16:04:34,472 - root - INFO] Sending a request with batch 3
[2023-11-16 16:04:35,509 - root - INFO] Sending a request with batch 1
[2023-11-16 16:04:35,538 - root - INFO] Requested batch: 3; processing time: 15 seconds.
[2023-11-16 16:04:36,471 - root - INFO] Sending a request with batch 2
[2023-11-16 16:04:36,708 - root - INFO] Requested batch: 1; processing time: 9 seconds.
[2023-11-16 16:04:37,888 - root - INFO] Requested batch: 2; processing time: 11 seconds.
[2023-11-16 16:04:45,708 - root - INFO] Processed batch of 1 in 9 seconds.
[2023-11-16 16:04:48,888 - root - INFO] Processed batch of 2 in 11 seconds.
[2023-11-16 16:04:50,538 - root - INFO] Processed batch of 3 in 15 seconds.
[2023-11-16 16:04:51,627 - root - INFO] Received a response for batch 1 after 16.118201876059175 seconds.
[2023-11-16 16:04:51,628 - root - INFO] {"ProcessingTime": 9}
[2023-11-16 16:04:51,630 - root - INFO] Received a response for batch 2 after 15.159262810833752 seconds.
[2023-11-16 16:04:51,630 - root - INFO] {"ProcessingTime": 11}
[2023-11-16 16:04:51,630 - root - ERROR] Timeout for task with batch of 3 after 10 seconds.
[2023-11-16 16:04:51,634 - snqueue.service.server - INFO] The server is shutting down.
```