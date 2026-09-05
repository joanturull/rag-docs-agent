"""Configuración de la aplicación, leída del entorno."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    anthropic_api_key: str
    model: str = "claude-sonnet-5"
    max_tokens: int = 1024


def get_settings() -> Settings:
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise ValueError(
            "Falta la variable de entorno ANTHROPIC_API_KEY. "
            "Añádela en tu shell o archivo .env con un valor válido: "
            "ANTHROPIC_API_KEY=tu_clave_aqui"
        )
    return Settings(anthropic_api_key=key)
