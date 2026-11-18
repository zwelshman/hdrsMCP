# BHF Data Science Centre - HDRS Project Analysis & OpenSAFELY Scaffold

## Summary

This analysis identifies **5 high-priority HDRS projects** that would benefit from BHF Data Science Centre services, maps **3 key cardiovascular datasets** from the HDRUK Gateway, identifies **8 core computable phenotypes** from the HDRUK Phenotype Library, and generates a complete **OpenSAFELY project scaffold** for cardiovascular research.

---

## 1. HDRS Projects Benefiting from BHF DSC Services

| Priority | Project | Institution | Key BHF DSC Services Needed |
|----------|---------|-------------|----------------------------|
| 🔴 **Critical** | **CARDINAL-DATA** | London SDE (OneLondon) | Data curation, phenotype implementation, harmonised demographics, CRM data specification |
| 🟠 **High** | **CoFIND** | NHS Research SDE Network | Cohort discovery, linkage coordination, data discovery, computable phenotypes |
| 🟠 **High** | **TETHER** | DataLoch (Scottish Safe Haven) | Data virtualisation, quality monitoring, cross-nation harmonisation, data curation pipelines |
| 🟠 **High** | **The Epi700 Multimodal Exemplar** | NHS Research SDE Network | Multimodal linkage, phenotype implementation, cloud-agnostic reference design |
| 🟠 **High** | **Federated and Harmonised Multi-SDE Linkage** | NHS Research SDE Network | Multi-SDE linkage coordination, harmonisation, data discovery |

### Supporting Projects
- **NHS DigiTrials Recruitment Connect** (NHS England) - PPIE, cohort linkage
- **SCALA** (DataLoch/eDRIS) - Cross-nation harmonisation, Scottish network

---

## 2. HDRUK Gateway Datasets for Cardiovascular Research

| Dataset ID | Title | Custodian | Key Variables | Research Alignment |
|------------|-------|-----------|---------------|-------------------|
| **1906** | Lipoprotein (a) testing in ASCVD patients UK | West Midlands SDE | Lp(a) testing, ASCVD cohorts (premature, recurrent, new), HCRU, medications, procedures | **Primary** - Direct alignment with BHF DSC CVD-COVID-UK themes |
| **1821** | Myocardial infarction datasets | Various | MI diagnoses, procedures, outcomes | Secondary - MI sub-cohort definition |
| **1986** | Heart failure datasets | Various | HF diagnoses, ejection fraction, medications | Secondary - HF sub-cohort, outcomes |

### Linkage Opportunities
- **Population-wide**: NHS England SDE, National Data Safe Haven Scotland, SAIL Databank Wales
- **Cohort-linked**: UK CliC TRE for consented cohort data linked to NHS data
- **Cross-nation**: BHF DSC supports linked studies spanning England, Scotland, Wales

---

## 3. HDRUK Phenotype Library - Computable Phenotypes & Codelists

### Core Cardiovascular Phenotypes (Ready for OpenSAFELY)

| Phenotype ID | Name | Coding System | Key Codes | OpenSAFELY Variable |
|--------------|------|---------------|-----------|---------------------|
| **PH5** | Cardiovascular Disease | Read v2 | G3... (IHD), G5... (CVD) | `has_cvd`, `cvd_date` |
| **PH25** | Heart Failure | SNOMED CT | 42343007, 48447003, 10633002, 418304008, 426263006 | `has_hf`, `hf_date`, `hf_type` |
| **PH26** | Hypertension | SNOMED CT | 59621000 | `has_htn`, `htn_date` |
| **PH22** | Chronic Kidney Disease | SNOMED CT | 709044004, 433144002, 90688005 | `has_ckd`, `ckd_date`, `ckd_stage` |
| **PH24** | Diabetes | SNOMED CT | 44054006, 237599002 | `has_diabetes`, `diabetes_date`, `diabetes_type` |

### Biomarker Phenotypes (Covariate Adjustment)

| Phenotype ID | Name | Data Source | Measurement Range | OpenSAFELY Variable |
|--------------|------|-------------|-------------------|---------------------|
| **PH10** | Heart Rate | CPRD GOLD | Pulse measurements | `heart_rate` |
| **PH16** | Blood Pressure | CPRD GOLD | SBP 20-350, DBP 20-200 mmHg | `sbp`, `dbp`, `bp_category` |
| **PH17** | Body Mass Index | CPRD GOLD | BMI 10-80 kg/m² | `bmi`, `bmi_category` |

### Additional Comorbidity Phenotypes
- **PH1** - COVID-19 infection (pandemic-era studies)
- **PH2/PH3** - Anxiety/Depression (mental health)
- **PH11/PH21** - Asthma (respiratory)
- **PH23** - COPD (respiratory)

---

## 4. BHF DSC Services → Project Mapping

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

## 5. OpenSAFELY Project Scaffold Generated

### Complete Project Structure
```
cardiovascular-research/
├── project.yaml                    # OpenSAFELY project configuration
├── analysis/
│   ├── cohort_definition.py        # Population, index dates, comorbidities, CRM profiles
│   ├── dataset_definition.py       # Medications, biomarkers, prior events, outcomes
│   ├── variables.py                # Derived variables, risk scores, treatment patterns
│   ├── measures.py                 # Population measures for BHF DSC Dashboard
│   ├── codelists.py                # All codelist imports (PH5, PH25, PH26, PH22, PH24, PH10, PH16, PH17)
│   └── main.py                     # Analysis execution (4 analyses)
├── codelists/
│   ├── cardiovascular_disease.csv  # PH5 - Read v2 codes
│   ├── heart_failure.csv           # PH25 - SNOMED CT codes
│   ├── hypertension.csv            # PH26 - SNOMED CT codes
│   ├── chronic_kidney_disease.csv  # PH22 - SNOMED CT codes
│   ├── diabetes.csv                # PH24 - SNOMED CT codes
│   ├── mi_codes.csv                # MI-specific codes
│   ├── medications/                # BNF chapter codelists
│   │   ├── ace_inhibitors.csv
│   │   ├── arbs.csv
│   │   ├── beta_blockers.csv
│   │   ├── statins.csv
│   │   ├── anticoagulants.csv
│   │   └── antiplatelets.csv
│   └── biomarkers/                 # Biomarker test codes
│       ├── lpa_testing.csv         # Dataset 1906 alignment
│       ├── lipid_profile.csv
│       ├── renal_function.csv
│       ├── bp_systolic.csv
│       ├── bp_diastolic.csv
│       ├── bmi.csv
│       └── heart_rate.csv
├── tests/                          # Unit tests
└── README.md                       # Documentation
```

### Key Features Implemented

#### Cohort Definitions (`cohort_definition.py`)
- **Population**: Adults 18+ registered in TPP practices during 2019-2026
- **Index date**: First CVD diagnosis (PH5) or fixed date
- **Comorbidities**: CVD, MI, HF (PH25), HTN (PH26), CKD (PH22), Diabetes (PH24)
- **Charlson Comorbidity Index** calculated from clinical events
- **Harmonised Demographics** (BHF DSC): age, sex, ethnicity, IMD, region, rural/urban
- **CRM Multimorbidity**: Cardiovascular-renal-metabolic profiles

#### Dataset Definition (`dataset_definition.py`)
- **Medications**: Current (6mo) and prior (ever) for ACEi, ARB, BB, Statin, Anticoag, Antiplatelet
- **Biomarkers**: Lp(a) (dataset 1906), lipids, eGFR, creatinine, BP (PH16), BMI (PH17), HR (PH10)
- **Prior Events**: MI admission, HF admission, stroke, PCI, CABG, hospitalization count
- **Outcomes**: MACE (CV death, MI, stroke, HF hosp), all-cause mortality, CV mortality
- **Covariates**: Smoking, alcohol, follow-up time

#### Derived Variables (`variables.py`)
- **Risk Scores**: CHA2DS2-VASc, HAS-BLED
- **CRM Profiles**: 15 multimorbidity combinations
- **Treatment Patterns**: GDMT for HF, secondary prevention post-MI
- **Lp(a) Risk Categories**: ESC/EAS guidelines (<30, 30-50, 50-100, 100-180, ≥180 nmol/L)
- **Medication Initiation**: New starts in first year post-diagnosis

#### Measures (`measures.py`) - BHF DSC Population Data Dashboard Aligned
- **Prevalence**: CVD, HF by age/sex/IMD/HF type
- **Medication**: Statin in CVD, ACEi/ARB/BB in HF, GDMT completion in HFrEF
- **Biomarker Testing**: Lp(a) testing rate by cohort, IMD, ethnicity, region
- **Outcomes**: MACE incidence, mortality, HF hospitalization by CRM profile
- **Equity**: All measures stratified by IMD quintile, ethnicity, region

#### Analyses (`main.py`)
1. **Lp(a) Testing Patterns** - Annual prevalence/incidence in ASCVD cohorts (Dataset 1906)
2. **CRM Multimorbidity Outcomes** - Incidence rates by CRM profile
3. **Medication Initiation** - GDMT initiation after incident CVD
4. **Equity Analysis** - Care and outcomes by IMD, ethnicity, region

---

## 6. Files Created

| File | Description |
|------|-------------|
| `bhf_dsc_analysis_report.md` | Detailed analysis report |
| `opensafely_cardiovascular_scaffold/` | Complete OpenSAFELY project scaffold |
| `SUMMARY.md` | This summary document |

---

## 7. Next Steps for Implementation

### For CARDINAL-DATA (Highest Priority)
1. **Deploy scaffold** to OpenSAFELY workspace
2. **Validate codelists** using BHF DSC Codelist Comparison Tool
3. **Run in London SDE** (OneLondon) with NHS England data
4. **Link to UK CliC** for consented cohort data if needed
5. **Engage BHF DSC** for data curation support and PPIE

### For CoFIND / Multi-SDE Linkage
1. **Adapt scaffold** for federated analysis across SDEs
2. **Use BHF DSC linkage coordination** for cross-SDE data access
3. **Implement harmonised variables** using BHF DSC curated assets

### For TETHER / Epi700
1. **Extend scaffold** with data virtualisation layer
2. **Add quality monitoring** metrics to measures
3. **Integrate multimodal data** (imaging, pathology, omics)

---

## 8. Key References

- **BHF DSC Services**: https://bhfdatasciencecentre.org/research-services-new/
- **HDRUK Phenotype Library**: https://phenotypelibrary.org/
- **HDRUK Gateway**: https://healthdatagateway.org/
- **OpenSAFELY Documentation**: https://docs.opensafely.org/
- **ehrQL Reference**: https://ehrql.opensafely.org/
- **Dataset 1906**: Lp(a) testing in ASCVD (West Midlands SDE)
- **CVD-COVID-UK**: https://bhfdatasciencecentre.org/research/data-access-and-linkage/population-data/cvd-covid-uk-covid-impact/