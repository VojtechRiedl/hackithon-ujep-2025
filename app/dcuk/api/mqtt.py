


from app.dcuk.infrastructure.mqtt_client import mqtt_client


@mqtt_client.client.on_connect()
def on_connect(client, flags, rc, properties):
    # Subscribe to a topic after connecting
    client.subscribe("#")


@mqtt_client.client.on_message()
async def on_message(client, topic, payload, qos, properties):
    # Handle incoming messages
    print(f"Received message: {payload.decode()} on topic: {topic}")

    return 0