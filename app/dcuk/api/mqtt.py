

from app.dcuk.infrastructure.mqtt_client import mqtt_client

from app.xdent.infrastructure.database import database
from app.xdent.repositories.ai_repository import AIRepository
from app.xdent.infrastructure.ollama_client import ollama_client

from app.xdent.models.xdent import Data

@mqtt_client.client.on_connect()
def on_connect(client, flags, rc, properties):
    # Subscribe to a topic after connecting
    client.subscribe("#")


repository = AIRepository(ollama_client)


@mqtt_client.client.on_message()
async def on_message(client, topic, payload, qos, properties):
    # Handle incoming messages
    try:

        with database.session as session:
            # Decode the payload
            decoded_payload = payload.decode('utf-8')
            
            if session.query(Data).filter(Data.topic == topic).count() > 0:
                print(f"Data already exists for topic: {topic}")
                return

            response = repository.get_dcuk_response(topic, decoded_payload)
            if response is None:
                print(f"Invalid response for topic: {topic}")
                return
            # Create a new Data instance
            data = Data(topic=topic, payload=decoded_payload, analysis=response)

            # Add the data to the session
            session.add(data)

            # Commit the session to save the data
            session.commit()
            
            print(f"Data saved: {data.topic} - {data.payload}")


    except Exception as e:
        print(f"Error processing message: {e}")
        return

