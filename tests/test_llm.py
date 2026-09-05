from types import SimpleNamespace

from rag_docs_agent.llm import _extract_text, estimate_cost_usd


def test_no_tokens_means_no_cost():
    assert estimate_cost_usd(0, 0) == 0


def test_cost_scales_with_token_counts():
    assert estimate_cost_usd(1_000_000, 0) == 2.0
    assert estimate_cost_usd(0, 1_000_000) == 10.0
    assert estimate_cost_usd(1_000_000, 1_000_000) == 12.0


def test_output_tokens_cost_more_than_input():
    assert estimate_cost_usd(0, 1000) > estimate_cost_usd(1000, 0)


def test_extract_text_joins_only_text_blocks_in_order():
    content = [
        SimpleNamespace(type="image", text="ignored"),
        SimpleNamespace(type="text", text="Hola, "),
        SimpleNamespace(type="thinking", text="ignored"),
        SimpleNamespace(type="text", text="mundo!"),
    ]
    assert _extract_text(content) == "Hola, mundo!"


def test_extract_text_handles_empty_content():
    assert _extract_text([]) == ""
