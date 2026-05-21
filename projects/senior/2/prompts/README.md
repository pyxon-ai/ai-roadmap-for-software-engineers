# AI-assisted development — prompts folder

## Summary

- **Track:** Senior
- **Project option:** Option C — Key prompts (short log)
- **Primary tools:** Antigravity AI, VS Code, FastMCP, vLLM & Ray Serve, React, FastAPI, Zilliz

---

## Option C — Key prompts (short log)

| # | Prompt (abbreviated) | Outcome                                                                                                                                                                |
|---|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | Set up the foundational architecture using FastAPI, Beanie (MongoDB), and Cloudflare R2 for secure image uploads and retrieval. | Created the core backend REST API, data models, and integrated AWS S3 protocols for direct Cloudflare R2 CDN storage.                                                  |
| 2 | Integrate Google Gemini API to automatically generate semantic metadata (titles, descriptions, tags) upon image upload. | integrated that analyzes incoming image bytes via Gemini vision models, auto-populating MongoDB and reducing manual admin data entry.                                  |
| 3 | Decouple the AI capabilities by introducing an MCP (Model Context Protocol) Server and a conversational LangGraph agent. | Spun up a standalone FastMCP server that exposes tools (like hybrid portfolio search) and prompt over http streamable transport to the FastAPI LangGraph orchestrator. |
| 4 | Connect Zilliz (Milvus) Vector Database to enable semantic image search for the conversational agent. | Backfilled the portfolio into Zilliz using `gemini-embedding-2`, and built a hybrid search MCP tool for the chat assistant to answer visual queries.                   |
| 5 | Transition local model curation pipeline from LangChain to native OpenAI structured output schema. | Implemented a clean, high-performance structured parser inside `metadata_generator.py` using native OpenAI clients with Pydantic validation schemas.                   |
| 6 | Build a dual-model self-healing failover wrapper for VLM and chat services. | Programmed an automatic hot-swap system that switches queries between local vLLM (Ministral 14B on Anyscale) and Google Gemini API on communication timeout or OOM.    |
| 7 | Restructure the homepage layout to prioritize the AI Showcase sandbox and correct file drag-and-drop alignment. | Moved the interactive sandbox directly below the Hero section, added a glassmorphic model toggle, and built reactive drag-and-drop DOM event handlers.                 |
| 8 | Tighten system prompt rules in the MCP server configuration to prevent model leaks of tools or functions. | Relocated core security guidelines to the top of `bot_persona`, cleaned up nested string formatting, and fully restricted tool-signature listings.                     |

---

## Optional notes

- **Assumptions made:** When implementing the dual-model failover engine, we assumed that temporary timeouts or latency spikes from the local Anyscale vLLM cluster should seamlessly and silently hot-swap to the Google Gemini API. This prioritizes 100% uptime for public endpoints, even if it results in slight stylistic differences in the generated metadata or chat responses.
- **Future Improvements:**
  - Implement system-wide token and endpoint rate-limiting using Redis to protect the entire architecture.
  - Migrate the FastAPI `BackgroundTasks` (used for indexing metadata into Milvus) over to a dedicated, distributed task queue like Celery or RabbitMQ for enhanced reliability.
  - Transition the semantic search pipeline to utilize a fast, local multimodal embedding model, reducing external API dependencies and optimizing vector retrieval latency.
