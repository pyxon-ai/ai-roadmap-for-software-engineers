# Senior — Project 3: Auto commentary for soccer (vision + LLM + TTS)

## Goal

Build an **end-to-end pipeline** that ingests a **soccer match video (MP4)**, understands what is happening using **vision models** (and optionally audio), generates **natural-language commentary** with an **LLM**, synthesizes speech with **TTS**, and exports a new **MP4** with commentary laid on the timeline. Persist a **structured match analysis** in a **database** for querying and reuse.

This is a **senior-level** brief: multimodal inputs, orchestration, media I/O, and data persistence.

## User flow

1. **Upload** an MP4 of a soccer match (duration and resolution within what you document—e.g. clip length limits for MVP).
2. **Process** the video: sample frames or segments, run **vision** understanding (classification, captioning, event detection, or a video model—your choice; document trade-offs).
3. **Generate** commentary text with an **LLM** (play-by-play, highlights, or narrative—define the style in README).
4. **Synthesize** audio with **TTS** (one or more voices; note latency and sync strategy).
5. **Mux** commentary into an output **MP4** (mixed with stadium audio or commentary-only track—document).
6. **Store** match **analysis** in a **database**: e.g. timeline of events, detected actions, LLM segments, file paths, timestamps, optional embeddings for search.

## Technical expectations

| Area | Notes |
|------|--------|
| **Vision** | At least one of: frame sampling + image model, short clip embedding, or video-specific API/model. State FPS/interval and why. |
| **LLM** | Commentary conditioned on vision outputs (and optional metadata: scoreboard OCR if you add it—optional). |
| **TTS** | Cloud API (ElevenLabs, Azure, Google, etc.) or open-source; document voice and language. |
| **Video** | `ffmpeg` or Python bindings; clear how audio/video sync is handled. |
| **DB** | SQL (PostgreSQL/SQLite) or document store—schema for runs, segments, analysis JSON, output paths. |

## Security & ops

- **No hardcoded API keys**; env vars or secret files excluded from git.  
- Document **compute** needs (GPU optional; CPU-only path if possible).  
- If processing **user-uploaded** video, document **size limits** and **content policy** assumptions.

## Deliverables

- Runnable pipeline (CLI and/or minimal **FastAPI** upload endpoint is a plus).  
- **README:** architecture diagram or bullet pipeline, env vars, example command, sample output clip link or path.  
- **`prompts/`** per [submission rules](../../README.md#2-prompts-folder-required).

## MVP vs stretch

- **MVP:** Short clip (e.g. 1–3 minutes), coarse event timeline, single-voice TTS, one output MP4, DB row per job.  
- **Stretch:** Multi-language commentary, highlight-only mode, Dockerized worker, queue (Redis/Celery).

## PR checklist

- [ ] MP4 in → processed with vision + LLM + TTS → MP4 out  
- [ ] Commentary audio aligned well enough to document (known drift acceptable if explained)  
- [ ] Match analysis persisted to DB with a clear schema  
- [ ] README + `prompts/`  
- [ ] State in PR: **Senior — Project 3**
