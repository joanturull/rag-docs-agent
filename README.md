# rag-docs-agent

Ask questions about your own documents and get answers with source citations. FastAPI + Claude API, containerised and deployed on Cloud Run.

## Status

Work in progress. Phase 0 (scaffolding) is complete — see the roadmap below for what lands next.

## What it does

- Ingests PDF and Markdown files and indexes them for semantic search
- Answers natural-language questions over that corpus, citing the source file and page
- Says "I don't know" when the answer is not in the indexed documents, instead of guessing
- Exposes everything over an HTTP API, so it can be driven from a script, a UI or another service
- Reports token usage and estimated cost for every request

## Stack

| Layer | Choice |
| --- | --- |
| Language | Python 3.12 |
| Packaging | uv, with a committed lockfile |
| Model | Claude API (Anthropic) |
| API | FastAPI |
| Tests | pytest |
| Container | Docker |
| CI/CD | GitHub Actions |
| Hosting | Google Cloud Run |

## Getting started

Requires [uv](https://docs.astral.sh/uv/).

```bash
git clone git@github.com:joanturull/rag-docs-agent.git
cd rag-docs-agent
uv sync
```

`uv sync` reads `uv.lock` and reproduces the exact dependency tree this project was built and tested against, on the Python version pinned in `.python-version`. No manual virtualenv step is needed.

Run the test suite:

```bash
uv run pytest
```

## Roadmap

- [x] **Phase 0** — Project scaffolding, packaging and installable layout
- [ ] **Phase 1** — CLI backed by the Claude API, with token and cost reporting
- [ ] **Phase 2** — Document ingestion, embeddings and retrieval with citations
- [ ] **Phase 3** — FastAPI service and test suite
- [ ] **Phase 4** — Containerisation
- [ ] **Phase 5** — Continuous integration
- [ ] **Phase 6** — Deployment to Cloud Run with continuous delivery
- [ ] **Phase 7** — Structured logging, latency and cost metrics, retrieval evaluation
- [ ] **Phase 8** — Architecture notes and demo

## License

MIT — see [LICENSE](LICENSE).
