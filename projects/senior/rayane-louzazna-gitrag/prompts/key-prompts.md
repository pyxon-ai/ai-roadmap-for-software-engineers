# Key Prompts Log

Prompts used with **Claude Code** during development of GitRAG. Redacted of all secrets.

---

| # | Phase | Prompt (summary) | What it produced |
|---|-------|-----------------|-----------------|
| 1 | Architecture | "Design a production RAG pipeline for GitHub repos: chunking strategy, vector store choice, retrieval method, LLM. Justify each choice." | Full architecture plan — AST chunking, ChromaDB, hybrid BM25+semantic+RRF, Cohere reranking, Groq LLM |
| 2 | Chunking | "Implement AST-aware chunking for Python files — extract functions and classes as semantic units. Fallback to sliding window for other languages." | `services/chunker.py` with Python AST parser + sliding window fallback |
| 3 | Retrieval | "Implement hybrid search: BM25 keyword index + ChromaDB semantic search, fused with Reciprocal Rank Fusion. Return top-k with combined scores." | `services/hybrid_search.py` with RRF fusion |
| 4 | API | "Build FastAPI endpoints: POST /ingest (clone, chunk, embed, store), POST /query (hybrid search + rerank + LLM), GET /health. Use Pydantic models, async throughout." | `routes/ingest.py`, `routes/query.py`, `routes/health.py`, `models/schemas.py` |
| 5 | Observability | "Add structured logging to every route and service call. Log: latency_ms per request, tokens_used per LLM call, batch sizes for embeddings." | `structlog` integration in `main.py` middleware + per-service log events |
| 6 | Resilience | "Add an async retry decorator with exponential backoff. Wrap all external API calls (embeddings, Groq, Cohere, GitHub)." | `utils/retry.py` with `@with_retry(max_retries=3)` |
| 7 | Docker | "Write a production Dockerfile: Python 3.13, non-root user, PORT from env var, single-stage, minimal image." | `Dockerfile` compatible with HuggingFace Spaces |
| 8 | Language support | "Extend SUPPORTED_EXTENSIONS to cover C#, Java, C/C++, Go, Rust, Ruby, PHP, Swift, Kotlin, Dart, Vue, Svelte, Shell, SQL, HTML, CSS, JSON, YAML, TOML, XML." | Updated `services/github.py` with 40+ extensions |
| 9 | Bug: ChromaDB | "Fix: ValueError: Batch size of 8944 is greater than max batch size of 5461 when upserting to ChromaDB." | Paged upsert in `services/vector_store.py` (5000 items/batch) |
| 10 | LLM prompt | "Rewrite the system prompt so it adapts format to question type: direct answer for simple questions, structured flow for 'how does X work', targeted lines for debug questions. Always answer in the user's language." | Updated `services/llm.py` SYSTEM_PROMPT with adaptive format rules |
| 11 | Frontend | "Build a React + Vite frontend with Cohere 2026 design system: white canvas, near-black CTAs, deep-green feature band, coral accents, monumental display type, rule-separated layouts. No gradient text, no glassmorphism, no identical card grids." | Full frontend — Navbar, Hero, HowItWorks, Tool, Footer components |
| 12 | Error UX | "Add human-readable error messages for: GitHub rate limit (403), private repo (404), unsupported language, network timeout. Show actionable hints." | `humanise()` function in `Tool.jsx` |
| 13 | Tests | "Write integration tests for: ingest endpoint, query endpoint, chunker, hybrid search, health check. Use pytest + httpx AsyncClient." | 40 tests in `tests/` directory |
