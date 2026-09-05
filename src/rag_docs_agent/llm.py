from anthropic import Anthropic

from rag_docs_agent.config import Settings

PRICE_INPUT_PER_MTOK = 2.0
PRICE_OUTPUT_PER_MTOK = 10.0


def estimate_cost_usd(input_tokens: int, output_tokens: int) -> float:
    return (
        input_tokens * PRICE_INPUT_PER_MTOK + output_tokens * PRICE_OUTPUT_PER_MTOK
    ) / 1_000_000


def _extract_text(content) -> str:

    partes = []

    for bloque in content:
        if bloque.type == "text":
            partes.append(bloque.text)

    return "".join(partes)


def ask(question: str, settings: Settings) -> tuple[str, dict]:
    client = Anthropic(api_key=settings.anthropic_api_key)
    message = client.messages.create(
        model=settings.model,
        max_tokens=settings.max_tokens,
        messages=[{"role": "user", "content": question}],
    )

    usage = message.usage

    return _extract_text(message.content), {
        "input_tokens": usage.input_tokens,
        "output_tokens": usage.output_tokens,
        "cost_usd": estimate_cost_usd(usage.input_tokens, usage.output_tokens),
        "stop_reason": message.stop_reason,
    }
