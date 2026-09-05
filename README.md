# AI Chatbot with RAG & Tool-Calling Agent

A small end-to-end project exploring three core building blocks of modern AI applications: LLM API integration, Retrieval-Augmented Generation (RAG), and a basic tool-calling agent — built while learning these concepts hands-on with Python.

## Overview

This repository contains three standalone scripts that together demonstrate a practical understanding of how LLM-powered applications are built:

| File | What it does |
|---|---|
| `gemini.py` | A conversational chatbot using the Google Gemini API with persistent multi-turn memory |
| `rag.py` | A Retrieval-Augmented Generation pipeline: embeds documents, stores them in a vector database, retrieves relevant context for a question, and (optionally) sends that context to Gemini for a grounded answer |
| `agent.py` | A simple tool-calling agent that decides which function to call (calculator, weather lookup) based on the user's request |

## Tech Stack

- **Python 3**
- **Google Gemini API** (`google-genai`) — LLM chat and reasoning
- **ChromaDB** — vector database for storing and querying embeddings
- **Sentence-Transformers** (`all-MiniLM-L6-v2`) — local embedding generation
- **Regex (`re`)** — lightweight intent detection for the agent demo

## How It Works

### 1. Chatbot (`gemini.py`)
Uses `client.chats.create()` to open a chat session with Gemini, so conversation history is managed automatically across turns — no need to manually track message state.

### 2. RAG Pipeline (`rag.py`)
1. A small knowledge base of source text is split into documents.
2. Each document is converted into a vector embedding.
3. Embeddings are stored in a local ChromaDB collection.
4. When a question comes in, it's embedded the same way and used to query ChromaDB for the most relevant documents (semantic search).
5. The retrieved text is passed to Gemini as context, and the model answers strictly based on that context — reducing hallucination compared to asking the model "cold."

**Design note:** Embeddings are generated **locally** with Sentence-Transformers rather than through a remote embedding API. This was a deliberate architecture choice made after hitting a regional network-access restriction on the cloud embedding endpoint — running the embedding step locally keeps the whole pipeline functional without depending on that connection. Swapping in a cloud embedding API instead (e.g. Gemini's `embed_content`) would only require changing the `get_embedding()` function; the rest of the pipeline is unaffected.

### 3. Agent Demo (`agent.py`)
A minimal illustration of the core idea behind tool-calling agents: given a user request, the agent decides *which* tool is relevant (a calculator or a weather lookup) and calls it, rather than trying to answer everything with static text. This version uses simple pattern matching to keep the demo dependency-free and runnable offline; the same routing logic is what an LLM does more flexibly via native function-calling / tool-use APIs.

## Setup

bash
pip install google-genai chromadb sentence-transformers

Each script expects a Gemini API key. Set it as an environment variable rather than hardcoding it:

bash
# Windows (PowerShell)
$env:GEMINI_API_KEY="your-key-here"

# macOS/Linux
export GEMINI_API_KEY="your-key-here"


python
import os
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

Run any script directly:

bash
python gemini.py
python rag.py
python agent.py
`

## Known Limitations

- The agent demo uses rule-based intent detection rather than a real LLM function-calling API — this was a deliberate simplification for a fully offline, dependency-light demo, not a production approach.
- The knowledge base in rag.py is a small illustrative set of sentences, not a real document corpus — the pipeline is built to scale to larger, chunked documents with no structural changes.

## What I'd Build Next

- Wire the agent demo into the Gemini tools / function-calling API for real LLM-driven tool selection.
- Extend the RAG pipeline to ingest real documents (PDF/text files) with proper chunking.
- Add a small FastAPI wrapper so the pipeline is callable as a service rather than a script.

---

Author: Aramesh Rafiee
[github.com/aramesh-rafiee-dev](https://github.com/aramesh-rafiee-dev) · [linkedin.com/in/aramesh-rafiee-dev](https://linkedin.com/in/aramesh-rafiee-dev)
