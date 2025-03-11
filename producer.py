import json
from confluent_kafka import Producer

# Kafka configuration
conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(conf)

topic = "test_topic"

# Produce JSON messages
for i in range(20):
    message = {"key": str(i), "value": f"Message {i}"}
    producer.produce(topic, key=str(i), value=json.dumps(message))
    print(f"Produced: {message}")

# Flush to ensure messages are sent
producer.flush()
