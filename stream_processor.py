import faust

# Create Faust app
app = faust.App("message-processor", broker="kafka://localhost:9092")

# Define Message Schema
class MessageSchema(faust.Record, serializer='json'):
    key: str
    value: str

# Define Kafka topics
input_topic = app.topic("test_topic", value_type=MessageSchema)
output_topic = app.topic("processed_topic", value_type=MessageSchema)

@app.agent(input_topic)
async def process(messages):
    async for msg in messages:
        transformed_value = msg.value.upper()
        transformed_message = MessageSchema(key=msg.key, value=transformed_value)

        # Print debug info
        print(f"Processing: {msg.value} ➝ {transformed_value}")

        # Send transformed message to new topic
        await output_topic.send(value=transformed_message)

if __name__ == "__main__":
    app.main()
