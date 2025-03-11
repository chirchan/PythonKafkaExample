# PythonKafkaExample
# Kafka Message Processing Pipeline

## Overview
This project demonstrates a **Kafka-based message processing pipeline** using:
- **Producer** → Sends messages to Kafka.
- **Stream Processor** (Faust) → Transforms the messages.
- **Consumer** → Reads and prints transformed messages.

---

## Project Structure
```
.
│── producer.py        # Produces messages to Kafka
│── stream_processor.py # Processes messages using Faust
│── consumer.py        # Consumes transformed messages
│── requirements.txt   # Python dependencies (if needed)
│── docker-compose.yml # (Optional) Kafka setup via Docker
```

---

## Components
### 1. Producer (`producer.py`)
- Sends **JSON messages** to Kafka topic: `test_topic`.
- Messages are structured as:
  ```json
  {"key": "1", "value": "Message 1"}
  ```
- Uses `confluent-kafka`.

### 2. Stream Processor (`stream_processor.py`)
- Uses **Faust** (Python Stream Processing).
- Listens to `test_topic`, transforms messages, and sends them to `processed_topic`.
- Transforms message values to **uppercase**.

### 3. Consumer (`consumer.py`)
- Reads from `processed_topic` and prints transformed messages.
- Messages are in JSON format.

---

## Setup & Installation
### 1. Install Dependencies
Ensure you have Python 3.9+ installed, then install required packages:
```bash
pip install confluent-kafka faust
```

### 2. Start Kafka (If Not Running)
If you have Kafka installed, start it:
```bash
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties
```
Or use Docker:
```bash
docker-compose up -d
```

### 3. Run the Kafka Pipeline
#### Step 1: Start the Stream Processor
```bash
python stream_processor.py
```
#### Step 2: Run the Producer
```bash
python producer.py
```
#### Step 3: Run the Consumer
```bash
python consumer.py
```

---

## Expected Output
1. **Producer:**
```
Produced: {"key": "1", "value": "Message 1"}
Produced: {"key": "2", "value": "Message 2"}
```

2. **Stream Processor:**
```
Processing: Message 1 ➔ MESSAGE 1
Processing: Message 2 ➔ MESSAGE 2
```

3. **Consumer:**
```
Consumed: {"key": "1", "value": "MESSAGE 1"}
Consumed: {"key": "2", "value": "MESSAGE 2"}
```

---

## Troubleshooting
- **Kafka not running?** Check with:
  ```bash
  kafka-topics.sh --list --bootstrap-server localhost:9092
  ```
- **Faust Import Error?** Ensure you installed Faust using `pip install faust`.
- **Consumer not receiving messages?** Check if `processed_topic` exists:
  ```bash
  kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic processed_topic --from-beginning
  ```

---

## Future Enhancements
- Add **Docker support** to run all services in containers.
- Implement **error handling & logging**.
- Scale Kafka to **multi-node clusters**.

---
