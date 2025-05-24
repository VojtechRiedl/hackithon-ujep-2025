

from app.xdent.core.settings import settings
from openai import OpenAI

import json



class OllamaClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.ollama.api_key,
            base_url=settings.ollama.url,
        )

    def prompt(self, prompt: str) -> dict:
        response = self.client.post(
            path="/generate",
            body={
                "model": settings.ollama.model,
                "prompt": prompt,
                "stream": False,
                "temperature": 0.3,
            },
            cast_to=str,
        )

        data: dict = json.loads(response)

        return json.loads(data["response"].split("```json")[1].split("```")[0].strip())


ollama_client = OllamaClient()

#print(ollama_client.prompt("Hello, how are you?"))