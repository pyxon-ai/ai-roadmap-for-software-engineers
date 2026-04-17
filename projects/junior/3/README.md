# Junior — Project 3: Football video & AI commentator

This project combines a **vision backbone** (player/ball tracking) with an optional **full-stack AI commentator** path: analysis → LLM scripts → **TTS** → **MP4**, **database**, **English + Arabic** commentary, and **three progressive submission levels**.

**AI Football Commentator** (below) is a **portfolio challenge**: submissions may be **reviewed**; strong work may be considered for **follow-up interviews**, **roles**, or **other compensation**—subject to organizer availability and fit. Nothing here is a guaranteed offer.

---

## Part A — Vision backbone (upstream source)

Anchor your perception layer on this open-source project:

| | |
|--|--|
| **Upstream** | [**github.com/MuhammadMoinFaisal/football_analysis**](https://github.com/MuhammadMoinFaisal/football_analysis) |
| **Summary** | Detects and tracks **players**, **referees**, and the **ball** through match video using **YOLO11**, with `input_videos`, `output_videos`, training notebooks, and a Python stack (Ultralytics, OpenCV, supervision, etc.). |

Use it as the **reference** you study, fork, or extend. Cite it and respect its **license** and **model weights** terms. This roadmap repo is **not** affiliated with the upstream authors.

**Minimum vision deliverable:** run or reproduce **detection + tracking** on sample **MP4**; document how YOLO11 outputs are produced (tracks, boxes, IDs). You may stop here for a **vision-only** submission if you clearly label scope—or continue to **Part B**.

---

## Part B — AI commentator (full challenge)

### One-liner

**In:** match footage (MP4). **Out:** MP4 with **AI-generated commentary** audio (and optional mix). **Store:** structured **match analysis** in a **database**. **Languages:** at least **English** and **Arabic** (separate tracks, alternating segments, or your design—document it).

### Why this project

It mirrors **multimodal AI engineering**: vision over video, LLM reasoning, speech synthesis, media tooling, and persistence.

### Core requirements

| # | Requirement |
|---|----------------|
| 1 | **Video analysis** — Use AI (vision and/or audio) to understand what is happening in a soccer match clip (events, tempo, scenes—your scope; document assumptions). |
| 2 | **Commentary generation** — Use an **LLM** (or equivalent) to produce **commentary scripts** grounded in your analysis. |
| 3 | **TTS** — Convert commentary to speech and **mux** into an **output MP4** (replace or mix with original audio—document). |
| 4 | **Database** — Persist **match / job analysis** (timestamps, segments, metadata, paths to assets—clear schema). |
| 5 | **Bilingual commentary** — At least **English** and **Arabic** spoken commentary in the deliverable (both must be present and intentional). |
| 6 | **Video evidence** — Provide **input sample** and **output MP4** with commentary (see submission). |

### Evaluation bonus: open source only

Solutions are **scored higher** if the **entire inference stack** for analysis, generation, and TTS is **open source**. If you use **any** closed API or proprietary model, **declare it** in the README—solutions **can still pass**; **OSS-only** is a distinct evaluation lane.

*Examples:* local LLMs (Ollama, llama.cpp), open TTS (Coqui, Piper, MMS), open vision models—list **every component** and its license.

---

## Three levels of submission (progression)

Meet **Part B** core requirements at the level you target—document **which level(s)** you implemented.

| Level | What you ship | Typical stack |
|-------|----------------|---------------|
| **1 — Web app + upload** | **Commentary + TTS** behind **Flask** (or similar): user **uploads an MP4**, server runs analysis → LLM → TTS → **downloadable output MP4**. | Flask/FastAPI, file upload, DB for jobs and analysis. |
| **2 — Live stream (WebSocket)** | **Video streams in real time**; browser ↔ server over **WebSockets** (and MSE / WebRTC / chunks—document). Commentary and TTS track the **live stream**. | `socket.io` or native WS, async workers; persist to **DB** where feasible. |
| **3 — Dynamic commentator + stream** | **Level 2** plus **controls**: persona/tone, **voice / TTS preset**, **language mix** (still **EN + AR** minimum)—then **stream** with those settings. | Dashboard → config per session/job → parameterized prompts and TTS. |

State in your README: **“Submission level: 1 / 2 / 3”** and what is out of scope.

---

## Submission model: **private** + **video upload**

Public drive-by PRs are **not** appropriate for full match video or proprietary assets.

1. **Code (private GitHub repo + reviewer)**  
   - Host your solution in a **private** GitHub repository (**private fork** of this roadmap if you started here, or a new private repo).  
   - Invite **[`enghamzasalem`](https://github.com/enghamzasalem)** as a **collaborator** (**Settings → Collaborators and teams → Add people**) with at least **read** access.  
   - Alternative: **zip** through an agreed secure channel (document in your registry PR).
2. **Video** — Do **not** attach large MP4s to a public issue. Use **private** object storage (time-limited, password if needed) or an organizer-provided upload.
3. **Written pack** — Architecture, runbook, **OSS vs closed** components, demo links, **hashes** or filenames of submitted videos.

**Reviewer GitHub:** [`https://github.com/enghamzasalem`](https://github.com/enghamzasalem)

---

## What to deliver (checklist)

- [ ] **Scope** — State **Part A only** (vision) or **Part A + Part B** (commentator), and **submission level** **1 / 2 / 3** if doing Part B.  
- [ ] **Runnable** pipeline / **web app** with `README` (env vars, GPU/CPU, commands).  
- [ ] **Input + output** media via **private** upload; for level **2+**, note or clip proving **stream** behavior if needed.  
- [ ] **English** and **Arabic** on output for Part B (explain track layout in README).  
- [ ] **Database** schema + examples (Part B).  
- [ ] **`prompts/`** per [submission rules](../README.md#submission-rules).  
- [ ] **OSS declaration** table (Part B).  
- [ ] **`enghamzasalem`** invited to your **private** repo (or zip path documented).  
- [ ] **Do not** commit large MP4s to this monorepo—use **Git LFS**, links, or `.gitignore`.

---

## PR / registry checklist (this monorepo as index)

- [ ] Optional **short entry** (e.g. `projects/junior/submissions-ai-football/your-team.md`) with **contact**, confirmation **`enghamzasalem`** has repo access (or zip note), **private video link**, **SHA/tag**—**no secrets**.

State in any PR: **Junior — Project 3**.

---

## Evaluation rubric (summary)

| Area | Weight |
|------|--------|
| **Part A:** working **vision** pipeline grounded in [**football_analysis**](https://github.com/MuhammadMoinFaisal/football_analysis) | High (if vision-only) |
| **Part B:** **video → analysis → EN+AR TTS → MP4** (level **1** minimum) | High |
| **Level 2–3:** WebSocket streaming, **dynamic** commentator controls | High / differentiation |
| **OSS-only** stack (where claimed) | Bonus / tier |
| **DB**, **README**, **`prompts/`**, **private** submission hygiene | Medium |
| **Security** and **licensing** disclosure | Required |

---

## Technical notes (non-binding)

- **Vision:** sampled frames, short clips, or open video models—justify cost vs quality.  
- **Sync:** document drift between events and TTS.  
- **Safety:** no hardcoded secrets; content policy for uploads.

---

## FAQ

**Vision-only vs full commentator?** **Part A** alone is valid if clearly labeled. **Part B** adds LLM, TTS, DB, EN+AR, and levels **1–3**.

**What are the three levels?** **(1)** Flask + MP4 upload + TTS output; **(2)** **WebSockets** + live video; **(3)** **dynamic** commentator settings, then stream.

**Do I need WebSockets?** Only for levels **2** and **3**.

**How do I submit code privately?** **Private** GitHub repo + invite **`enghamzasalem`**—see **Submission model** above.

**Can I use cloud APIs?** Yes; label them; OSS-only is a separate lane.

**Minimum clip length?** Declare your tested range (e.g. 1–5 minutes for MVP).

**Arabic dialect?** MSA or a stated dialect; document TTS engine and limitations.

---

*This challenge is a learning and portfolio framework. Official hiring is only through real employer processes and contracts.*
