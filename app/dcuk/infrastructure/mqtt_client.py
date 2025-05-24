
from fastapi_mqtt import MQTTConfig, FastMQTT
from app.xdent.core.settings import settings

import ssl

class MqttClient:
    def __init__(self):
        self.ssl_context = ssl.create_default_context()
        self.ssl_context.check_hostname = True
        self.ssl_context.verify_mode = ssl.CERT_REQUIRED

        self._config = MQTTConfig(
            host=settings.mqtt.host,
            port=settings.mqtt.port,
            username=settings.mqtt.username,
            password=settings.mqtt.password,
            ssl=self.ssl_context,  # Set to True if using SSL/TLS
            version=4,  # Use MQTTv311 or MQTTv5 as needed
        )

        self._client = FastMQTT(
            config=self._config,
            client_id="xdent_mqtt_client",
        )   

    @property
    def client(self):
        return self._client

    async def connect(self):
        await self._client.mqtt_startup()

    async def publish(self, topic, payload):
        await self._client.publish(topic, payload)

    async def subscribe(self, topic):
        await self._client.subscribe(topic)

    async def disconnect(self):
        # Disconnect from the MQTT broker
        await self._client.mqtt_shutdown()

mqtt_client = MqttClient()