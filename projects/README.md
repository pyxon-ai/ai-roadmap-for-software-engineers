# Projects

After the [learning roadmap](../ROADMAP.md), you can build a **portfolio project** and submit it here. Pick a **Junior** or **Senior** track, then **one** project brief, implement it, and open a **pull request**.

| Track | Projects |
|--------|----------|
| [Junior](junior/README.md) | [1 — Applied ML / NLP + Streamlit](junior/1/README.md) · [2 — RAG application](junior/2/README.md) |
| [Senior](senior/README.md) | [1 — Agentic AI (search + web/API)](senior/1/README.md) · [2 — Production LLM/RAG service](senior/2/README.md) · [3 — Auto soccer commentary (vision + LLM + TTS)](senior/3/README.md) |

**Junior** options follow a common path: classical ML demos → **RAG**. **Senior** adds **agentic tools**, **production** services, and an optional **multimodal** build (video + speech).

---

## Repository layout (when you submit)

Add **one folder** under the track you are targeting:

```text
projects/<junior|senior>/<your-name-or-project-slug>/
  README.md              # how to run, architecture, stack
  prompts/               # required — see below
  ... your code ...
```

Example: `projects/junior/jane-doe-rag-parser/` or `projects/senior/acme-agent-swarm/`.

---

## Submission rules

### 1. Pull request

1. Fork this repo and create a branch (e.g. `project/yourname-junior-1`).
2. Add your project under `projects/junior/...` or `projects/senior/...` as above.
3. Open a PR with contact info, which **numbered project** you chose, how to run, and a demo link if the brief asks for it.

### 2. `prompts/` folder (required)

Every submission **must** include a **`prompts/`** directory at the root of your project folder. This shows **how you used AI coding tools** (Cursor, Claude Code, GitHub Copilot, etc.) or documents your **step-by-step process** without tooling.

Include a **`prompts/README.md`** that covers at least one of:

| Approach | What to add |
|----------|-------------|
| **A. Tool history** | Exports or copies of relevant chats (Cursor, Claude Code, etc.), or links to gists—**redact secrets**. |
| **B. Step-by-step** | A clear narrative: phases, decisions, what you tried, what failed, what you shipped. |
| **C. Prompt log** | A list of **important prompts** you used and **what each produced** (short bullets are fine). |

You may add extra files under `prompts/`, for example:

- `prompts/process.md` — timeline or checklist  
- `prompts/key-prompts.md` — table of prompts → outcomes  
- `prompts/cursor-export.md` — pasted export (no API keys)

**Do not** commit API keys, tokens, or private URLs.

A **[starter template](prompts/README.template.md)** is available—copy it into your project as `prompts/README.md` and fill it in.

### 3. Security & quality

- No hardcoded secrets; use environment variables.  
- Document dependencies and env vars in your project `README.md`.

### 4. Official hiring

If you are applying to a **specific company**, follow their official repo and deadlines too. This repo is a **community roadmap companion**.

---

## PR description (minimum)

- **Contact** (email or phone)  
- **Track** (Junior / Senior) and **project number** (Junior: **1 or 2**; Senior: **1, 2, or 3**)  
- **Summary** and **how to run**  
- **Demo link** when the project brief requires it  
- Confirmation that **`prompts/`** is included and what format you used (A / B / C)

---

## Evaluation (high level)

- Meets the README for the **numbered project** you chose.  
- Code quality, docs, and runnable setup.  
- **`prompts/`** shows honest process—helpful for reviewers understanding trade-offs.  
- Security hygiene (secrets, dangerous URL fetch, etc., as applicable).
