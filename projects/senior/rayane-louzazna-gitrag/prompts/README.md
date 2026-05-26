# Prompts & Process — GitRAG

**Track:** Senior — Project 2: Production LLM/RAG service
**Format used:** B (step-by-step narrative) + C (prompt log)

---

## Project summary

GitRAG is a production RAG API that lets you ask natural-language questions about any public GitHub repository and get answers grounded in actual source code, with exact file paths and line numbers.

**Live demo:** https://gitrag.vercel.app
**API:** https://yanou16-gitgub-rag.hf.space/docs
**Source:** https://github.com/yanou16/Git_RAG

---

## Step-by-step build narrative

### Phase 1 — Architecture design

Started by mapping out the full RAG pipeline before writing any code. Key decisions made upfront:

- **Chunking strategy:** AST-aware for Python (functions/classes as units), sliding window for others. Rationale: semantic chunks improve retrieval precision vs arbitrary character windows.
- **Vector store:** ChromaDB — zero external dependencies, Python-native, persistent local storage. Qdrant would scale better but adds Docker complexity for a solo project.
- **Retrieval:** Hybrid from the start (BM25 + semantic). Pure vector search misses exact identifiers (function names, error codes). RRF fusion combines both signals without tuning per-corpus weights.
- **Reranking:** Cohere cross-encoder as a second stage — rescores top 20 candidates, sends best 5 to the LLM. Cuts hallucination risk significantly.

See [`engineering_decisions.md`](engineering_decisions.md) for the full decision log.

### Phase 2 — Backend (FastAPI)

Built the API layer first, top-down:

1. `POST /ingest` — GitHub file listing → AST chunking → batch embedding → ChromaDB upsert
2. `POST /query` — embed query → hybrid retrieval → Cohere rerank → Groq LLM → structured response
3. `GET /health` — liveness check for HuggingFace Spaces

**Structured logging from day 1** using `structlog`. Every request logs `latency_ms`, every LLM call logs `tokens_used` and `model`. This made debugging production issues (ChromaDB batch size, GitHub rate limits) traceable from HF Spaces logs.

**Retry decorator** (`utils/retry.py`) wraps all external API calls with exponential backoff — covers Groq rate limits and transient embedding API failures.

### Phase 3 — Productionisation

- **Dockerfile** — single-stage Python 3.13, non-root user, `--no-cache-dir` pip install, PORT injected by HuggingFace via env var
- **docker-compose.yml** — local dev with volume mount for ChromaDB persistence
- **Rate limit handling** — GITHUB_TOKEN support raises unauthenticated 60 req/h to 5000 req/h; documented in README
- **ChromaDB batch fix** — discovered max batch size of 5461 items; implemented paged upsert (5000/batch) to support large repos

### Phase 4 — Frontend

Built a React + Vite frontend using the Cohere 2026 design system:
- White canvas, near-black CTAs, deep-green feature bands
- Real-time progress steps during indexing
- Expandable source citations with file path + line number + relevance score
- Error handling with human-readable messages (rate limit, private repo, unsupported language)

Deployed on Vercel with `VITE_API_URL` pointing to the HF Space.

### Phase 5 — Extended language support

Initial version only supported Python and JS/TS. Extended `SUPPORTED_EXTENSIONS` to 40+ entries covering C#, Java, C/C++, Go, Rust, Ruby, PHP, Swift, Kotlin, Dart, Vue, Svelte, Shell, SQL, HTML/CSS, JSON, YAML, TOML, XML.

---

## Key design trade-offs

| Decision | Chosen | Alternative | Why |
|----------|--------|-------------|-----|
| Chunking | AST (Python) + sliding window | tree-sitter universal AST | No native binary deps in Docker |
| Vector DB | ChromaDB | Qdrant | Zero-config for demo; Qdrant for v2 |
| LLM | Groq llama-3.3-70b | OpenAI GPT-4o | 10x lower latency, free tier |
| Retrieval | Hybrid BM25 + semantic + RRF | Pure vector | Catches exact identifiers |
| Reranking | Cohere rerank-v3.5 | None | Cuts noise from 20 → 5 candidates |
| Workers | 1 Uvicorn worker | Multi-worker | ChromaDB PersistentClient not multiprocess-safe |

---

## Resilience considerations

- **GitHub rate limit:** unauthenticated = 60 req/h. Documented GITHUB_TOKEN secret. Error message surfaced to frontend with setup instructions.
- **Embedding API timeout:** `@with_retry(max_retries=3)` with exponential backoff on all external calls.
- **ChromaDB batch limit:** hard cap at 5461 items per upsert. Fixed with paged inserts of 5000.
- **Large repos:** `max_files` cap (configurable via request body), file size filter (> 100 KB skipped), chunk cap per file (50).
- **Reranker unavailable:** pipeline degrades gracefully — returns BM25+semantic results without reranking if Cohere key is missing.
- **LLM hallucination:** system prompt enforces "use ONLY information from provided chunks" with a strict fallback message.

---

## AI tooling used

Built with **Claude Code** (Anthropic) as the primary coding assistant throughout all phases. See [`key-prompts.md`](key-prompts.md) for the most important prompts and what each produced.
