# Senior — Project 1: Agentic AI (search + web/API tools)

## Inspiration

Senior AI engineering work is often **agentic**: the model **decides** when to call **tools**—search the web, **fetch URLs or APIs**, then **synthesize** grounded answers. This bundles the “search agent” and “URL/API agent” patterns into **one coherent portfolio piece** you can extend toward production later.

## Goal

Build an **agent** (LangChain, LangGraph, LlamaIndex, or custom) that uses:

1. **Search** — web or news search (Google CSE, Tavily, SerpAPI, Bing, etc.).  
2. **HTTP** — **GET** (and optionally **POST**) to public URLs or JSON APIs; parse HTML/JSON for the model.

The LLM should **reason** over tool outputs and return answers with **sources** or citations where possible.

## Scope

- **Tool use:** explicit ReAct-style, function-calling, or graph nodes—document the pattern.  
- **Optional:** light **RAG** over fetched text (embed snippets, retrieve, then generate).  
- **Safety:** no hardcoded keys; document **allowlists** or warnings if URLs are user-supplied (`allow_dangerous_requests`, SSRF, etc.).

## Deliverables

- Runnable code + **README** (deps, env vars, example questions).  
- At least one flow that uses **search** and at least one that uses **HTTP** to real public endpoints.  
- **`prompts/`** per [submission rules](../../README.md#2-prompts-folder-required).

## PR checklist

- [ ] Search-backed Q&A path  
- [ ] URL/API-backed Q&A path  
- [ ] Security notes in README  
- [ ] README + `prompts/`  
- [ ] State in PR: **Senior — Project 1**
