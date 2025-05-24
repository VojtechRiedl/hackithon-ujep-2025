
from abc import ABC, abstractmethod

from app.xdent.infrastructure.ollama_client import OllamaClient

class IAIRepository(ABC):
    """
    Interface for AI repository.
    """
    def __init__(self, ollama_client: OllamaClient):
        self.ollama_client = ollama_client

    @abstractmethod
    def get_xdent_response(self, input: dict) -> dict | None:
        pass