# Architecture Diagrams

## 1. System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                          USER BROWSER                               │
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │              React + Vite  (Vercel)                         │  │
│   │                                                             │  │
│   │   [ Paste GitHub URL ]  ──────────►  [ Ask a question ]    │  │
│   │         Step 01                           Step 02          │  │
│   └────────────────────┬────────────────────────┬──────────────┘  │
└────────────────────────┼────────────────────────┼─────────────────┘
                         │  POST /ingest           │  POST /query
                         │  { repo_url }           │  { repo_url, question }
                         ▼                         ▼
┌─────────────────────────────────────────────────────────────────────┐
│                  FastAPI Backend  (HuggingFace Spaces / Docker)      │
│                                                                     │
│   ┌──────────────┐              ┌──────────────────────────────┐   │
│   │  /ingest     │              │  /query                      │   │
│   │              │              │                              │   │
│   │  GitHub API  │              │  Embed query                 │   │
│   │  ↓           │              │  ↓                          │   │
│   │  AST Chunker │              │  Hybrid Search (BM25+vec)   │   │
│   │  ↓           │              │  ↓                          │   │
│   │  Embedder    │              │  Cohere Reranker            │   │
│   │  ↓           │              │  ↓                          │   │
│   │  ChromaDB ◄──┘              │  Groq LLM                   │   │
│   └──────────────┘              └──────────────────────────────┘   │
│                                                                     │
│   structlog ─── every request: latency_ms, tokens, status          │
└─────────────────────────────────────────────────────────────────────┘
                    │                          │
                    ▼                          ▼
         ┌──────────────────┐      ┌───────────────────┐
         │   ChromaDB       │      │  External APIs    │
         │  (persistent     │      │                   │
         │   vector store)  │      │  • OpenAI embeds  │
         └──────────────────┘      │  • Cohere rerank  │
                                   │  • Groq LLM       │
                                   │  • GitHub API     │
                                   └───────────────────┘
```

---

## 2. RAG Pipeline (detailed)

```
  USER QUESTION
  "How does routing work?"
        │
        ▼
┌───────────────────┐
│   Embed Query     │  text-embedding-3-small  →  vector [1536 dims]
└────────┬──────────┘
         │
         ├─────────────────────────────────────┐
         │                                     │
         ▼                                     ▼
┌─────────────────────┐             ┌─────────────────────┐
│   Semantic Search   │             │    BM25 Search      │
│                     │             │                     │
│  ChromaDB cosine    │             │  rank-bm25 index    │
│  similarity         │             │  keyword matching   │
│                     │             │                     │
│  Top 20 chunks      │             │  Top 20 chunks      │
└─────────┬───────────┘             └──────────┬──────────┘
          │                                    │
          └──────────────┬─────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  Reciprocal Rank    │
              │  Fusion (RRF)       │
              │                     │
              │  score = Σ 1/(k+r)  │
              │  k=60, r=rank       │
              │                     │
              │  Top 20 fused       │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  Cohere Reranker    │
              │  rerank-v3.5        │
              │                     │
              │  Cross-encoder      │
              │  scores all 20      │
              │  keeps best 5  ◄────┼── cuts noise 4x
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  Context window     │
              │                     │
              │  chunk 1 ──────┐    │
              │  chunk 2 ──┐   │    │
              │  chunk 3 ─┐│   │    │
              │  chunk 4 ┐││   │    │
              │  chunk 5 ││││   │   │
              └──────────┼┼┼┼──┼───┘
                         ▼▼▼▼  ▼
              ┌─────────────────────┐
              │  Groq LLM           │
              │  llama-3.3-70b      │
              │                     │
              │  System prompt:     │
              │  "answer grounded   │
              │   in chunks only"   │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  ANSWER             │
              │                     │
              │  "Routing works     │
              │   via @app.route()  │
              │   in app.py:L45"    │
              │                     │
              │  + sources cited    │
              │  + file paths       │
              │  + line numbers     │
              └─────────────────────┘
```

---

## 3. Ingest Pipeline

```
  POST /ingest  { repo_url: "github.com/owner/repo" }
        │
        ▼
┌───────────────────────────────────────────────────────┐
│  Already indexed?  ──YES──►  return cached response   │
└──────────────┬────────────────────────────────────────┘
               │ NO
               ▼
    GitHub API  list all files
    filter by SUPPORTED_EXTENSIONS (40+ langs)
    skip files > 100 KB
               │
               ▼  (up to 10 concurrent)
    ┌──────────────────────────┐
    │  per file:               │
    │                          │
    │  Python  →  AST chunks   │  functions + classes
    │  Others  →  sliding win  │  512 tok, 64 overlap
    │                          │
    │  skip chunks < 50 chars  │
    │  cap at 50 chunks/file   │
    └──────────┬───────────────┘
               │  all_chunks  (e.g. 8944 for cult-ui)
               ▼
    Embedder  text-embedding-3-small
    batched 100 texts/call
               │  embeddings [N × 1536]
               ▼
    ChromaDB upsert
    batched 5000/call  ← fixes batch size error
               │
               ▼
    { files_indexed: 447, chunks_stored: 8944, duration_ms: 45200 }
```

---

## 4. Observability

```
  Every HTTP request
        │
        ▼
  observability_middleware  (main.py)
  logs: method · path · status_code · latency_ms · client_ip

  Every LLM call (llm.py)
  logs: model · tokens_used · latency_ms · chunks_count

  Every embed batch (embedder.py)
  logs: model · batch_size · latency_ms

  Every rerank (reranker.py)
  logs: model · input_chunks · output_chunks · top_score

  → All as JSON via structlog
  → Visible in HuggingFace Spaces Logs tab
  → Ready for Datadog / Logtail ingestion
```
