# hdrsMCP (HDRS Projects Tracker)

[![Stars](https://img.shields.io/github/stars/zwelshman/hdrsMCP?style=flat-square&logo=github&color=blue)](https://github.com/zwelshman/hdrsMCP/stargazers)
[![Forks](https://img.shields.io/github/forks/zwelshman/hdrsMCP?style=flat-square&logo=git&color=orange)](https://github.com/zwelshman/hdrsMCP/network/members)
[![Issues](https://img.shields.io/github/issues/zwelshman/hdrsMCP?style=flat-square&logo=issues&color=critical)](https://github.com/zwelshman/hdrsMCP/issues)
[![Repo Size](https://img.shields.io/github/repo-size/zwelshman/hdrsMCP?style=flat-square&logo=codeforces&color=success)](https://github.com/zwelshman/hdrsMCP)

A lightweight, FastMCP server that currently sintegrates the Health Data Research (HDRS) projects database directly into your AI assistant (such as Cursor, VS Code, or Claude Desktop). It allows LLMs to query, filter, and match health data projects, institutions, and infrastructure requirements using natural language.

## 🛠️ Tech Stack

* **Core Protocol:** Model Context Protocol (MCP)
* **Framework:** FastMCP (Python), Langflow for the data pipeline
* **Data Processing:** Pandas (Vectorized operations)
* **Deployment:** Uvicorn (SSE) or Local CLI

## 📊 Data Pipeline

* **Source:** A centralized CSV dataset (`data/hdrs_projects_2026-12-06.csv`) tracking project metadata, funding awards, institutions, and key contacts, built using a Langflow pipeline.
* **Processing:** Loads strictly in read-only mode, leveraging fast, in-memory Pandas dataframe filtering to instantly retrieve project context without token bloat.

## 🚀 Supported MCP Capabilities

Your AI assistant will automatically discover and utilize the following targeted data tools:

* `get_dataset_summary()` – Retrieve a high-level summary of total tracked projects and unique hosting institutions/networks.
* `search_projects(keyword)` – Perform a vectorized keyword search across all textual fields for quick project discovery.
* `get_projects_by_institution(institution_name)` – Filter the database by specific hosting networks (e.g., 'Wessex SDE').
* `get_project_details(project_name)` – Fetch comprehensive, markdown-formatted metadata for a specific project.
* `match_service_to_projects(service_keywords, requires_sde_infrastructure)` – Score and rank projects based on their relevance to specific services, tech stacks (e.g., 'PySpark'), or Secure Data Environment (SDE/TRE) requirements.
* `find_infrastructure_fit(tech_requirement, domain)` – Cross-reference infrastructure needs (e.g., 'Safe Haven') with specific clinical domains (e.g., 'cardiovascular').
* `get_service_pitch_contacts(project_name)` – Extract key stakeholders, lead institutions, and reference URLs for collaboration routing and service pitches.

## ⚙️ Deployment & Integration

The server can be run locally or hosted remotely via Uvicorn as an SSE (Server-Sent Events) endpoint.

### VS Code / Cursor Configuration (Hosted SSE)

If you deploy the Uvicorn ASGI app (`app = mcp.sse_app()`) to a hosting platform, connect your IDE using the HTTP transport:

```json
{
  "mcpServers": {
    "hdrs-projects-tracker": {
      "type": "http",
      "url": "https://hdrsmcp.onrender.com.mcp/sse"
    }
  }
}

```
