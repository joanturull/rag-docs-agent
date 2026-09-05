import argparse

from rag_docs_agent.config import get_settings
from rag_docs_agent.llm import ask


def main() -> None:
    parser = argparse.ArgumentParser(description="Pregunta a Claude desde el terminal.")
    parser.add_argument("question", help="La pregunta que quieres hacer")
    args = parser.parse_args()

    settings = get_settings()
    text, usage = ask(args.question, settings)

    print(text)
    print(usage)
