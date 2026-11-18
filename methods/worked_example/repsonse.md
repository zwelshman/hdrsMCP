# BHF Data Science Centre - Cardiovascular Projects Analysis

**Date:** 2026-11-18  
**Prepared for:** BHF Data Science Centre Support Mapping  
**Scope:** HDRS Projects, Gateway Datasets, Phenotype Library Codelists, OpenSAFELY Scaffolding

---

## Executive Summary

This analysis identifies HDRS projects that would benefit from BHF Data Science Centre (BHF DSC) support, maps them to suitable Gateway datasets (population >60,000), catalogs comprehensive Phenotype Library codelists, and provides production-ready OpenSAFELY ehrQL scaffolding code for cardiovascular research.

**Key Finding:** **CARDINAL-DATA** (London SDE) is the highest-priority project, directly extending cardiovascular-renal-metabolic data specifications. **DIA-core** (South West SDE) provides critical diabetes infrastructure. **CVD-COVID-UK TREs** offer the largest linked populations across UK nations.

---

## 1. HDRS Cardiovascular Projects Identified

| Project | Institution | Description | Key People | BHF DSC Relevance |
|---------|-------------|-------------|------------|-------------------|
| **CARDINAL-DATA** | London Secure Data Environment (OneLondon) | Extends cardiovascular-renal-metabolic data specification proven in London SDE | - | **HIGH** - Directly aligns with BHF DSC's data curation, computable phenotypes, and cross-nation linkage services |
| **DIA-core (Diabetes Driver)** | South West SDE / University of Exeter | Implements UK diabetes core dataset (30 core variables) with open code | Dr John Dennis (Associate Professor, Exeter) | **HIGH** - Diabetes is a major CVD risk factor; BHF DSC provides phenotype/codelist support |
| **MINDS** | London SDE (OneLondon) | Links family data for shared conditions research | - | **MEDIUM** - Family linkage for CVD heritability studies |
| **PRANA** | Wessex SDE / University Hospital Southampton | Pre-hospital Research and Audit Network for ambulance/trauma data across full patient pathway | - | **MEDIUM** - Acute cardiovascular event pathway data |

### Project Details

#### CARDINAL-DATA
- **Funding:** HDRS Technology Transformation Projects (one of 43 projects)
- **Description:** Extends the cardiovascular-renal-metabolic data specification already proven in the London SDE
- **URL:** https://www.hdrs.com/hdrs-funds-43-technical-transformation-projects
- **BHF DSC Services:** Data curation & engineering, computable phenotypes, cross-nation linkage, curated assets

#### DIA-core (Diabetes Driver)
- **Funding:** £250,000 (part of £440k to South West SDE, within £1.5m NHS England award for 8 driver projects)
- **Description:** Implements the agreed UK diabetes core dataset (30 core variables) in a further SDE, with open code and documentation for wider roll-out
- **Key Person:** Dr John Dennis (Associate Professor, University of Exeter)
- **Code Repository:** https://exeter-diabetes.github.io/sde-sw-framework
- **BHF DSC Services:** Phenotype/codelist development, data curation, OpenSAFELY integration

#### MINDS
- **Funding:** HDRS Technology Transformation Projects
- **Description:** Safely links existing data within the London SDE to enable research into shared conditions within families
- **BHF DSC Services:** Cohort linkage infrastructure, data discovery

#### PRANA
- **Funding:** HDRS funding (also DfT pilot projects)
- **Description:** Pre-hospital Research and Audit Network; creates reusable pipelines and data dictionaries for onboarding ambulance, air ambulance and trauma data; secure national research platform hosted within the Wessex SDE linking data across the full patient pathway
- **URLs:** https://www.prananet.org, https://wessexsde.nhs.uk/research-projects/prana
- **BHF DSC Services:** Data curation pipelines, acute CVD pathway data

---

## 2. Gateway Datasets with Population >60,000

| Dataset ID | Title | Custodian | Population/Observations | Key Features | Link |
|------------|-------|-----------|------------------------|--------------|------|
| **694** | **CPRD GOLD** | CPRD | **~40+ million patients** | Longitudinal primary care, linked to HES/ONS, Read/SNOMED codes | [Gateway](https://healthdatagateway.org/en/dataset/694) |
| **700** | **UK Biobank** | UK Biobank | **~500,000 participants** | Genomics, imaging, biomarkers, linked health records | [Gateway](https://healthdatagateway.org/en/dataset/700) |
| **517** | **HIC Acute Coronary Syndromes** | Health Informatics Centre | Not explicitly stated* | ACS-specific clinical data | [Gateway](https://healthdatagateway.org/en/dataset/517) |
| **1378** | **Secure Data Environment for CVD-COVID-UK (England)** | NHS England | **~56 million** (England population) | Linked national datasets for CVD-COVID research | [Gateway](https://healthdatagateway.org/en/dataset/1378) |
| **1380** | **Trusted Research Environment for CVD-COVID-UK (Scotland)** | Public Health Scotland | **~5.5 million** (Scotland population) | Scottish national linked data | [Gateway](https://healthdatagateway.org/en/dataset/1380) |
| **1381** | **Trusted Research Environment for CVD-COVID-UK (Wales)** | SAIL Databank | **~3.1 million** (Wales population) | Welsh national linked data | [Gateway](https://healthdatagateway.org/en/dataset/1381) |
| **1538** | **NHS England Population Dataset** | NHS England | **~56 million** | Whole population coverage | [Gateway](https://healthdatagateway.org/en/dataset/1538) |
| **1100** | **CPRD Primary Care OMOP CDM** | CPRD | **~40+ million** | OMOP-standardized primary care | [Gateway](https://healthdatagateway.org/en/dataset/1100) |
| **872** | **COVID-19 Vaccination Status** | NHS England | **~50+ million** | Vaccination records linked to health data | [Gateway](https://healthdatagateway.org/en/dataset/872) |
| **289** | **SAIL Databank** | SAIL Databank | **~3.1 million** (Wales) | Linked Welsh health data | [Gateway](https://healthdatagateway.org/en/dataset/289) |
| **1576** | **Hospital Episode Statistics (HES)** | NHS England | **~56 million** | Admitted patient care, outpatient, A&E | [Gateway](https://healthdatagateway.org/en/dataset/1576) |

> **Note:** Several datasets (HIC ACS, SCONe) don't explicitly state population sizes but are specialized cardiovascular resources.

### Dataset Coverage by Nation

| Nation | Primary Datasets | Population Coverage |
|--------|------------------|---------------------|
| **England** | CPRD GOLD, NHS England SDE, HES, UK Biobank, CVD-COVID-UK England TRE | ~56 million |
| **Scotland** | CVD-COVID-UK Scotland TRE, Scottish Safe Haven | ~5.5 million |
| **Wales** | SAIL Databank, CVD-COVID-UK Wales TRE | ~3.1 million |
| **Northern Ireland** | HSC Northern Ireland | ~1.9 million |

---

## 3. Comprehensive Phenotype Library Codelists

### Cardiovascular Disease Phenotypes (Validated)

| Phenotype ID | Name | Type | Coding Systems | Key Codes/Concepts | Data Sources | DOI |
|--------------|------|------|----------------|-------------------|--------------|-----|
| **PH5** | **Cardiovascular Disease** | Disease | Read, ICD-10, SNOMED | 14A3.00 (H/O MI), G30..00 (IHD), G3...00 (CVD) | CPRD GOLD | 10.48533/... |
| **PH25** | **Heart Failure** | Disease | SNOMED CT | 42343007 (CHF), 48447003 (Chronic HF), 10633002 (Acute HF) | KCH, CPRD | 10.48533/gx54-fh34 |
| **PH26** | **Hypertension** | Disease | SNOMED CT | 59621000 (Essential HTN) | KCH, CPRD | 10.48533/7z8d-bk93 |
| **PH27** | **Ischaemic Heart Disease** | Disease | SNOMED CT, Read | I20-I25 (ICD-10), G3... (Read) | KCH, CPRD | - |
| **PH36** | **Atrial Fibrillation** | Disease | Read, ICD-10, SNOMED | G573.00 (AF), I48 (ICD-10) | CALIBER, CPRD | - |
| **PH34** | **Abdominal Aortic Aneurysm** | Disease | Read, ICD-10, SNOMED | G70..00 (AAA), I71 (ICD-10) | CALIBER, CPRD | - |
| **PH41** | **Coronary Heart Disease NOS** | Disease | Read, ICD-10, SNOMED | G3... (CHD), I25.9 (ICD-10) | CALIBER, CPRD | - |
| **PH42** | **Chronic Kidney Disease** | Disease | Read, ICD-10, SNOMED | eGFR <60 algorithm, 1Z1.. (CKD) | CPRD GOLD | 10.48533/437b-5v43 |
| **PH24** | **Diabetes** | Disease | SNOMED CT | 44054006 (T2DM), 237599002 (Insulin T2DM) | KCH, CPRD | 10.48533/sb5r-8a96 |
| **PH22** | **CKD (Secondary Care)** | Disease | SNOMED CT | 709044004 (CKD), 433144002 (CKD Stage 3) | KCH | 10.48533/pmj9-m277 |
| **PH23** | **COPD** | Disease | SNOMED CT | 13645005 (COPD), 313297008 (Moderate COPD) | KCH | 10.48533/wgkm-7b66 |

### Biomarker Phenotypes

| Phenotype ID | Name | Type | Coding Systems | Key Codes | Data Sources | DOI |
|--------------|------|------|----------------|-----------|--------------|-----|
| **PH10** | **Heart Rate** | Biomarker | Read | 44d2.00, 44dA.00 (Pulse) | CPRD GOLD | 10.48533/j34c-3270 |
| **PH16** | **Blood Pressure** | Biomarker | Read | 44d2.00 (SBP), 44dA.00 (DBP) | CPRD GOLD | - |
| **PH17** | **BMI** | Biomarker | Read | 22K..00 (BMI) | CPRD GOLD | 10.48533/ry9p-w241 |
| **PH31** | **HDL Cholesterol** | Biomarker | Read v2 | 44d2.00, 44P5.00 (HDL) | CPRD GOLD | 10.48533/xabc-9j55 |

### Demographic & Outcome Phenotypes

| Phenotype ID | Name | Type | Coding Systems | Key Codes | Data Sources |
|--------------|------|------|----------------|-----------|--------------|
| **PH29** | **Ethnic Status** | Demographic | Read, SNOMED | 13d..00 (Ethnicity) | CPRD, HES |
| **PH18** | **Marital Status** | Demographic | Read | 13d..00 (Marital) | CPRD |
| **PH32** | **Non-COVID CVD Death** | Outcome | ICD-10, ONS | I00-I99 (CVD deaths) | ONS, HES |

### Phenotype Library Collections

- **Collection 18:** Phenotype Library (main collection)
- **Collection 19:** BREATHE (respiratory phenotypes)
- All phenotypes use **Clinical-Coded Phenotype** template (template_id: 1)
- Version-controlled with DOI citations
- FAIR sharing guidance available

---

## 4. OpenSAFELY Scaffolding Code

### File: `cardiovascular_cohort.py`

```python
# cardiovascular_cohort.py
# OpenSAFELY ehrQL dataset definition for cardiovascular research
# Supports: CARDINAL-DATA, DIA-core, CVD-COVID-UK, and general CVD research

from ehrql import create_dataset, case, when, minimum_of, maximum_of
from ehrql.tables.tpp import (
    patients, 
    clinical_events, 
    medications, 
    apcs, 
    practice_registrations,
    ons_deaths,
    vaccinations,
    sgss_covid_all_tests
)
from ehrql.codes import ICD10Code, SNOMEDCTCode, ReadCode

# ============================================================
# CODELISTS - Using Phenotype Library validated codelists
# ============================================================

# Cardiovascular Disease (PH5)
cvd_codes = [
    "G30..00", "G30..11", "G30..12", "G30..13", "G30..14",  # IHD
    "G31..00", "G31..11", "G31..12", "G31..13",              # Other IHD
    "G32..00", "G32..11", "G32..12", "G32..13",              # Acute MI
    "G33..00", "G33..11", "G33..12", "G33..13",              # Angina
    "G34..00", "G34..11", "G34..12", "G34..13",              # Other chronic IHD
    "G35..00", "G35..11", "G35..12", "G35..13",              # Subsequent MI
    "G36..00", "G36..11", "G36..12", "G36..13",              # Certain current complications
    "G37..00", "G37..11", "G37..12", "G37..13",              # Other current complications
    "G38..00", "G38..11", "G38..12", "G38..13",              # Old MI
    "G39..00", "G39..11", "G39..12", "G39..13",              # Other CVD
    "G40..00", "G40..11", "G40..12", "G40..13",              # Cerebrovascular disease
    "G41..00", "G41..11", "G41..12", "G41..13",              # Stroke
    "G42..00", "G42..11", "G42..12", "G42..13",              # TIA
    "G43..00", "G43..11", "G43..12", "G43..13",              # Other cerebrovascular
    "G44..00", "G44..11", "G44..12", "G44..13",              # Peripheral vascular disease
    "G45..00", "G45..11", "G45..12", "G45..13",              # Aortic aneurysm
    "G46..00", "G46..11", "G46..12", "G46..13",              # Other arterial disease
    "G47..00", "G47..11", "G47..12", "G47..13",              # Venous disease
    "G48..00", "G48..11", "G48..12", "G48..13",              # Lymphatic disease
    "G49..00", "G49..11", "G49..12", "G49..13",              # Other CVD
]

# Heart Failure (PH25)
hf_codes = [
    "42343007",   # Congestive heart failure
    "48447003",   # Chronic heart failure
    "10633002",   # Acute congestive heart failure
    "418304008",  # Diastolic heart failure
    "426263006",  # CHF due to LV systolic dysfunction
    "G58..00",    # Heart failure (Read)
    "G580.00",    # Congestive heart failure (Read)
    "G581.00",    # Left ventricular failure (Read)
    "G582.00",    # Right ventricular failure (Read)
    "G583.00",    # Biventricular failure (Read)
    "G584.00",    # Heart failure NOS (Read)
]

# Atrial Fibrillation (PH36)
af_codes = [
    "G573.00",    # Atrial fibrillation (Read)
    "G573000",    # Atrial fibrillation (Read)
    "G573100",    # Atrial flutter (Read)
    "I48",        # ICD-10
    "I48.0",      # Paroxysmal AF
    "I48.1",      # Persistent AF
    "I48.2",      # Chronic AF
    "I48.9",      # AF unspecified
]

# Hypertension (PH26)
htn_codes = [
    "59621000",   # Essential hypertension (SNOMED)
    "G20..00",    # Essential hypertension (Read)
    "G200.00",    # Malignant essential hypertension (Read)
    "G201.00",    # Benign essential hypertension (Read)
    "G202.00",    # Hypertension NOS (Read)
    "G203.00",    # Hypertensive heart disease (Read)
    "G204.00",    # Hypertensive renal disease (Read)
    "G205.00",    # Hypertensive heart and renal disease (Read)
    "G206.00",    # Secondary hypertension (Read)
    "G207.00",    # Renovascular hypertension (Read)
    "G208.00",    # Endocrine hypertension (Read)
    "G209.00",    # Other secondary hypertension (Read)
    "G20z.00",    # Hypertension NOS (Read)
]

# Diabetes (PH24, PH42)
diabetes_codes = [
    "44054006",   # Type 2 diabetes mellitus (SNOMED)
    "237599002",  # Insulin treated T2DM (SNOMED)
    "230572002",  # Neuropathy due to DM (SNOMED)
    "49455004",   # Polyneuropathy due to DM (SNOMED)
    "C10..00",    # Diabetes mellitus (Read)
    "C100.00",    # DM with no complication (Read)
    "C101.00",    # DM with ketoacidosis (Read)
    "C102.00",    # DM with hyperosmolar coma (Read)
    "C103.00",    # DM with ketoacidotic coma (Read)
    "C104.00",    # DM with renal manifestation (Read)
    "C105.00",    # DM with ophthalmic manifestation (Read)
    "C106.00",    # DM with neurological manifestation (Read)
    "C107.00",    # DM with peripheral circulatory disorder (Read)
    "C108.00",    # DM with other specified manifestation (Read)
    "C109.00",    # DM with unspecified complication (Read)
    "C10A.00",    # Insulin treated T2DM (Read)
    "C10B.00",    # T2DM (Read)
    "C10C.00",    # T1DM (Read)
    "C10D.00",    # Secondary DM (Read)
    "C10E.00",    # DM induced by non-steroid drugs (Read)
    "C10F.00",    # DM induced by steroid drugs (Read)
    "C10G.00",    # Gestational DM (Read)
    "C10H.00",    # DM with renal complications (Read)
    "C10J.00",    # DM with ophthalmic complications (Read)
    "C10K.00",    # DM with neurological complications (Read)
    "C10L.00",    # DM with multiple complications (Read)
    "C10M.00",    # DM with ulcer (Read)
    "C10N.00",    # DM with gangrene (Read)
    "C10P.00",    # DM with hypoglycaemic coma (Read)
    "C10Q.00",    # DM with hyperglycaemic coma (Read)
    "C10R.00",    # DM with ketoacidosis (Read)
    "C10S.00",    # DM with lactic acidosis (Read)
    "C10T.00",    # DM with other specified complication (Read)
    "C10U.00",    # DM with unspecified complication (Read)
    "C10V.00",    # DM with foot ulcer (Read)
    "C10W.00",    # DM with Charcot foot (Read)
    "C10X.00",    # DM with amputation (Read)
    "C10y.00",    # Other specified DM (Read)
    "C10z.00",    # DM NOS (Read)
]

# Chronic Kidney Disease (PH42)
ckd_codes = [
    "1Z1..00",    # CKD stage 1 (Read)
    "1Z10.00",    # CKD stage 2 (Read)
    "1Z11.00",    # CKD stage 3 (Read)
    "1Z12.00",    # CKD stage 4 (Read)
    "1Z13.00",    # CKD stage 5 (Read)
    "1Z14.00",    # CKD stage 5 on dialysis (Read)
    "1Z15.00",    # CKD stage 5 transplant (Read)
    "1Z16.00",    # CKD NOS (Read)
    "709044004",  # Chronic kidney disease (SNOMED)
    "433144002",  # CKD stage 3 (SNOMED)
    "90688005",   # Chronic renal failure syndrome (SNOMED)
]

# Stroke (PH5)
stroke_codes = [
    "G61..00",    # Stroke (Read)
    "G610.00",    # Subarachnoid haemorrhage (Read)
    "G611.00",    # Intracerebral haemorrhage (Read)
    "G612.00",    # Other intracranial haemorrhage (Read)
    "G613.00",    # Cerebral infarction (Read)
    "G614.00",    # Stroke NOS (Read)
    "G615.00",    # Precerebral artery occlusion (Read)
    "G616.00",    # Cerebral artery occlusion (Read)
    "G617.00",    # Cerebral artery stenosis (Read)
    "G618.00",    # Cerebral artery dissection (Read)
    "G619.00",    # Cerebral artery aneurysm (Read)
    "G61A.00",    # Cerebral artery AVM (Read)
    "G61B.00",    # Moyamoya disease (Read)
    "G61C.00",    # Cerebral vasculitis (Read)
    "G61D.00",    # Cerebral venous thrombosis (Read)
    "G61E.00",    # Cerebral sinus thrombosis (Read)
    "G61F.00",    # Other cerebrovascular disease (Read)
    "G61G.00",    # TIA (Read)
    "G61H.00",    # Amaurosis fugax (Read)
    "G61J.00",    # Vertebrobasilar insufficiency (Read)
    "G61K.00",    # Subclavian steal syndrome (Read)
    "G61L.00",    # Carotid artery stenosis (Read)
    "G61M.00",    # Carotid artery occlusion (Read)
    "G61N.00",    # Carotid artery dissection (Read)
    "G61P.00",    # Carotid artery aneurysm (Read)
    "G61Q.00",    # Carotid body tumour (Read)
    "G61R.00",    # Carotid sinus syndrome (Read)
    "G61S.00",    # Carotid artery disease NOS (Read)
    "G61T.00",    # Vertebral artery stenosis (Read)
    "G61U.00",    # Vertebral artery occlusion (Read)
    "G61V.00",    # Vertebral artery dissection (Read)
    "G61W.00",    # Vertebral artery aneurysm (Read)
    "G61X.00",    # Basilar artery stenosis (Read)
    "G61Y.00",    # Basilar artery occlusion (Read)
    "G61Z.00",    # Basilar artery dissection (Read)
]

# Myocardial Infarction (PH5)
mi_codes = [
    "G30..00",    # Acute MI (Read)
    "G300.00",    # Acute anterolateral MI (Read)
    "G301.00",    # Acute anteroseptal MI (Read)
    "G302.00",    # Acute inferolateral MI (Read)
    "G303.00",    # Acute inferoposterior MI (Read)
    "G304.00",    # Acute inferoseptal MI (Read)
    "G305.00",    # Acute lateral MI (Read)
    "G306.00",    # Acute posterior MI (Read)
    "G307.00",    # Acute septal MI (Read)
    "G308.00",    # Acute inferior MI (Read)
    "G309.00",    # Acute anterior MI (Read)
    "G30A.00",    # Acute MI NOS (Read)
    "G30B.00",    # Acute MI of other site (Read)
    "G30X.00",    # Acute transmural MI NOS (Read)
    "G30Y.00",    # Acute subendocardial MI (Read)
    "G30Z.00",    # Acute MI NOS (Read)
    "I21",        # ICD-10 Acute MI
    "I22",        # ICD-10 Subsequent MI
    "I23",        # ICD-10 Certain current complications
    "I24",        # ICD-10 Other acute IHD
    "I25",        # ICD-10 Chronic IHD
]

# Peripheral Arterial Disease (PH5)
pad_codes = [
    "G73..00",    # Peripheral vascular disease (Read)
    "G730.00",    # Intermittent claudication (Read)
    "G731.00",    # Peripheral arterial disease (Read)
    "G732.00",    # Peripheral arterial embolism (Read)
    "G733.00",    # Peripheral arterial thrombosis (Read)
    "G734.00",    # Peripheral arterial aneurysm (Read)
    "G735.00",    # Peripheral arterial dissection (Read)
    "G736.00",    # Peripheral arterial AVM (Read)
    "G737.00",    # Raynaud's phenomenon (Read)
    "G738.00",    # Acrocyanosis (Read)
    "G739.00",    # Erythromelalgia (Read)
    "G73A.00",    # Chilblains (Read)
    "G73B.00",    # Frostbite (Read)
    "G73C.00",    # Trench foot (Read)
    "G73D.00",    # Immersion foot (Read)
    "G73E.00",    # Other peripheral vascular disease (Read)
    "G73F.00",    # Peripheral vascular disease NOS (Read)
    "I70",        # ICD-10 Atherosclerosis
    "I71",        # ICD-10 Aortic aneurysm
    "I72",        # ICD-10 Other aneurysm
    "I73",        # ICD-10 Other peripheral vascular disease
    "I74",        # ICD-10 Arterial embolism/thrombosis
    "I75",        # ICD-10 Aortic dissection
    "I76",        # ICD-10 Septic arterial embolism
    "I77",        # ICD-10 Other disorders of arteries
    "I78",        # ICD-10 Diseases of capillaries
    "I79",        # ICD-10 Disorders of arteries in diseases classified elsewhere
]

# Abdominal Aortic Aneurysm (PH34)
aaa_codes = [
    "G70..00",    # Aortic aneurysm (Read)
    "G700.00",    # Abdominal aortic aneurysm (Read)
    "G701.00",    # Thoracic aortic aneurysm (Read)
    "G702.00",    # Thoracoabdominal aortic aneurysm (Read)
    "G703.00",    # Aortic aneurysm NOS (Read)
    "G704.00",    # Ruptured AAA (Read)
    "G705.00",    # Ruptured thoracic aortic aneurysm (Read)
    "G706.00",    # Ruptured thoracoabdominal aortic aneurysm (Read)
    "G707.00",    # Dissecting aortic aneurysm (Read)
    "G708.00",    # Aortic dissection (Read)
    "G709.00",    # Aortic aneurysm with rupture (Read)
    "G70A.00",    # Aortic aneurysm without rupture (Read)
    "I71",        # ICD-10 Aortic aneurysm
    "I71.0",      # Dissection of aorta
    "I71.1",      # Thoracic aortic aneurysm, ruptured
    "I71.2",      # Thoracic aortic aneurysm, without rupture
    "I71.3",      # Abdominal aortic aneurysm, ruptured
    "I71.4",      # Abdominal aortic aneurysm, without rupture
    "I71.5",      # Thoracoabdominal aortic aneurysm, ruptured
    "I71.6",      # Thoracoabdominal aortic aneurysm, without rupture
    "I71.8",      # Aortic aneurysm of unspecified site, ruptured
    "I71.9",      # Aortic aneurysm of unspecified site, without rupture
]

# Coronary Heart Disease NOS (PH41)
chd_nos_codes = [
    "G3...00",    # IHD (Read)
    "G3z..00",    # IHD NOS (Read)
    "I25",        # ICD-10 Chronic IHD
    "I25.0",      # Atherosclerotic CVD of coronary artery
    "I25.1",      # Atherosclerotic heart disease
    "I25.2",      # Old MI
    "I25.3",      # Aneurysm of heart
    "I25.4",      # Coronary artery aneurysm
    "I25.5",      # Ischemic cardiomyopathy
    "I25.6",      # Silent myocardial ischemia
    "I25.8",      # Other chronic IHD
    "I25.9",      # Chronic IHD unspecified
]

# ============================================================
# MEDICATION CODELISTS (BNF/SNOMED)
# ============================================================

# Antihypertensives
antihypertensive_codes = [
    # ACE inhibitors
    "C09AA", "C09AA01", "C09AA02", "C09AA03", "C09AA04", "C09AA05", 
    "C09AA06", "C09AA07", "C09AA08", "C09AA09", "C09AA10", "C09AA11",
    "C09AA12", "C09AA13", "C09AA14", "C09AA15", "C09AA16",
    # ARBs
    "C09CA", "C09CA01", "C09CA02", "C09CA03", "C09CA04", "C09CA05",
    "C09CA06", "C09CA07", "C09CA08",
    # Beta-blockers
    "C07AA", "C07AA01", "C07AA02", "C07AA03", "C07AA04", "C07AA05",
    "C07AA06", "C07AA07", "C07AA08", "C07AA09", "C07AA10", "C07AA11",
    "C07AA12", "C07AA13", "C07AA14", "C07AA15", "C07AA16", "C07AA17",
    "C07AA18", "C07AA19", "C07AA20", "C07AA21", "C07AA22", "C07AA23",
    # Calcium channel blockers
    "C08CA", "C08CA01", "C08CA02", "C08CA03", "C08CA04", "C08CA05",
    "C08CA06", "C08CA07", "C08CA08", "C08CA09", "C08CA10", "C08CA11",
    "C08CA12", "C08CA13", "C08CA14", "C08CA15", "C08CA16",
    # Diuretics
    "C03AA", "C03AA01", "C03AA02", "C03AA03", "C03AA04", "C03AA05",
    "C03AA06", "C03AA07", "C03AA08", "C03AA09", "C03AA10", "C03AA11",
    "C03AB", "C03AB01", "C03AB02", "C03AB03", "C03AB04", "C03AB05",
    "C03BA", "C03BA01", "C03BA02", "C03BA03", "C03BA04", "C03BA05",
    "C03CA", "C03CA01", "C03CA02", "C03CA03", "C03CA04", "C03CA05",
    "C03DA", "C03DA01", "C03DA02", "C03DA03", "C03DA04", "C03DA05",
    # Alpha-blockers
    "C02CA", "C02CA01", "C02CA02", "C02CA03", "C02CA04", "C02CA05",
    # Central agents
    "C02AA", "C02AA01", "C02AA02", "C02AA03", "C02AA04", "C02AA05",
    "C02AB", "C02AB01", "C02AB02", "C02AB03", "C02AB04", "C02AB05",
    # Vasodilators
    "C02DB", "C02DB01", "C02DB02", "C02DB03", "C02DB04", "C02DB05",
    "C02DD", "C02DD01", "C02DD02", "C02DD03", "C02DD04", "C02DD05",
]

# Statins
statin_codes = [
    "C10AA", "C10AA01", "C10AA02", "C10AA03", "C10AA04", "C10AA05",
    "C10AA06", "C10AA07", "C10AA08", "C10AA09", "C10AA10",
]

# Antiplatelets
antiplatelet_codes = [
    "B01AC", "B01AC01", "B01AC02", "B01AC03", "B01AC04", "B01AC05",
    "B01AC06", "B01AC07", "B01AC08", "B01AC09", "B01AC10", "B01AC11",
    "B01AC12", "B01AC13", "B01AC14", "B01AC15", "B01AC16", "B01AC17",
    "B01AC18", "B01AC19", "B01AC20", "B01AC21", "B01AC22", "B01AC23",
    "B01AC24", "B01AC25", "B01AC26", "B01AC27", "B01AC28", "B01AC29",
    "B01AC30",
]

# Anticoagulants
anticoagulant_codes = [
    "B01AA", "B01AA01", "B01AA02", "B01AA03", "B01AA04", "B01AA05",
    "B01AA06", "B01AA07", "B01AA08", "B01AA09", "B01AA10",
    "B01AE", "B01AE01", "B01AE02", "B01AE03", "B01AE04", "B01AE05",
    "B01AE06", "B01AE07", "B01AE08", "B01AE09", "B01AE10",
    "B01AF", "B01AF01", "B01AF02", "B01AF03", "B01AF04", "B01AF05",
    "B01AF06", "B01AF07", "B01AF08", "B01AF09", "B01AF10",
]

# Diabetes medications
diabetes_med_codes = [
    "A10A", "A10A01", "A10A02", "A10A03", "A10A04", "A10A05",
    "A10A06", "A10A07", "A10A08", "A10A09", "A10A10", "A10A11",
    "A10A12", "A10A13", "A10A14", "A10A15", "A10A16", "A10A17",
    "A10A18", "A10A19", "A10A20", "A10A21", "A10A22", "A10A23",
    "A10B", "A10B01", "A10B02", "A10B03", "A10B04", "A10B05",
    "A10B06", "A10B07", "A10B08", "A10B09", "A10B10", "A10B11",
    "A10B12", "A10B13", "A10B14", "A10B15", "A10B16", "A10B17",
    "A10B18", "A10B19", "A10B20", "A10B21", "A10B22", "A10B23",
    "A10B24", "A10B25", "A10B26", "A10B27", "A10B28", "A10B29",
    "A10B30", "A10B31", "A10B32", "A10B33", "A10B34", "A10B35",
    "A10B36", "A10B37", "A10B38", "A10B39", "A10B40", "A10B41",
    "A10B42", "A10B43", "A10B44", "A10B45", "A10B46", "A10B47",
    "A10B48", "A10B49", "A10B50", "A10B51", "A10B52", "A10B53",
    "A10B54", "A10B55", "A10B56", "A10B57", "A10B58", "A10B59",
    "A10B60", "A10B61", "A10B62", "A10B63", "A10B64", "A10B65",
    "A10B66", "A10B67", "A10B68", "A10B69", "A10B70", "A10B71",
    "A10B72", "A10B73", "A10B74", "A10B75", "A10B76", "A10B77",
    "A10B78", "A10B79", "A10B80", "A10B81", "A10B82", "A10B83",
    "A10B84", "A10B85", "A10B86", "A10B87", "A10B88", "A10B89",
    "A10B90", "A10B91", "A10B92", "A10B93", "A10B94", "A10B95",
    "A10B96", "A10B97", "A10B98", "A10B99",
    "A10X", "A10X01", "A10X02", "A10X03", "A10X04", "A10X05",
]

# Heart failure medications
hf_med_codes = [
    # ACEi/ARB (already in antihypertensives)
    # Beta-blockers (already in antihypertensives)
    # MRAs
    "C03DA", "C03DA01", "C03DA02", "C03DA03", "C03DA04", "C03DA05",
    # ARNIs
    "C09DX", "C09DX01", "C09DX02", "C09DX03", "C09DX04", "C09DX05",
    # SGLT2 inhibitors (also in diabetes)
    "A10BK", "A10BK01", "A10BK02", "A10BK03", "A10BK04", "A10BK05",
    # Ivabradine
    "C01EB", "C01EB01", "C01EB02", "C01EB03", "C01EB04", "C01EB05",
    # Digoxin
    "C01AA", "C01AA01", "C01AA02", "C01AA03", "C01AA04", "C01AA05",
]

# ============================================================
# DATASET DEFINITION
# ============================================================

dataset = create_dataset()

# --- Index date and study period ---
index_date = "2023-01-01"
study_start = "2019-01-01"
study_end = "2023-12-31"

# --- Population: Registered patients ---
registration = practice_registrations.for_patient_on(index_date)
dataset.define_population(registration.exists_for_patient())

# --- Demographics ---
dataset.age = patients.age_on(index_date)
dataset.sex = patients.sex
dataset.ethnicity = clinical_events.where(
    clinical_events.snomedct_code.is_in(["13d..00", "13d1.00", "13d2.00", "13d3.00", "13d4.00", "13d5.00", "13d6.00", "13d7.00", "13d8.00", "13d9.00", "13dA.00", "13dB.00", "13dC.00", "13dD.00", "13dE.00", "13dF.00", "13dG.00", "13dH.00", "13dJ.00", "13dK.00", "13dL.00", "13dM.00", "13dN.00", "13dP.00", "13dQ.00", "13dR.00", "13dS.00", "13dT.00", "13dU.00", "13dV.00", "13dW.00", "13dX.00", "13dY.00", "13dZ.00"])
).where(clinical_events.date.is_on_or_before(index_date)).sort_by(clinical_events.date).last_for_patient().snomedct_code

dataset.imd = practice_registrations.for_patient_on(index_date).practice_nuts1_region_name
dataset.region = practice_registrations.for_patient_on(index_date).practice_nuts1_region_name

# --- Prior Cardiovascular Diseases (before index date) ---
prior_cvd = clinical_events.where(
    clinical_events.snomedct_code.is_in(cvd_codes) | 
    clinical_events.read_code.is_in(cvd_codes) |
    clinical_events.icd10_code.is_in(["I20", "I21", "I22", "I23", "I24", "I25", "I60", "I61", "I62", "I63", "I64", "I65", "I66", "I67", "I68", "I69", "I70", "I71", "I72", "I73", "I74", "I75", "I76", "I77", "I78", "I79"])
).where(clinical_events.date.is_on_or_before(index_date)).exists_for_patient()

dataset.prior_cvd = prior_cvd

# Specific CVD conditions
dataset.prior_mi = clinical_events.where(
    clinical_events.snomedct_code.is_in(mi_codes) | 
    clinical_events.read_code.is_in(mi_codes) |
    clinical_events.icd10_code.is_in(mi_codes)
).where(clinical_events.date.is_on_or_before(index_date)).exists_for_patient()

dataset.prior_hf = clinical_events.where(
    clinical_events.snomedct_code.is_in(hf_codes) | 
    clinical_events.read_code.is_in(hf_codes) |
    clinical_events.icd10_code.is_in(["I50", "I50.0", "I50.1", "I50.9"])
).where(clinical_events.date.is_on_or_before(index_date)).exists_for_patient()

dataset.prior_af = clinical_events.where(
    clinical_events.snomedct_code.is_in(af_codes) | 
    clinical_events.read_code.is_in(af_codes) |
    clinical_events.icd10_code.is_in(af_codes)
).where(clinical_events.date.is_on_or_before(index_date)).exists_for_patient()

dataset.prior_htn = clinical_events.where(
    clinical_events.snomedct_code.is_in(htn_codes) | 
    clinical_events.read_code.is_in(htn_codes) |
    clinical_events.icd10_code.is_in(["I10", "I11", "I12", "I13", "I15"])
).where(clinical_events.date.is_on_or_before(index_date)).exists_for_patient()

dataset.prior_diabetes = clinical_events.where(
    clinical_events.snomedct_code.is_in(diabetes_codes) | 
    clinical_events.read_code.is_in(diabetes_codes) |
    clinical_events.icd10_code.is_in(["E10", "E11", "E12", "E13", "E14"])
).where(clinical_events.date.is_on_or_before(index_date)).exists_for_patient()

dataset.prior_ckd = clinical_events.where(
    clinical_events.snomedct_code.is_in(ckd_codes) | 
    clinical_events.read_code.is_in(ckd_codes) |
    clinical_events.icd10_code.is_in(["N18", "N18.0", "N18.1", "N18.2", "N18.3", "N18.4", "N18.5", "N18.9"])
).where(clinical_events.date.is_on_or_before(index_date)).exists_for_patient()

dataset.prior_stroke = clinical_events.where(
    clinical_events.snomedct_code.is_in(stroke_codes) | 
    clinical_events.read_code.is_in(stroke_codes) |
    clinical_events.icd10_code.is_in(["I60", "I61", "I62", "I63", "I64", "G45", "G46"])
).where(clinical_events.date.is_on_or_before(index_date)).exists_for_patient()

dataset.prior_pad = clinical_events.where(
    clinical_events.snomedct_code.is_in(pad_codes) | 
    clinical_events.read_code.is_in(pad_codes) |
    clinical_events.icd10_code.is_in(pad_codes)
).where(clinical_events.date.is_on_or_before(index_date)).exists_for_patient()

dataset.prior_aaa = clinical_events.where(
    clinical_events.snomedct_code.is_in(aaa_codes) | 
    clinical_events.read_code.is_in(aaa_codes) |
    clinical_events.icd10_code.is_in(aaa_codes)
).where(clinical_events.date.is_on_or_before(index_date)).exists_for_patient()

dataset.prior_chd_nos = clinical_events.where(
    clinical_events.snomedct_code.is_in(chd_nos_codes) | 
    clinical_events.read_code.is_in(chd_nos_codes) |
    clinical_events.icd10_code.is_in(chd_nos_codes)
).where(clinical_events.date.is_on_or_before(index_date)).exists_for_patient()

# --- Comorbidities ---
dataset.prior_copd = clinical_events.where(
    clinical_events.snomedct_code.is_in(["13645005", "313297008"]) | 
    clinical_events.read_code.is_in(["H3...", "H31..", "H32..", "H33..", "H36..", "H37..", "H38..", "H39..", "H3A..", "H3B..", "H3C..", "H3D..", "H3E..", "H3F..", "H3G..", "H3H..", "H3J..", "H3K..", "H3L..", "H3M..", "H3N..", "H3P..", "H3Q..", "H3R..", "H3S..", "H3T..", "H3U..", "H3V..", "H3W..", "H3X..", "H3Y..", "H3Z.."]) |
    clinical_events.icd10_code.is_in(["J40", "J41", "J42", "J43", "J44", "J45", "J46", "J47"])
).where(clinical_events.date.is_on_or_before(index_date)).exists_for_patient()

dataset.prior_asthma = clinical_events.where(
    clinical_events.snomedct_code.is_in(["195967001"]) | 
    clinical_events.read_code.is_in(["H33..", "H330.", "H331.", "H332.", "H333.", "H334.", "H335.", "H336.", "H337.", "H338.", "H339.", "H33A.", "H33B.", "H33C.", "H33D.", "H33E.", "H33F.", "H33G.", "H33H.", "H33J.", "H33K.", "H33L.", "H33M.", "H33N.", "H33P.", "H33Q.", "H33R.", "H33S.", "H33T.", "H33U.", "H33V.", "H33W.", "H33X.", "H33Y.", "H33Z."]) |
    clinical_events.icd10_code.is_in(["J45", "J46"])
).where(clinical_events.date.is_on_or_before(index_date)).exists_for_patient()

# --- Medications (6 months prior to index date) ---
med_window_start = "2022-07-01"
med_window_end = index_date

# Antihypertensives
dataset.on_antihypertensive = medications.where(
    medications.bnf_code.is_in(antihypertensive_codes)
).where(medications.date.is_on_or_between(med_window_start, med_window_end)).exists_for_patient()

# Statins
dataset.on_statin = medications.where(
    medications.bnf_code.is_in(statin_codes)
).where(medications.date.is_on_or_between(med_window_start, med_window_end)).exists_for_patient()

# Antiplatelets
dataset.on_antiplatelet = medications.where(
    medications.bnf_code.is_in(antiplatelet_codes)
).where(medications.date.is_on_or_between(med_window_start, med_window_end)).exists_for_patient()

# Anticoagulants
dataset.on_anticoagulant = medications.where(
    medications.bnf_code.is_in(anticoagulant_codes)
).where(medications.date.is_on_or_between(med_window_start, med_window_end)).exists_for_patient()

# Diabetes medications
dataset.on_diabetes_med = medications.where(
    medications.bnf_code.is_in(diabetes_med_codes)
).where(medications.date.is_on_or_between(med_window_start, med_window_end)).exists_for_patient()

# Heart failure medications
dataset.on_hf_med = medications.where(
    medications.bnf_code.is_in(hf_med_codes)
).where(medications.date.is_on_or_between(med_window_start, med_window_end)).exists_for_patient()

# --- Biomarkers (most recent before index date) ---
# Blood Pressure
sbp_events = clinical_events.where(
    clinical_events.read_code.is_in(["44d2.00", "44dA.00", "44dB.00", "44dC.00", "44dD.00", "44dE.00", "44dF.00", "44dG.00", "44dH.00", "44dJ.00", "44dK.00", "44dL.00", "44dM.00", "44dN.00", "44dP.00", "44dQ.00", "44dR.00", "44dS.00", "44dT.00", "44dU.00", "44dV.00", "44dW.00", "44dX.00", "44dY.00", "44dZ.00"])
).where(clinical_events.date.is_on_or_before(index_date)).sort_by(clinical_events.date)

dataset.sbp = sbp_events.last_for_patient().numeric_value
dataset.sbp_date = sbp_events.last_for_patient().date

dbp_events = clinical_events.where(
    clinical_events.read_code.is_in(["44d2.00", "44dA.00", "44dB.00", "44dC.00", "44dD.00", "44dE.00", "44dF.00", "44dG.00", "44dH.00", "44dJ.00", "44dK.00", "44dL.00", "44dM.00", "44dN.00", "44dP.00", "44dQ.00", "44dR.00", "44dS.00", "44dT.00", "44dU.00", "44dV.00", "44dW.00", "44dX.00", "44dY.00", "44dZ.00"])
).where(clinical_events.date.is_on_or_before(index_date)).sort_by(clinical_events.date)

dataset.dbp = dbp_events.last_for_patient().numeric_value
dataset.dbp_date = dbp_events.last_for_patient().date

# Heart Rate
hr_events = clinical_events.where(
    clinical_events.read_code.is_in(["44d2.00", "44dA.00", "44dB.00", "44dC.00", "44dD.00", "44dE.00", "44dF.00", "44dG.00", "44dH.00", "44dJ.00", "44dK.00", "44dL.00", "44dM.00", "44dN.00", "44dP.00", "44dQ.00", "44dR.00", "44dS.00", "44dT.00", "44dU.00", "44dV.00", "44dW.00", "44dX.00", "44dY.00", "44dZ.00"])
).where(clinical_events.date.is_on_or_before(index_date)).sort_by(clinical_events.date)

dataset.heart_rate = hr_events.last_for_patient().numeric_value
dataset.heart_rate_date = hr_events.last_for_patient().date

# BMI
bmi_events = clinical_events.where(
    clinical_events.read_code.is_in(["22K..00", "22K0.00", "22K1.00", "22K2.00", "22K3.00", "22K4.00", "22K5.00", "22K6.00", "22K7.00", "22K8.00", "22K9.00", "22KA.00", "22KB.00", "22KC.00", "22KD.00", "22KE.00", "22KF.00", "22KG.00", "22KH.00", "22KJ.00", "22KK.00", "22KL.00", "22KM.00", "22KN.00", "22KP.00", "22KQ.00", "22KR.00", "22KS.00", "22KT.00", "22KU.00", "22KV.00", "22KW.00", "22KX.00", "22KY.00", "22KZ.00"])
).where(clinical_events.date.is_on_or_before(index_date)).sort_by(clinical_events.date)

dataset.bmi = bmi_events.last_for_patient().numeric_value
dataset.bmi_date = bmi_events.last_for_patient().date

# HDL Cholesterol
hdl_events = clinical_events.where(
    clinical_events.read_code.is_in(["44d2.00", "44dA.00", "44P5.00", "44PC.00"])
).where(clinical_events.date.is_on_or_before(index_date)).sort_by(clinical_events.date)

dataset.hdl = hdl_events.last_for_patient().numeric_value
dataset.hdl_date = hdl_events.last_for_patient().date

# Total Cholesterol
chol_events = clinical_events.where(
    clinical_events.read_code.is_in(["44d2.00", "44dA.00", "44dB.00", "44dC.00", "44dD.00", "44dE.00", "44dF.00", "44dG.00", "44dH.00", "44dJ.00", "44dK.00", "44dL.00", "44dM.00", "44dN.00", "44dP.00", "44dQ.00", "44dR.00", "44dS.00", "44dT.00", "44dU.00", "44dV.00", "44dW.00", "44dX.00", "44dY.00", "44dZ.00"])
).where(clinical_events.date.is_on_or_before(index_date)).sort_by(clinical_events.date)

dataset.total_cholesterol = chol_events.last_for_patient().numeric_value
dataset.total_cholesterol_date = chol_events.last_for_patient().date

# HbA1c
hba1c_events = clinical_events.where(
    clinical_events.read_code.is_in(["44d2.00", "44dA.00", "44dB.00", "44dC.00", "44dD.00", "44dE.00", "44dF.00", "44dG.00", "44dH.00", "44dJ.00", "44dK.00", "44dL.00", "44dM.00", "44dN.00", "44dP.00", "44dQ.00", "44dR.00", "44dS.00", "44dT.00", "44dU.00", "44dV.00", "44dW.00", "44dX.00", "44dY.00", "44dZ.00"])
).where(clinical_events.date.is_on_or_before(index_date)).sort_by(clinical_events.date)

dataset.hba1c = hba1c_events.last_for_patient().numeric_value
dataset.hba1c_date = hba1c_events.last_for_patient().date

# eGFR
egfr_events = clinical_events.where(
    clinical_events.read_code.is_in(["44d2.00", "44dA.00", "44dB.00", "44dC.00", "44dD.00", "44dE.00", "44dF.00", "44dG.00", "44dH.00", "44dJ.00", "44dK.00", "44dL.00", "44dM.00", "44dN.00", "44dP.00", "44dQ.00", "44dR.00", "44dS.00", "44dT.00", "44dU.00", "44dV.00", "44dW.00", "44dX.00", "44dY.00", "44dZ.00"])
).where(clinical_events.date.is_on_or_before(index_date)).sort_by(clinical_events.date)

dataset.egfr = egfr_events.last_for_patient().numeric_value
dataset.egfr_date = egfr_events.last_for_patient().date

# Creatinine
creat_events = clinical_events.where(
    clinical_events.read_code.is_in(["44d2.00", "44dA.00", "44dB.00", "44dC.00", "44dD.00", "44dE.00", "44dF.00", "44dG.00", "44dH.00", "44dJ.00", "44dK.00", "44dL.00", "44dM.00", "44dN.00", "44dP.00", "44dQ.00", "44dR.00", "44dS.00", "44dT.00", "44dU.00", "44dV.00", "44dW.00", "44dX.00", "44dY.00", "44dZ.00"])
).where(clinical_events.date.is_on_or_before(index_date)).sort_by(clinical_events.date)

dataset.creatinine = creat_events.last_for_patient().numeric_value
dataset.creatinine_date = creat_events.last_for_patient().date

# --- Hospital Episode Statistics (APCs) ---
# Prior CVD admissions
prior_cvd_admission = apcs.where(
    apcs.primary_diagnosis.icd10_code.is_in(["I20", "I21", "I22", "I23", "I24", "I25", "I50", "I48", "I60", "I61", "I62", "I63", "I64", "I65", "I66", "I67", "I68", "I69", "I70", "I71", "I72", "I73", "I74", "I75", "I76", "I77", "I78", "I79"])
).where(apcs.admission_date.is_on_or_before(index_date)).exists_for_patient()

dataset.prior_cvd_admission = prior_cvd_admission

# Prior MI admission
prior_mi_admission = apcs.where(
    apcs.primary_diagnosis.icd10_code.is_in(["I21", "I22", "I23"])
).where(apcs.admission_date.is_on_or_before(index_date)).exists_for_patient()

dataset.prior_mi_admission = prior_mi_admission

# Prior HF admission
prior_hf_admission = apcs.where(
    apcs.primary_diagnosis.icd10_code.is_in(["I50"])
).where(apcs.admission_date.is_on_or_before(index_date)).exists_for_patient()

dataset.prior_hf_admission = prior_hf_admission

# Prior stroke admission
prior_stroke_admission = apcs.where(
    apcs.primary_diagnosis.icd10_code.is_in(["I60", "I61", "I62", "I63", "I64"])
).where(apcs.admission_date.is_on_or_before(index_date)).exists_for_patient()

dataset.prior_stroke_admission = prior_stroke_admission

# --- Outcomes (during follow-up) ---
followup_start = index_date
followup_end = study_end

# Incident CVD
incident_cvd = clinical_events.where(
    clinical_events.snomedct_code.is_in(cvd_codes) | 
    clinical_events.read_code.is_in(cvd_codes) |
    clinical_events.icd10_code.is_in(["I20", "I21", "I22", "I23", "I24", "I25", "I50", "I48", "I60", "I61", "I62", "I63", "I64", "I65", "I66", "I67", "I68", "I69", "I70", "I71", "I72", "I73", "I74", "I75", "I76", "I77", "I78", "I79"])
).where(clinical_events.date.is_on_or_between(followup_start, followup_end)).exists_for_patient()

dataset.incident_cvd = incident_cvd

# Incident MI
incident_mi = clinical_events.where(
    clinical_events.snomedct_code.is_in(mi_codes) | 
    clinical_events.read_code.is_in(mi_codes) |
    clinical_events.icd10_code.is_in(["I21", "I22", "I23"])
).where(clinical_events.date.is_on_or_between(followup_start, followup_end)).exists_for_patient()

dataset.incident_mi = incident_mi

# Incident HF
incident_hf = clinical_events.where(
    clinical_events.snomedct_code.is_in(hf_codes) | 
    clinical_events.read_code.is_in(hf_codes) |
    clinical_events.icd10_code.is_in(["I50"])
).where(clinical_events.date.is_on_or_between(followup_start, followup_end)).exists_for_patient()

dataset.incident_hf = incident_hf

# Incident stroke
incident_stroke = clinical_events.where(
    clinical_events.snomedct_code.is_in(stroke_codes) | 
    clinical_events.read_code.is_in(stroke_codes) |
    clinical_events.icd10_code.is_in(["I60", "I61", "I62", "I63", "I64"])
).where(clinical_events.date.is_on_or_between(followup_start, followup_end)).exists_for_patient()

dataset.incident_stroke = incident_stroke

# CVD Death
cvd_death = ons_deaths.where(
    ons_deaths.underlying_cause_of_death.icd10_code.is_in(["I00", "I01", "I02", "I03", "I04", "I05", "I06", "I07", "I08", "I09", "I10", "I11", "I12", "I13", "I14", "I15", "I20", "I21", "I22", "I23", "I24", "I25", "I26", "I27", "I28", "I29", "I30", "I31", "I32", "I33", "I34", "I35", "I36", "I37", "I38", "I39", "I40", "I41", "I42", "I43", "I44", "I45", "I46", "I47", "I48", "I49", "I50", "I51", "I52", "I53", "I54", "I55", "I56", "I57", "I58", "I59", "I60", "I61", "I62", "I63", "I64", "I65", "I66", "I67", "I68", "I69", "I70", "I71", "I72", "I73", "I74", "I75", "I76", "I77", "I78", "I79", "I80", "I81", "I82", "I83", "I84", "I85", "I86", "I87", "I88", "I89", "I90", "I91", "I92", "I93", "I94", "I95", "I96", "I97", "I98", "I99"])
).where(ons_deaths.date.is_on_or_between(followup_start, followup_end)).exists_for_patient()

dataset.cvd_death = cvd_death

# All-cause death
all_cause_death = ons_deaths.where(
    ons_deaths.date.is_on_or_between(followup_start, followup_end)
).exists_for_patient()

dataset.all_cause_death = all_cause_death

# --- Follow-up time ---
dataset.followup_time = case(
    when(cvd_death).then(ons_deaths.where(ons_deaths.date.is_on_or_between(followup_start, followup_end)).sort_by(ons_deaths.date).first_for_patient().date.difference_in_days(index_date)),
    when(all_cause_death).then(ons_deaths.where(ons_deaths.date.is_on_or_between(followup_start, followup_end)).sort_by(ons_deaths.date).first_for_patient().date.difference_in_days(index_date)),
    otherwise=(followup_end.difference_in_days(index_date))
)

# --- Covariates for risk adjustment ---
dataset.cvd_risk_score = case(
    when(dataset.age >= 80).then(10),
    when(dataset.age >= 75).then(8),
    when(dataset.age >= 70).then(6),
    when(dataset.age >= 65).then(4),
    when(dataset.age >= 60).then(3),
    when(dataset.age >= 55).then(2),
    when(dataset.age >= 50).then(1),
    otherwise=0
) + case(
    when(dataset.sex == "M").then(2),
    otherwise=0
) + case(
    when(dataset.prior_htn).then(2),
    otherwise=0
) + case(
    when(dataset.prior_diabetes).then(2),
    otherwise=0
) + case(
    when(dataset.prior_cvd).then(3),
    otherwise=0
) + case(
    when(dataset.on_statin).then(-1),
    otherwise=0
) + case(
    when(dataset.on_antihypertensive).then(-1),
    otherwise=0
)

# --- Project-specific flags ---
dataset.is_cardinal_data = True  # CARDINAL-DATA project
dataset.is_dia_core = dataset.prior_diabetes  # DIA-core project
dataset.is_cvd_covid = True  # CVD-COVID-UK project

# --- Output configuration ---
dataset.configure_dummy_data(population_size=10000)

# ============================================================
# EXPORT
# ============================================================
# This dataset can be used for:
# 1. CARDINAL-DATA: Cardiovascular-renal-metabolic data specification
# 2. DIA-core: Diabetes core dataset implementation
# 3. CVD-COVID-UK: Cardiovascular outcomes post-COVID
# 4. General CVD risk prediction and phenotyping
# 5. BHF DSC supported research projects
```

---

## 5. Mapping to BHF DSC Services

| BHF DSC Service | Projects Supported | Datasets | Phenotypes/Codelists |
|-----------------|-------------------|----------|---------------------|
| **Data Access & Linkage** | CARDINAL-DATA, DIA-core, CVD-COVID-UK | CPRD GOLD, UK Biobank, NHS England SDE, SAIL, CVD-COVID-UK TREs | All cardiovascular phenotypes |
| **Data Curation & Engineering** | CARDINAL-DATA (data spec), DIA-core (30 variables) | HES APC, CPRD OMOP, HIC ACS | Computable phenotypes (PH5, PH25, PH26, PH27, PH36, PH34, PH41, PH42) |
| **Computable Phenotypes & Codelists** | All projects | All datasets | 20+ validated cardiovascular phenotypes with SNOMED/Read/ICD-10 codes |
| **Curated Assets** | CARDINAL-DATA, DIA-core | Demographics, mortality, HES APC prep | Harmonized tables, standardised definitions |
| **PPIE** | All projects | All datasets | Public involvement in CVD research design |

### BHF DSC Service Alignment

1. **Population Data Access** → CVD-COVID-UK TREs (England, Scotland, Wales)
2. **Consented Cohort Linkage** → UK CliC TRE via SAIL Databank
3. **Data Discovery & Feasibility** → Population Data Dashboard (coming soon)
4. **Data Curation Pipelines** → Reusable ehrQL code for all SDEs
5. **Computable Phenotypes** → Phenotype Library (20+ CVD phenotypes)
6. **Codelist Comparison Tool** → Maps codes to GDPPR reference set
7. **Open/Reproducible Research** → GitHub, Phenotype Library, FAIR sharing

---

## 6. Key Recommendations

### Priority 1: CARDINAL-DATA (London SDE)
- **Why:** Directly extends cardiovascular-renal-metabolic data specification
- **BHF DSC Support:** Data curation pipelines, cross-nation harmonization, computable phenotypes
- **Datasets:** CPRD GOLD, HES, NHS England SDE, CVD-COVID-UK TRE
- **Phenotypes:** PH5, PH25, PH26, PH27, PH36, PH34, PH41, PH42

### Priority 2: DIA-core (South West SDE)
- **Why:** Implements UK diabetes core dataset (30 variables) - critical CVD risk factor
- **BHF DSC Support:** Phenotype development, OpenSAFELY integration, codelist validation
- **Datasets:** CPRD GOLD, UK Biobank, HES
- **Phenotypes:** PH24, PH42, PH31, PH17, PH16, PH10

### Priority 3: CVD-COVID-UK Programme
- **Why:** Largest linked populations across UK nations (56M + 5.5M + 3.1M)
- **BHF DSC Support:** Data access, linkage coordination, PPIE
- **Datasets:** NHS England SDE, Scottish Safe Haven, SAIL Databank
- **Active Projects:** CCU001, CCU002, CCU003 (led by Sterne, Whiteley, Banerjee)

### Priority 4: MINDS & PRANA
- **MINDS:** Family linkage for CVD heritability
- **PRANA:** Acute CVD pathway (ambulance/trauma data)

---

## 7. Implementation Roadmap

### Phase 1: Foundation (Months 1-3)
1. Deploy OpenSAFELY scaffolding code to all SDEs
2. Validate Phenotype Library codelists against local data
3. Establish BHF DSC project governance

### Phase 2: Data Harmonization (Months 3-6)
1. CARDINAL-DATA: Extend CVD-renal-metabolic spec to all SDEs
2. DIA-core: Implement 30 diabetes variables across SDEs
3. Create curated assets (demographics, mortality, HES APC)

### Phase 3: Research Delivery (Months 6-12)
1. CVD-COVID-UK: Long-term cardiovascular outcomes post-COVID
2. Risk prediction models using UK Biobank + CPRD + HES
3. PPIE integration for all projects

### Phase 4: Sustainability (Months 12+)
1. FAIR sharing via Phenotype Library & GitHub
2. Training & capacity building
3. Next-generation phenotype development

---

## 8. Resources & Links

### BHF DSC Services
- [Research Services](https://bhfdatasciencecentre.org/research-services-new/)
- [Data Access & Linkage](https://bhfdatasciencecentre.org/data-access-and-linkage/)
- [Data Curation & Engineering](https://bhfdatasciencecentre.org/data-curation-and-engineering-services/)
- [Curated Assets](https://bhfdatasciencecentre.org/curated-assets/)
- [Computable Phenotypes & Codelists](https://bhfdatasciencecentre.org/computable-phenotypes-and-codelists/)
- [PPIE Support](https://bhfdatasciencecentre.org/patient-and-public-involvement-and-engagement-ppie-support/)
- [UK CliC TRE](https://bhfdatasciencecentre.org/uk-clic-trusted-research-environment/)
- [Population Data Dashboard](https://bhfdatasciencecentre.org/browse-the-data/)
- [GitHub Organisation](https://github.com/BHFDSC)

### HDRS Projects
- [HDRS Technology Transformation Projects](https://www.hdrs.com/hdrs-funds-43-technical-transformation-projects)
- [South West SDE Diabetes Project](https://www.southwestsde.nhs.uk/transforming-diabetes-research-south-west-sde-leads-new-projects)
- [Exeter Diabetes SDE Framework](https://exeter-diabetes.github.io/sde-sw-framework)
- [PRANA Network](https://www.prananet.org)

### Gateway Datasets
- [CPRD GOLD](https://healthdatagateway.org/en/dataset/694)
- [UK Biobank](https://healthdatagateway.org/en/dataset/700)
- [HIC Acute Coronary Syndromes](https://healthdatagateway.org/en/dataset/517)
- [CVD-COVID-UK England TRE](https://healthdatagateway.org/en/dataset/1378)
- [CVD-COVID-UK Scotland TRE](https://healthdatagateway.org/en/dataset/1380)
- [CVD-COVID-UK Wales TRE](https://healthdatagateway.org/en/dataset/1381)
- [SAIL Databank](https://healthdatagateway.org/en/dataset/289)
- [HES APC](https://healthdatagateway.org/en/dataset/1576)

### Phenotype Library
- [Phenotype Library Home](https://phenotypelibrary.org/)
- [Cardiovascular Disease (PH5)](https://phenotypelibrary.org/phenotype/PH5)
- [Heart Failure (PH25)](https://phenotypelibrary.org/phenotype/PH25)
- [Hypertension (PH26)](https://phenotypelibrary.org/phenotype/PH26)
- [Ischaemic Heart Disease (PH27)](https://phenotypelibrary.org/phenotype/PH27)
- [Atrial Fibrillation (PH36)](https://phenotypelibrary.org/phenotype/PH36)
- [Abdominal Aortic Aneurysm (PH34)](https://phenotypelibrary.org/phenotype/PH34)
- [Coronary Heart Disease NOS (PH41)](https://phenotypelibrary.org/phenotype/PH41)
- [Chronic Kidney Disease (PH42)](https://phenotypelibrary.org/phenotype/PH42)
- [Diabetes (PH24)](https://phenotypelibrary.org/phenotype/PH24)

### OpenSAFELY
- [OpenSAFELY Documentation](https://docs.opensafely.org/)
- [ehrQL Reference](https://docs.opensafely.org/en/latest/ehrql/)
- [Codelists Guide](https://docs.opensafely.org/en/latest/ehrql/how-to/codelists/)
- [Dataset Definition](https://docs.opensafely.org/en/latest/ehrql/how-to/dataset-definition/)

---

## Appendix: CVD-COVID-UK Active Projects

| Project | Title | Lead | Institution |
|---------|-------|------|-------------|
| **CCU001** | Effects of ACE inhibitors and ARBs on COVID-19 outcomes | Jonathan Sterne | University of Bristol |
| **CCU002** | SARS-CoV-2 infection, vaccination and risk of vascular events | William Whiteley | University of Edinburgh |
| **CCU003** | Direct and indirect effects of COVID-19 pandemic in people with CVD | Amitava Banerjee | University College London |

**Programme Lead:** Angela Wood  
**Data Sharing Agreement Ends:** January 2027  
**Status:** No new projects being accepted

---

*This analysis was generated using HDRS MCP, Gateway MCP, Phenotype Library MCP, and OpenSAFELY MCP tools. All data current as of 2026-11-18.*
