# Chunking Decisions

## Python — AST-based chunking

**Why:** Python's `ast` module lets us extract semantically meaningful units (functions, classes) rather than arbitrary character windows. This yields chunks that represent complete, self-contained logic, which dramatically improves retrieval relevance.

**Trade-off:** AST parsing fails on Python 2 syntax or heavily macro-generated code → graceful fallback to sliding window.

**Truncation at 2000 chars:** Avoids exceeding embedding model token limits while keeping the most important part of large functions.

## Markdown — heading-based chunking

**Why:** Markdown documents are structured by headings. Splitting on `#`, `##`, `###` preserves thematic coherence — each chunk answers a single topic.

**Trade-off:** Very short sections (< 50 chars) are dropped. Sections > 2000 chars are truncated.

## TypeScript / JavaScript / Go / Rust — sliding window

**Why:** No reliable cross-language AST library in pure Python. Sliding window with overlap (64 tokens) ensures no information is lost at chunk boundaries.

**Parameters:**
- `chunk_size = 512 tokens` ≈ 2048 chars — fits comfortably in `text-embedding-3-small` (8191 token limit)
- `overlap = 64 tokens` ≈ 256 chars — enough context to avoid cutting mid-function

**Why not tree-sitter?** Adds a native binary dependency and complicates Docker builds. Sliding window is sufficient for v1.

## File-level filters

- Skip files > 100 KB: these are typically generated files (minified JS, lockfiles) with low Q&A value
- Skip chunks < 50 chars: too short to be meaningful for retrieval
- Cap at 50 chunks/file: prevents a single giant file from dominating the collection
