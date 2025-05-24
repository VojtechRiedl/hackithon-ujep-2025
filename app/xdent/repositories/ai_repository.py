from json import JSONDecodeError

from app.xdent.interfaces.ai_repository import IAIRepository

from app.xdent.infrastructure.ollama_client import OllamaClient
class AIRepository(IAIRepository):
    """
    Implementation of the AI repository.
    """
    def __init__(self, ollama_client: OllamaClient):
        super().__init__(ollama_client)


    def get_xdent_response(self, input: dict) -> dict | None:
        try:
            prompt = f"""Jsi Český AI asistent specializovaný na analýzu stomatologických zdravotních záznamů. 
                Na základě vstupního textu vytvoř strukturovaný JSON výstup podle níže uvedené šablony.
                Rozepiš všechny odborné termíny a zkratky do srozumitelného jazyka, aby byl výstup srozumitelný i laikovi.

                Pravidla:
                - Výstup musí přesně odpovídat dané JSON struktuře (názvy polí, typy, pořadí).
                - Pokud ve vstupním textu některé informace chybí, musí být příslušná pole přítomna a vyplněna výchozími hodnotami:
                - text: ""
                - číslo: 0
                - pole: []
                - boolean: false
                - enum (např. urgency_level): "nízká", "střední", "vysoká"
                - Pole visualization_hint.topic_distribution musí být seznam objektů ve formátu:
                - {{"topic": "název_tématu", "percentage": číslo}} a jejich součet musí být 100.
                - Výstup nesmí obsahovat žádné komentáře ani doplňující vysvětlení - pouze platný JSON objekt.

                Vstupní text:
                {input}

                Požadovaná výstupní struktura:
                {{
                "semantic_analysis": {{
                    "text": "str",
                    "treatment_summary": "str",
                    "diagnosis": [str],
                    "procedures": [str],
                    "medications": [
                    {{
                        "name": "str",
                        "dosage": "str",
                        "frequency": "str",
                        "duration": "str",
                        "purpose": "str",
                        "prescribed": bool
                    }}
                    ],
                    "teeth_status": [
                    {{
                        "tooth": "int",
                        "procedure": "str",
                        "condition": "str"
                    }}
                    ],
                    "suggested_action": "str",
                    "urgency_level": ["nízká","střední","vysoká"]
                }},
                "analysis_explanation": {{
                    "recognized_keywords": [str],
                    "mapping_reasoning": {{
                    "term": "reason"
                    }},
                    "model_confidence": ["nízká","střední","vysoká"],
                }},
                "visualization_hint": {{
                    "topic_distribution": [
                    {{
                        "topic": "str",
                        "percentage": 0
                    }}
                    ],
                    "dominant_topic": "str"
                }}
                }}"""
            
            return self.ollama_client.prompt(prompt)
        except JSONDecodeError:
            return None