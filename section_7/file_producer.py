import sys
import time

from confluent_kafka import Producer
from settings import settings


def send_message(topic, message, callback):
    try:
        p.produce(topic, message, callback=callback)

    except BufferError:
        sys.stderr.write('%% Local producer queue is full (%d messages awaiting delivery): try again\n' %
                         len(p))

    p.poll(0)

def delivery_callback(err, msg):
    if err:
        sys.stderr.write('%% Message failed delivery: %s\n' % err)
    else:
        sys.stderr.write('%% Message delivered to %s [%d] @ %d\n' %
                         (msg.topic(), msg.partition(), msg.offset()))


if __name__ == '__main__':
    broker = settings.broker_url
    topic = settings.simple_topic
    print(f'Usage: <bootstrap-brokers> : {broker} <topic> {topic}')

    # Producer configuration
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    conf = {'bootstrap.servers': broker}

    # Create Producer instance
    p = Producer(**conf)

    file_path = "./test.txt"
    file = open(file_path, mode="r")
    while True:
        message = file.read()
        if not message:
            print("sleep 1 sec")
            time.sleep(1)
            continue

        send_message(topic, message, delivery_callback)
