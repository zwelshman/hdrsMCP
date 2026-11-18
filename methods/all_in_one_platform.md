This is a compelling multi-MCP orchestration scenario. Before I design the integrated workflow, I need to clarify a few things to make the demo concrete and high-impact.

# Integrated Multi-MCP Workflow: BHF DSC Project Support Analysis

## 🎯 Executive Summary for Technical Programme Directors

> **One question, four MCPs, one orchestrated answer** — replacing 2-3 weeks of manual cross-referencing with a 5-minute AI-driven analysis that identifies HDRS projects needing BHF DSC support, maps their data/phenotype needs, and generates OpenSAFELY starter code where applicable.

---

## 🔄 End-to-End Workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ORCHESTRATION LAYER (AI Agent)                       │
│  "Which HDRS projects would benefit from BHF DSC support? Identify         │
│   projects, people, datasets, phenotypes. If OpenSAFELY project,           │
│   generate boilerplate code."                                               │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        ▼                           ▼                           ▼
┌───────────────┐           ┌───────────────┐           ┌───────────────┐
│  HDRS MCP     │           │ GatewayMCP    │           │ Phenotype     │
│  (RAG)        │           │ (HDRUK GW)    │           │ Library MCP   │
└───────┬───────┘           └───────┬───────┘           └───────┬───────┘
        │                           │                           │
        │  1. List all HDRS         │  2. For each project:     │  4. For each
        │     projects + metadata   │     - Search datasets     │     phenotype:
        │     (PI, theme, tech)     │       by theme/keywords   │     - Get codelist
        │                           │     - Find data uses      │     - Check
        │                           │       (similar projects)  │       OpenSAFELY
        │                           │     - Get publications    │       port
        │                           │     - Find tools          │
        └───────────────────────────┼───────────────────────────┘
                                    │
                                    ▼
                         ┌───────────────────┐
                         │  OpenSAFelyMCP    │
                         │  (Code Gen)       │
                         └─────────┬─────────┘
                                   │
                         5. For OpenSAFELY-
                            suitable projects:
                            - Generate
                            study definition
                            - Codelist imports
                            - Action boilerplate
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │  SYNTHESISED DELIVERABLE    │
                    │  - Project prioritisation   │
                    │  - Dataset/phenotype map    │
                    │  - OpenSAFELY starter kits  │
                    │  - Gap analysis             │
                    └─────────────────────────────┘
```

---

## 📋 Step-by-Step Execution Trace

### Step 1: HDRS MCP — Portfolio Discovery
**Tool**: `ask_hdrs_projects` (RAG retrieval + synthesis)

```python
question = """
List all HDRS technical transformation projects with:
- Project name & PI / key personnel
- Research theme / disease area
- Technical approach (OpenSAFELY, SQL, Python, other)
- Current datasets used or needed
- Phenotypes / codelists referenced
- Funding stage / maturity
"""
```

**Expected Output** (grounded in `hdrs3` collection):
| Project | PI | Theme | Tech Stack | Datasets | Phenotypes |
|---------|-----|-------|------------|----------|------------|
| Cardinal | Dr. X | Cardiovascular | OpenSAFELY, Python | GDPPR, HES | Heart failure, MI |
| Project B | Prof. Y | Respiratory | SQL, R | CPRD, HES | COPD, Asthma |
| Project C | Dr. Z | Diabetes | Python, Spark | GDPPR, ONS | T2D, HbA1c |
| ... | ... | ... | ... | ... | ... |

---

### Step 2: GatewayMCP — Dataset & Ecosystem Mapping
**Tools**: `search_datasets`, `search_collections`, `search_data_uses`, `search_tools`, `search_publications`

```python
# For each HDRS project from Step 1:
for project in hdrs_projects:
    # 2a: Find relevant Gateway datasets
    datasets = search_datasets(
        keyword=project.theme + " " + " ".join(project.phenotypes),
        custodian=["NHS England", "SAIL", "CPRD"]
    )
    
    # 2b: Find BHF DSC collections
    collections = search_collections(keyword="BHF Data Science Centre")
    
    # 2c: Find prior data uses (what similar projects used)
    data_uses = search_data_uses(dataset_id=datasets.top_ids)
    
    # 2d: Find existing phenotyping tools on Gateway
    tools = search_tools(keyword=project.phenotypes[0])
    
    # 2e: Find publications for evidence base
    pubs = search_publications(dataset_id=datasets.top_ids)
```

**Value**: Connects HDRS projects to *actual accessible datasets*, *approved research precedents*, and *reusable tools* on the Gateway.

---

### Step 3: PhenotypeLibraryMCP — Phenotype Standardisation Check
**Tools**: `search_phenotypes`, `get_phenotype`, `get_codelist`

```python
# For each phenotype mentioned in HDRS projects:
for phenotype_name in all_phenotypes:
    # 3a: Check if phenotype exists in library
    lib_entry = search_phenotypes(name=phenotype_name)
    
    if lib_entry.exists:
        # 3b: Get canonical codelist (SNOMED, ICD-10, Read)
        codelist = get_codelist(phenotype_id=lib_entry.id, terminology="SNOMED")
        
        # 3c: Check OpenSAFELY port status
        opensafely_port = get_opensafely_implementation(phenotype_id=lib_entry.id)
    else:
        # Gap: phenotype not in library
        gap_report.add(phenotype_name, "Missing from Phenotype Library")
```

**Output**: Phenotype ↔ Codelist ↔ OpenSAFELY readiness matrix.

---

### Step 4: OpenSAFELYMCP — Boilerplate Generation
**Tools**: `generate_study_definition`, `generate_codelist_import`, `generate_actions_boilerplate`

```python
# For projects flagged as OpenSAFELY-suitable (from HDRS tech stack + phenotype readiness):
for project in opensafely_candidates:
    # 4a: Generate codelist imports from Phenotype Library canonical codes
    codelist_code = generate_codelist_import(
        codelists=project.phenotypes_codelists,
        format="opensafely"
    )
    
    # 4b: Generate study definition skeleton
    study_def = generate_study_definition(
        project_name=project.name,
        population="GDPPR + HES APC",
        exposures=project.phenotypes,
        outcomes=project.phenotypes,
        covariates=["age", "sex", "imd", "ethnicity"],
        index_date="2020-01-01"
    )
    
    # 4c: Generate action boilerplate (cohort extraction, matching, analysis)
    actions = generate_actions_boilerplate(
        study_definition=study_def,
        output_format="parquet",
        matching="propensity_score"
    )
    
    # 4d: Save to project-specific directory
    save_boilerplate(project.name, codelist_code, study_def, actions)
```

---

### Step 5: Synthesis & Deliverable
**AI Agent** combines all MCP outputs into a single report:

```markdown
# BHF DSC Support Analysis — HDRS Portfolio
*Generated: 2025-XX-XX | MCPs: HDRS, Gateway, PhenotypeLib, OpenSAFELY*

## 1. Project Prioritisation Matrix
| Project | BHF DSC Fit | Data Access Ready | Phenotype Ready | OpenSAFELY Ready | Priority |
|---------|-------------|-------------------|-----------------|------------------|----------|
| Cardinal | ⭐⭐⭐⭐⭐ | ✅ GDPPR, HES approved | ✅ In lib + OS port | ✅ Boilerplate generated | **HIGH** |
| Project B | ⭐⭐⭐ | ⚠️ CPRD access pending | ✅ In lib | ❌ No OS port | MEDIUM |
| Project C | ⭐⭐⭐⭐ | ✅ GDPPR approved | ❌ Missing from lib | N/A | MEDIUM |

## 2. Key People & Collaboration Map
- **Cardinal**: Dr. X (PI) — connects to BHF DSC CVD theme lead
- **Project B**: Prof. Y — respiratory theme, needs CPRD broker

## 3. Dataset Access Pathways
| Project | Gateway Dataset IDs | Data Use Precedent | Access Route |
|---------|---------------------|-------------------|--------------|
| Cardinal | 888 (GDPPR), 102 (HES APC) | 12 prior CVD studies | Standard DSA |
| Project B | 45 (CPRD Aurum), 102 | 3 respiratory studies | CPRD ISAC |

## 4. Phenotype Coverage & Gaps
| Phenotype | In Library | SNOMED Codelist | OpenSAFELY Port | Action |
|-----------|------------|-----------------|-----------------|--------|
| Heart failure | ✅ PHENO-001 | 47 codes | ✅ v2.1 | Ready |
| MI | ✅ PHENO-045 | 23 codes | ✅ v1.0 | Ready |
| T2D | ❌ | — | — | **Submit to library** |

## 5. OpenSAFELY Boilerplate Delivered
```
generated/
├── cardinal/
│   ├── codelists.py          # Auto-imported from Phenotype Library
│   ├── study_definition.py   # Population, variables, expectations
│   ├── actions/
│   │   ├── extract_cohort.yaml
│   │   ├── match_cohorts.yaml
│   │   └── analyse_outcomes.yaml
│   └── project.yaml          # OpenSAFELY project config
```

## 6. Recommended BHF DSC Interventions
1. **Cardinal** — Fund OpenSAFELY engineer for 3 months; broker GDPPR+HES linkage
2. **Project B** — Expedite CPRD ISAC; sponsor phenotype library entry for missing codes
3. **Project C** — Submit T2D phenotype to library; connect with SAIL for WLGP access
```

---

## 🎪 Live Demo Script (15 Minutes)

| Time | Action | MCP Calls | Audience Hook |
|------|--------|-----------|---------------|
| 0:00 | Ask the question | — | "One natural language question" |
| 1:30 | HDRS MCP returns 8 projects | `ask_hdrs_projects` | "No manual scraping" |
| 3:00 | GatewayMCP maps datasets for top 3 | `search_datasets`, `search_data_uses` | "Real approved precedents" |
| 5:00 | PhenotypeLib checks 12 phenotypes | `search_phenotypes`, `get_codelist` | "Canonical codes, not guesswork" |
| 7:00 | OpenSAFELY generates code for 2 projects | `generate_study_definition`, `generate_actions_boilerplate` | "Production-ready in seconds" |
| 10:00 | Synthesised report displayed | — | "Decision-ready output" |
| 12:00 | Drill-down: "Show me Cardinal's codelist lineage" | Cross-MCP trace | "Full provenance" |
| 15:00 | Q&A | — | — |

---

## 📊 Why This Beats Manual Work

| Dimension | Manual (Weeks) | Multi-MCP (Minutes) |
|-----------|----------------|---------------------|
| **Project discovery** | Search HDRS site, PDFs, spreadsheets | 1 RAG query over curated KB |
| **Dataset matching** | Browse Gateway UI, filter, cross-ref | 4 API calls → structured table |
| **Phenotype validation** | Search library, download CSVs, map codes | 1 search + canonical codelist |
| **OpenSAFELY starter** | Copy-paste from examples, adapt | Generated from *your* phenotypes |
| **Gap analysis** | Manual comparison across sources | Auto-diff across all 4 systems |
| **Provenance** | Lost in emails/notes | Every fact traced to MCP call |

---

## 🔧 Technical Requirements for Demo

| Component | Status | Notes |
|-----------|--------|-------|
| HDRS MCP | ✅ Deployed | Astra DB `hdrs3` + OpenRouter |
| GatewayMCP | ✅ Published | `hdruk-gateway-mcp` on GitHub |
| OpenSAFELYMCP | ✅ Published | `OpenSafelyMCP` with LangFlow backend |
| PhenotypeLibraryMCP | ✅ Published | `phenotypelibraryMCP` |
| Orchestration Agent | 🔧 Needed | LangGraph / LangChain / custom — routes to 4 MCPs |
| Eval Harness | 🔧 Needed | Golden questions for regression testing |

---

## 🚀 Next Steps for Programme Directors

1. **Approve orchestration layer build** — 2 sprints for LangGraph agent + MCP router
2. **Fund eval harness** — 20 golden questions covering all 4 MCP combos
3. **Pilot with 3 HDRS projects** — Cardinal + 2 others; measure time-to-first-analysis
4. **Integrate with BHF DSC workflow** — Connect to project intake / triage process

---

## 📎 MCP Tool Schemas Quick Reference

| MCP | Key Tools for This Workflow |
|-----|----------------------------|
| **HDRS** | `search_hdrs_projects(query)`, `ask_hdrs_projects(question)` |
| **Gateway** | `search_datasets`, `search_collections`, `search_data_uses`, `search_tools`, `search_publications`, `search_all` |
| **PhenotypeLib** | `search_phenotypes`, `get_phenotype`, `get_codelist`, `check_opensafely_port` |
| **OpenSAFELY** | `generate_codelist_import`, `generate_study_definition`, `generate_actions_boilerplate`, `validate_study_definition` |

---

**Ready to proceed?** I can:
1. Write the **LangGraph orchestration agent** that chains these 4 MCPs
2. Create a **golden eval set** for the 4-MCP workflow
3. Build a **Streamlit demo UI** for the pitch session
4. Draft the **project brief** for the orchestration layer build

Which would be most valuable next?
