
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, Field

class Ollama(BaseModel):
    """
    Ollama model for Xdent.
    """
    url: str = Field(..., description="URL of the Ollama API", alias="url")
    api_key: str = Field(..., description="API key for the Ollama API", alias="api_key")
    model: str = Field(..., description="Model name for the Ollama API", alias="model")


class Database(BaseModel):
    url: str = Field(..., description="URL of the database", alias="url")


class Mqtt(BaseModel):
    host: str = Field(..., description="Host of the MQTT broker", alias="host")
    port: int = Field(..., description="Port of the MQTT broker", alias="port")
    username: str = Field(..., description="Username for the MQTT broker", alias="username")
    password: str = Field(..., description="Password for the MQTT broker", alias="password")
    off: bool = Field(..., description="Disable MQTT", alias="off")


class Settings(BaseSettings):
    ollama: Ollama = Field(
        ...,
        description="Ollama settings",
        example={
            "url": "http://localhost:11434",
            "api_key": "your_api_key",
            "model": "llama2",
        },
    )
    database: Database = Field(
        ...,
        description="Database settings",
        example={
            "url": "sqlite:///./xdent.db",
        },
    )

    mqtt: Mqtt = Field(
        ...,
        description="MQTT settings",
        example={
            "url": "mqtt://localhost",
            "port": 1883,
            "username": "user",
            "password": "password",
        },
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        arbitrary_types_allowed=True,
        env_nested_delimiter="__",
    )


settings = Settings() 
