# HDRS Projects RAG Pipeline — End-to-End Workflow for Internal AI Use Case Pitch

This document describes the complete **three-stage pipeline** that powers the HDRS Projects conversational AI — from raw web discovery to a production RAG service exposed via MCP.

---

## 🎯 Pitch Summary

> **One-liner**: An automated research-intelligence pipeline that continuously discovers, enriches, and makes queryable the entire HDRS technical transformation portfolio — accessible via natural language chat **and** standard MCP tool calls.

---

## 📊 Architecture Overview

```
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│  STAGE 1: GENERATE  │     │  STAGE 2: INGEST    │     │  STAGE 3: RETRIEVE  │
│  (Data Generation)  │────▶│  (Vector Ingestion) │────▶│  (RAG Retrieval)    │
└─────────────────────┘     └─────────────────────┘     └─────────────────────┘
       │                           │                           │
       ▼                           ▼                           ▼
  hdrs_projects_         hdrs3 collection           Chat / MCP Server
  prod_v5.csv            (Astra DB)                 (OpenRouter LLM)
```

---

## 🔄 Stage 1: Data Generation — *Automated Research Intelligence*

**File**: `hdrs_projects_core_data_generation.md`  
**Workflow**: `HDRS Data Generator` (LangFlow)

| Step | Component | Purpose |
|------|-----------|---------|
| 1. **Discovery** | HTTP Request → Parser → StructuredOutput | Fetches the official HDRS projects funding page; extracts 9-field project records via LLM |
| 2. **Enrichment Loop** | For each project: Web Search → Agent | Performs targeted web searches (GitHub, Zenodo, team pages, funding records) and feeds results to an Agent for deep extraction |
| 3. **Output** | JSON/CSV → File Save | Produces `hdrs_projects_prod_v5.csv` — a structured, queryable dataset for portfolio analysis |

**Key value**: Replaces manual research with an automated, repeatable pipeline that keeps the knowledge base current.

---

## 🗄️ Stage 2: Vector Ingestion — *Production-Ready Knowledge Base*

**File**: `hdrs_projects_core_data_vectorDB.md`  
**Workflow**: `HDRS RAG Ingest` (LangFlow)

| Stage | Operation | Details |
|-------|-----------|---------|
| 1. **Load** | File (CSV) → Message | Reads `hdrs_projects_prod_v5.csv` from local storage |
| 2. **Convert** | CSV → JSON | Transforms raw text to structured JSON records |
| 3. **Chunk** | RecursiveCharacterTextSplitter | `chunk_size=1000`, `chunk_overlap=200` — preserves context across boundaries |
| 4. **Embed & Store** | AstraDBVectorStore | **Collection**: `hdrs3`<br>**Embeddings**: NVIDIA NV-Embed-QA (1024 dims)<br>**Hybrid search**: Vector + lexical with NVIDIA reranker (`nvidia/llama-3.2-nv-rerankqa-1b-v2`)<br>**Records**: 53 project chunks |

**Incremental updates**: Uses `deletion_field` to refresh only changed projects — no full re-index needed.

---

## 💬 Stage 3: RAG Retrieval — *Hallucination-Free Q&A*

**File**: `hdrs_projects_core_data_vectorDB_retrieve.md`  
**Workflow**: `HDRS RAG Retrieve` (LangFlow)

| Component | Configuration |
|-----------|---------------|
| **Vector Store** | Astra DB `hdrs3` (same as ingestion) |
| **Search** | Similarity, top-4 results, cached |
| **Reranker** | NVIDIA `llama-3.2-nv-rerankqa-1b-v2` (disabled for pure vector search; available for hybrid) |
| **LLM** | OpenRouter (Agent mode) |
| **Prompt** | Strict grounding — **answer ONLY from retrieved context** |
| **Memory** | Session-aware for follow-up questions |

**Use case example**:  
> **User**: "What is the Cardinal project about?"  
> **Pipeline**: Vector search → top-4 chunks → Agent answers: *"Based on the knowledge base, the Cardinal project is..."*

---

## 🔌 MCP Exposure — *Standardised AI Access*

**Repository**: `https://github.com/zwelshman/hdrsMCP/blob/main/server.py`

The RAG retrieval pipeline is wrapped as an **MCP (Model Context Protocol) server**, exposing:

| MCP Tool | Description |
|----------|-------------|
| `search_hdrs_projects(query)` | Semantic search over the `hdrs3` collection — returns top-k project chunks with metadata |
| `ask_hdrs_projects(question)` | Full RAG answer (retrieval + LLM synthesis) — grounded, cited, session-aware |

**Why MCP matters**:
- **Interoperable**: Any MCP-compatible client (Claude Desktop, Cursor, custom agents) can call the tools directly
- **No custom SDK**: Standard JSON-RPC over stdio/HTTP
- **Composable**: Chain with other MCP servers (GitHub, filesystem, databases) for multi-step workflows
- **Governance**: Tool-level access control, audit logs, rate limiting

> **Assumption for pitch**: The MCP server pulls live from the Astra DB `hdrs3` collection (not a local CSV copy), ensuring answers always reflect the latest ingestion.

---

## 🎪 Demo Flow for Internal Audience

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Run **Generation** pipeline | Fresh `hdrs_projects_prod_v5.csv` with latest project metadata |
| 2 | Run **Ingestion** pipeline | `hdrs3` collection updated; 53 chunks indexed |
| 3 | Open **Retrieval** chat | Ask: *"Which projects use NVIDIA embeddings?"* → grounded answer |
| 4 | Call MCP tool `search_hdrs_projects("funding amount > £1M")` | Structured JSON results — reusable in downstream automation |
| 5 | Call MCP tool `ask_hdrs_projects("Summarise the Cardinal project")` | Narrative answer with implicit citations |

---

## 📈 Business Value Points

| Dimension | Impact |
|-----------|--------|
| **Time-to-insight** | Minutes vs. days for portfolio questions |
| **Freshness** | Generation pipeline can run on schedule (weekly/monthly) |
| **Governance** | Strict grounding = no hallucinations; audit trail via MCP logs |
| **Extensibility** | Swap embedding model, add reranker, plug new data sources — all without changing MCP interface |
| **Reuse** | Same `hdrs3` collection powers chat, analytics dashboards, and agentic workflows |

---

## 🛠️ Next Steps for Production

1. **Schedule Generation** — Cron/airflow job to re-fetch HDRS page quarterly
2. **CI/CD for Ingestion** — Automate on CSV change; run tests on chunk quality
3. **MCP Hardening** — Auth, rate limits, observability (Langfuse / OpenTelemetry)
4. **Eval Harness** — Golden Q&A set to regression-test retrieval + answer quality
5. **Internal Launch** — Publish MCP server to internal registry; document tool schemas for citizen developers

---

## 📎 References

- Generation pipeline: `hdrs_projects_core_data_generation.md` [3]
- Ingestion pipeline: `hdrs_projects_core_data_vectorDB.md` [2]
- Retrieval pipeline: `hdrs_projects_core_data_vectorDB_retrieve.md` [1]
- MCP server: `https://github.com/zwelshman/hdrsMCP/blob/main/server.py`

---

**Ready to demo?** I can walk through each stage live, show the LangFlow graphs, and run sample MCP calls against the deployed server.
