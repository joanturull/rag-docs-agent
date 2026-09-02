def test_package_exposes_main_entrypoint():
    """The console script declared in pyproject.toml needs main() to exist."""
    from rag_docs_agent import main

    assert callable(main)

