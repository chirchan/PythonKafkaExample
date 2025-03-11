from confluent_kafka import Consumer
import json

# Kafka Consumer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'processed_group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(["processed_topic"])  # ✅ Updated to read from `processed_topic`

print("Listening for transformed messages...")

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Error: {msg.error()}")
            continue

        transformed_msg = json.loads(msg.value().decode('utf-8'))
        print(f"Consumed: {transformed_msg}")

except KeyboardInterrupt:
    print("Shutting down...")
finally:
    consumer.close()
