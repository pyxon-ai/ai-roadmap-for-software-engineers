# Junior — Project 2: RAG application (modern LLM stack)

## Inspiration

This matches the phase where roles shift toward **LLM products**: a **RAG chatbot**—upload **PDFs** (or docs), **embed** chunks, **retrieve**, answer with an **LLM API**, optionally **conversation memory**. Many transition stories cite this exact project type as what moved interviews forward, together with a **clean GitHub** and **deployed demo**.

## Goal

Prove you can wire **retrieval + generation**: embeddings, a **vector database**, and a real **LLM** (OpenAI, Anthropic, local via Ollama, etc.).

## Scope

- **Ingestion:** PDFs and/or other documents you parse into text chunks.  
- **Embeddings + vector store:** e.g. Chroma, Pinecone, Qdrant, Weaviate, FAISS—pick one and justify.  
- **Retrieval:** top-k similarity (optionally hybrid keyword + dense later).  
- **Generation:** LLM answers **grounded** on retrieved chunks; **citations** or source snippets are a plus.  
- **Optional:** short-term **chat memory**; **SQL** for metadata if you want to show structured queries.

## Requirements

- **End-to-end path:** user question → retrieve → LLM answer (no fake “TODO” in the critical path).  
- **README:** env vars, how to index sample docs, example questions.  
- **Demo:** **live link** strongly preferred (Streamlit, Hugging Face Spaces, etc.).  
- **`prompts/`** per [submission rules](../../README.md#2-prompts-folder-required).

## Optional stretch (from org-specific briefs)

If you want extra depth: **Arabic** text support, **diacritics**, or a **small benchmark** on retrieval quality—document in README.

## PR checklist

- [ ] RAG pipeline: chunk → embed → store → retrieve → LLM  
- [ ] Vector DB in the loop  
- [ ] Working demo + README with env vars  
- [ ] `prompts/`  
- [ ] State in PR: **Junior — Project 2**
