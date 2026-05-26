# GitRAG — Senior Project 2: Production LLM/RAG Service

**Track:** Senior — Project 2
**Author:** Rayane Louzazna
**Contact:** [LinkedIn](https://www.linkedin.com/in/rayane-louzazna-b7752b224)

---

## What it does

GitRAG lets you ask natural-language questions about any public GitHub repository and get answers grounded in the actual source code, with exact file paths and line numbers.

**Live demo:** https://gitrag.vercel.app
**API docs:** https://yanou16-gitgub-rag.hf.space/docs
**Source code:** https://github.com/yanou16/Git_RAG

---

## Senior Project 2 checklist

- [x] FastAPI service — `/ingest`, `/query`, `/health`
- [x] Dockerfile + `docker-compose.yml`
- [x] Structured logging — `latency_ms`, `tokens_used`, `status_code` on every request
- [x] Deployed to HuggingFace Spaces (Docker) + Vercel (frontend)
- [x] Rate limit handling, retry logic, graceful reranker fallback
- [x] `prompts/` with narrative, prompt log, and architecture diagrams

---

## Architecture

```
  User (browser)
      │
      │  React + Vite — Vercel
      │
      ├── POST /ingest ──────────────────────────────────────────────┐
      │                                                              │
      │   GitHub API → AST Chunker → Embedder → ChromaDB            │
      │                                                              │
      └── POST /query ──────────────────────────────────────────────┤
                                                                     │
          Embed query → BM25 + Semantic → RRF Fusion                 │
          → Cohere Rerank (20→5) → Groq llama-3.3-70b → Answer      │
                                                                     │
      FastAPI Backend — HuggingFace Spaces (Docker)  ◄──────────────┘
```

Full diagrams (system / RAG pipeline / ingest / observability) in [`prompts/architecture.md`](prompts/architecture.md).

---

## Stack

| Layer | Technology |
|-------|-----------|
| API | FastAPI + Uvicorn |
| Embeddings | OpenAI `text-embedding-3-small` |
| Vector store | ChromaDB (persistent) |
| Keyword search | BM25 (rank-bm25) |
| Fusion | Reciprocal Rank Fusion |
| Reranking | Cohere `rerank-v3.5` |
| LLM | Groq `llama-3.3-70b-versatile` |
| Frontend | React + Vite + Tailwind CSS |
| Hosting | HuggingFace Spaces + Vercel |

**Supported languages:** Python, JS/TS, C#, Java, Go, Rust, C/C++, Swift, Kotlin, Dart, Ruby, PHP, Vue, Svelte, Shell, SQL, HTML, CSS, JSON, YAML, TOML, XML (40+ extensions)

---

## How to run

### Prerequisites

```bash
# API keys needed:
ANIMUSAI_API_KEY=...      # OpenAI-compatible embeddings
ANIMUSAI_BASE_URL=...     # e.g. https://api.openai.com/v1
GROQ_API_KEY=...          # groq.com
COHERE_API_KEY=...        # optional — reranking
GITHUB_TOKEN=...          # optional — raises rate limit 60→5000 req/h
```

### Local (Python)

```bash
git clone https://github.com/yanou16/Git_RAG.git
cd Git_RAG
cp .env.example .env      # fill in your keys
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API available at `http://localhost:8000/docs`

### Docker

```bash
docker compose up --build
```

### Frontend

```bash
cd frontend
npm install
npm run dev               # http://localhost:3000
```

---

## Observability

Every request is logged as structured JSON via `structlog`:

```json
{"method":"POST","path":"/query","status_code":200,"latency_ms":1123,"event":"http_request"}
{"model":"llama-3.3-70b-versatile","tokens_used":1378,"latency_ms":1113,"event":"llm_call"}
{"model":"rerank-v3.5","input_chunks":20,"output_chunks":5,"top_score":0.92,"event":"rerank_done"}
```

Logs are visible in HuggingFace Spaces → Logs tab and are ready for Datadog/Logtail ingestion.

---

## Resilience

| Scenario | Handling |
|----------|----------|
| GitHub rate limit | `GITHUB_TOKEN` support (60→5000 req/h); error surfaced to frontend with setup instructions |
| API timeout / transient failure | `@with_retry(max_retries=3)` with exponential backoff on all external calls |
| ChromaDB batch limit (5461 items) | Paged upsert at 5000/batch — handles repos with 10k+ chunks |
| Large repos | `max_files` cap, 100 KB file size filter, 50 chunk/file cap |
| Reranker unavailable | Pipeline degrades gracefully — returns BM25+semantic results |
| LLM hallucination | System prompt enforces chunk-only answers; strict fallback message |

---

## Tests

```bash
pip install -r requirements-dev.txt
pytest tests/ -v
# 40 tests — ingest, query, chunker, hybrid search, health
```
