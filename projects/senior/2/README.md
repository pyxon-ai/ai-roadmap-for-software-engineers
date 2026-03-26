# Senior — Project 2: Production LLM/RAG service (MLOps-style)

## Inspiration

Many successful transitions lean on a **developer superpower**: **shipping**. Take a RAG or LLM app **beyond a notebook**—**API** (e.g. **FastAPI**), **Docker**, **experiment or observability** tooling (**MLflow**, **Weights & Biases**, or basic logging), **deploy** to a cloud target (**AWS**, **GCP**, **Azure**), and think about **latency**, **token usage**, **rate limits**, and **fallbacks**—the same themes that show up in **system design** interviews (chatbot architecture, monitoring in production).

## Goal

Demonstrate **production-minded** delivery: your model or RAG stack is **containerized**, **observable**, and **deployed** (or realistically deployable with a single command + env file).

## Scope

- **API:** **FastAPI** (or equivalent) exposing at least: health check + **query** endpoint for your RAG/LLM flow.  
- **Container:** **Dockerfile**; optional `docker-compose` for app + vector DB.  
- **Observability:** track **latency**, **token usage** (if applicable), and/or errors—simple structured logs count.  
- **Cloud:** deploy to **one** cloud (ECS, Cloud Run, App Service, EC2 + script, etc.) **or** provide a **clear, tested** path (Terraform/CD optional).  
- **Resilience:** document **rate limits**, **timeouts**, or **fallback** behavior you considered.

## Optional (bonus)

- **Multi-agent** router on top of the same API (thin orchestration layer).  
- **K8s/Helm** sketch if you already use them.

## Deliverables

- Repo runs locally **and** in Docker per README.  
- **`prompts/`** per [submission rules](../../README.md#2-prompts-folder-required).

## PR checklist

- [ ] FastAPI (or equivalent) service  
- [ ] Docker artifact  
- [ ] Monitoring/logging of latency and/or tokens (or justified alternative)  
- [ ] Deployment notes or live URL  
- [ ] README + `prompts/`  
- [ ] State in PR: **Senior — Project 2**
