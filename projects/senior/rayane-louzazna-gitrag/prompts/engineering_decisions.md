# Engineering Decisions

## ChromaDB vs Qdrant vs Pinecone

**Chosen: ChromaDB**

| Criterion | ChromaDB | Qdrant | Pinecone |
|---|---|---|---|
| Self-hosted | ✅ | ✅ | ❌ (managed only) |
| Python-native | ✅ | ❌ (REST/gRPC) | ❌ |
| Zero-config local dev | ✅ | ❌ (Docker required) | ❌ |
| Free tier on Render | ✅ (persistent volume) | ❌ | ❌ |
| Production scale | Medium | High | High |

**Why ChromaDB for v1:** Zero external dependencies, pure Python client, persistent storage via a local directory. Ideal for a senior project demo that needs to run on Render free tier without extra services.

**Limitation acknowledged:** ChromaDB is single-process; no horizontal scaling. Qdrant would be the next step for multi-instance deploys.

## Groq vs OpenAI vs Mistral

**Chosen: Groq (llama-3.3-70b-versatile)**

| Criterion | Groq | OpenAI GPT-4o | Mistral |
|---|---|---|---|
| Latency | ~0.5s | ~2-5s | ~1-2s |
| Free tier | ✅ generous | ❌ | ✅ limited |
| Code quality | High | Very high | High |
| Cost | Free/cheap | $$ | $ |

**Why Groq:** Extremely low latency (inference on custom silicon) + generous free tier + llama-3.3-70b is strong on code Q&A. Perfect for a demo with real users.

## AnimusAI vs OpenAI Embeddings

**Chosen: AnimusAI (OpenAI-compatible endpoint)**

Uses `text-embedding-3-small` via an OpenAI-compatible API. This means the same `openai` Python SDK works without changes — just swap `base_url`.

**Why not direct OpenAI:** AnimusAI provides a free tier suitable for indexing multiple repos during development. The OpenAI SDK compatibility means zero migration cost if we switch later.

## FastAPI vs Flask vs Django

**Chosen: FastAPI**

- Automatic OpenAPI docs (Swagger UI at `/docs`) — great for demo
- Native async support — critical for concurrent GitHub API fetches
- Pydantic models for request/response validation — no boilerplate
- Type hints = self-documenting code

## Structured Logging (structlog)

JSON logs from day 1. Each request logs: method, path, status, latency_ms. Each LLM call logs: model, tokens_used, latency_ms. This makes Render's log viewer useful and prepares for future log aggregation (Datadog, Logtail).

## Single-worker Uvicorn

`--workers 1` on Render free tier. ChromaDB's `PersistentClient` is not thread-safe across multiple processes. Multi-worker would require switching to ChromaDB's HTTP server mode — deferred to v2.
