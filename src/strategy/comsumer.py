import json
from kafka import KafkaConsumer
from kafka.structs import OffsetAndMetadata
from kafka.structs import TopicPartition

def value_deserializer(m):
    try:
        return json.loads(m.decode())
    except Exception:
        return {}

consumer = KafkaConsumer(
    'test',
    group_id='group-a',
    bootstrap_servers=['kafka-1:9092'],
    value_deserializer=value_deserializer,
    enable_auto_commit=False,
)

for message in consumer:
    print(message)
    print('%s:%d:%d: key=%s value=%s' % (
        message.topic,
        message.partition,
        message.offset,
        message.key,
        message.value
    ))