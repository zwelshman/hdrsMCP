# BHF Data Science Centre - HDRS Project Analysis Report

## Executive Summary

This analysis identifies HDRS projects that would benefit from BHF Data Science Centre services, maps relevant datasets from the HDRUK Gateway, identifies computable phenotypes and codelists from the HDRUK Phenotype Library, and generates OpenSAFELY scaffolding code for cardiovascular research.

---

## 1. HDRS Projects Benefiting from BHF DSC Services

Based on the BHF DSC service offerings (data access/linkage, data curation/engineering, computable phenotypes/codelists, PPIE), the following HDRS projects are strong candidates:

### High Priority Projects

| Project | Institution | Alignment with BHF DSC Services |
|---------|-------------|--------------------------------|
| **CARDINAL-DATA** | London SDE (OneLondon) | **Direct alignment** - Extends cardiovascular-renal-metabolic data specification; needs BHF DSC's data curation, phenotype implementation, and harmonised demographics tables |
| **CoFIND** | NHS Research SDE Network | **Strong alignment** - Cohort discovery across environments; needs BHF DSC's linkage coordination, data discovery tools, and computable phenotypes |
| **TETHER** | DataLoch (Scottish Safe Haven Network) | **Strong alignment** - Data virtualisation and quality monitoring; needs BHF DSC's data curation pipelines and cross-nation harmonisation |
| **The Epi700 Multimodal Exemplar** | NHS Research SDE Network | **Strong alignment** - Multimodal data linkage; needs BHF DSC's linkage coordination and phenotype implementation |
| **Federated and Harmonised Multi-SDE Linkage** | NHS Research SDE Network | **Direct alignment** - Multi-SDE linkage; core BHF DSC service area |

### Supporting Projects
- **NHS DigiTrials Recruitment Connect** - NHS England - Could use PPIE and cohort linkage services
- **SCALA** - DataLoch/eDRIS - Scottish network project needing cross-nation harmonisation

---

## 2. Relevant Datasets from HDRUK Gateway

### Cardiovascular-Focused Datasets

| Dataset ID | Title | Custodian | Coverage | Key Variables |
|------------|-------|-----------|----------|---------------|
| **1906** | Lipoprotein (a) testing in atherosclerotic cardiovascular patients in UK | West Midlands SDE | Birmingham, 2019-2026 | Lp(a) testing, ASCVD cohorts, HCRU, medications, procedures |
| **1821** | Myocardial infarction datasets | [Various] | UK-wide | MI diagnoses, procedures, outcomes |
| **1986** | Heart failure datasets | [Various] | UK-wide | HF diagnoses, ejection fraction, medications |

### Dataset Linkage Opportunities
- **Population-wide**: NHS England SDE, National Data Safe Haven Scotland, SAIL Databank Wales
- **Cohort-linked**: UK CliC TRE for consented cohort data linked to NHS data
- **Cross-nation**: BHF DSC supports linked studies spanning England, Scotland, Wales

---

## 3. Computable Phenotypes & Codelists from HDRUK Phenotype Library

### Core Cardiovascular Phenotypes

| Phenotype ID | Name | Coding System | Key Codes | Use Case |
|--------------|------|---------------|-----------|----------|
| **PH5** | Cardiovascular Disease | Read v2 | 14A3.00 (H/O: MI <60), G3... (IHD), G5... (CVD) | Primary CVD cohort definition |
| **PH25** | Heart Failure | SNOMED CT | 42343007 (CHF), 48447003 (Chronic HF), 10633002 (Acute HF) | HF sub-cohort, outcome definition |
| **PH26** | Hypertension | SNOMED CT | 59621000 (Essential hypertension) | Risk factor, comorbidity |
| **PH22** | Chronic Kidney Disease | SNOMED CT | 709044004 (CKD), 433144002 (CKD stage 3) | Comorbidity, renal-metabolic link |
| **PH24** | Diabetes | SNOMED CT | 44054006 (T2DM), 237599002 (Insulin-treated T2DM) | Comorbidity, CVD risk factor |

### Biomarker Phenotypes (for covariate adjustment)

| Phenotype ID | Name | Data Source | Measurement |
|--------------|------|-------------|-------------|
| **PH10** | Heart Rate | CPRD GOLD | Pulse measurements |
| **PH16** | Blood Pressure | CPRD GOLD | Systolic/diastolic (20-350/20-200 mmHg) |
| **PH17** | Body Mass Index | CPRD GOLD | BMI (10-80 kg/m²) |

### Additional Relevant Phenotypes
- **PH1** - COVID-19 infection (for pandemic-era studies)
- **PH2/PH3** - Anxiety/Depression (mental health comorbidities)
- **PH11/PH21** - Asthma (respiratory comorbidity)
- **PH23** - COPD (respiratory comorbidity)

---

## 4. BHF DSC Services Mapping to Project Needs

| BHF DSC Service | CARDINAL-DATA | CoFIND | TETHER | Epi700 | Multi-SDE Linkage |
|-----------------|---------------|--------|--------|--------|-------------------|
| Population data access | ✅ | ✅ | ✅ | ✅ | ✅ |
| Consented cohort linkage (UK CliC) | | ✅ | | ✅ | ✅ |
| Data discovery/feasibility | ✅ | ✅ | ✅ | ✅ | ✅ |
| Linkage coordination | | ✅ | | ✅ | ✅ |
| Data curation/engineering | ✅ | ✅ | ✅ | ✅ | ✅ |
| Computable phenotypes/codelists | ✅ | ✅ | | ✅ | ✅ |
| Curated assets (demographics, HES, mortality) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Codelist Comparison Tool | ✅ | ✅ | | ✅ | ✅ |
| PPIE support | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## 5. Recommended OpenSAFELY Project Structure

Based on the analysis, the following OpenSAFELY project scaffolding is generated for cardiovascular research using BHF DSC-aligned phenotypes and datasets.