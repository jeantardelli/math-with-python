"""
Some data is received in a constant stream from various sources. For example,
we might have a situation where multiple temperature probes are reporting
values at set intervals via a Kafka server. Kafka is a streaming data message
broker that passes messages to different processing agents based on topics.

Processing streaming data is the perfect application for asynchronous Python.
This allows us to process larger quantities of data concurrently, which could
be very important in applications. Of course, we can't directly perform
long-running analysis on this data in an asynchronous context, since this will
interfere with the execution of the event loop. For working with Kafka streams
it is best to use Python's asynchronous programming features, such as the Faust
package. This package allows us to define asynchronous functions that will act
as processing agents or services that can process or otherwise interact with a
stream of data from a Kafka server.

This module illustrates how to use the Faust package to process a stream of
data from a Kafka server.
"""
import faust

from numpy.random import default_rng

rng = default_rng(12345)
app = faust.App("sample", broker="kafka://localhost")

class Record(faust.Record, serializer="json"):
    id_string: str
    value: float

topic = app.topic("sample-topic", value_type=Record)

@app.agent(topic)
async def process_record(records):
    async for record in records:
        print(f"Got {record.id_string}: {record.value}")

@app.timer(interval=1.0)
async def producer1(app):
    await app.send(
            "sample-topic",
            value=Record(id_string="producer 1", value=rng.uniform(0, 2)))

@app.timer(interval=2.0)
async def producer2(app):
    await app.send(
            "sample-topic",
            value=Record(id_string="producer 2", value=rng.uniform(0, 5)))

app.main()
