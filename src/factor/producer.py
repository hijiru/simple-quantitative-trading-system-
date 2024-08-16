# -*- coding: utf-8 -*-
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
from time import sleep

def value_serializer(m):
    return json.dumps(m).encode()

producer = KafkaProducer(bootstrap_servers=['kafka-1:9092'],value_serializer=value_serializer,)
while True:
    # asynchronous by default
    future = producer.send('test',{'hello':'world'})
    print(future)

    # block for 'synchronous' sends
    try:
        record_metadata = future.get(timeout=10)
        print(record_metadata)
    except KafkaError:
        # decide what to do if produce request failed...
        pass
    sleep(3)

# successful result returns assigned partition and offset
# print(record_metadata.topic)
# print(record_metadata.partition)
# print(record_metadata.offset)

