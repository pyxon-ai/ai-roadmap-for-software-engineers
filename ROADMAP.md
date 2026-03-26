# Roadmap to AI for Software Engineers (Pyxon)

This roadmap aligns with Pyxon’s **Junior** and **Senior AI Engineer** job descriptions: from core Python and LLM tooling to enterprise deployment, security, and client-facing delivery.

**Diagrams:** see the [README](README.md) (SVG figures).

---

## Phase 1 — Foundation (about 2–3 months)

**Goal:** Solid Python, basic ML/LLM concepts, and hands-on use of tools named in the Junior role.

- **Python:** Data structures, OOP, async where relevant, `requests`, JSON, subprocess, packaging basics.
- **AI/ML fundamentals:** Training vs inference; supervised/unsupervised intuition; metrics (accuracy, F1, etc.) at a practical level.
- **Transformers & LLMs:** Tokens, attention, embeddings; skim “Illustrated Transformer” and Hugging Face NLP course intro.
- **Ollama:** Run models locally (e.g. Llama, Mistral); call the HTTP API from Python.
- **AI APIs:** OpenAI, Anthropic, Google AI — small scripts, error handling, retries, config-driven provider switch.
- **AI-assisted dev:** Cursor, Copilot, or similar in daily workflow (explicitly in the Junior JD).

**Milestone:** You can explain training vs inference, run a local model, and call cloud LLM APIs from code.

---

## Phase 2 — Core AI engineering (Junior profile, about 3–4 months)

**Goal:** Match Pyxon Junior core bar: RAG, agents, APIs, documentation, collaboration.

- **Prompting:** Zero/few-shot, chain-of-thought, structured outputs; simple evals on fixed tasks.
- **RAG end-to-end:** Chunking, embeddings (e.g. sentence-transformers), vector DB (Chroma, Qdrant, etc.), retrieval, generation via Ollama or APIs.
- **Agents:** LangChain or LlamaIndex — tools, memory, multi-step flows; one “tool-using” agent project.
- **Integration:** Wrap RAG/agents as services; log latency and failures; basic observability.

**Milestone:** A portfolio “chat with your documents” app and an agent that uses at least one tool reliably.

---

## Phase 3 — Specialization (path to Senior depth, about 3–4 months)

**Goal:** Cover Junior “nice-to-haves” and Senior prerequisites (fine-tuning, ops, cloud).

- **Fine-tuning:** LoRA/QLoRA with Hugging Face `peft` / `transformers`; small domain or style dataset.
- **Advanced RAG:** Re-ranking, hybrid search, multi-document reasoning; measure quality vs baseline.
- **Docker & MLOps:** Containerize apps; touch MLflow/DVC or similar; `docker-compose` for app + DB + optional local LLM.
- **Cloud AI:** One of AWS (SageMaker/Bedrock), GCP (Vertex), or Azure AI — deploy a container or use managed APIs.
- **Optimization & edge (optional):** Quantization (GGUF/GPTQ), `llama.cpp`, Raspberry Pi / Jetson experiments.

**Milestone:** One fine-tuned or heavily customized pipeline, containerized, with a minimal cloud or automated deploy story.

---

## Phase 4 — Senior leadership & enterprise (about 4–6+ months, ongoing)

**Goal:** Align with Senior JD: lead deployments, security/compliance, customer work, full lifecycle.

- **Kubernetes & Helm:** Deployments, Services, Ingress, ConfigMaps/Secrets; package your stack as a Helm chart; practice on minikube/kind then a cloud cluster.
- **CI/CD:** GitHub Actions / GitLab CI — build, test, scan, push images, deploy to staging/prod.
- **IaC:** Terraform or Pulumi for VPC, clusters, IAM, managed DBs — match how real enterprises provision.
- **Security & compliance:** Encryption in transit/at rest, private endpoints, RBAC, data residency awareness; threat model for “LLM + enterprise data.”
- **Client-facing skills:** Discovery questions, architecture decks, phased rollout, handover docs — practice with mock stakeholders.
- **Multi-modal / TTS (Senior plus):** Integrate or fine-tune TTS where relevant (Whisper, Coqui, vendor APIs) per JD.

**Milestone:** You can whiteboard a private/hybrid deployment, list risks and controls, and own a chart from code to production cluster.

---

## Quick reference: Junior vs Senior (from JDs)

| Area | Junior emphasis | Senior emphasis |
|------|-----------------|-------------------|
| **Role** | Build, integrate, optimize, document; work with seniors | Lead end-to-end deployments; bridge platform and enterprise clients |
| **RAG & agents** | Implement and maintain pipelines | Architect performant, secure, customer-specific solutions |
| **Models** | APIs + Ollama; strong Python | Fine-tuning (LoRA/QLoRA), TTS customization, deeper behavior analysis |
| **Infrastructure** | Docker; cloud AI familiarity | Kubernetes + Helm; deep cloud networking; IaC |
| **Security** | Good API hygiene | Private/hybrid/on-prem, compliance, VPCs, private links |
| **Stakeholders** | Team collaboration | Direct work with client IT/engineering as technical advisor |

---

## Next step: portfolio project

After you have covered the phases above, pick **one** portfolio brief under the [Junior](projects/junior/README.md) (options **1–2**) or [Senior](projects/senior/README.md) (options **1–3**) track, implement it, and open a pull request. Include a **`prompts/`** folder in your submission (see **[projects/README.md](projects/README.md)**).

---

## Applying at Pyxon

Per the job posts: send CV and portfolio to **muneerah@pyxon.com** with **“Junior AI Engineer”** or the appropriate title in the subject line.
