# OpenSAFELY Cardiovascular Research Project Scaffold
# Generated based on BHF Data Science Centre services alignment

## Project Structure
```
cardiovascular-research/
├── project.yaml
├── analysis/
│   ├── __init__.py
│   ├── dataset_definition.py
│   ├── cohort_definition.py
│   ├── codelists.py
│   ├── variables.py
│   ├── measures.py
│   └── main.py
├── codelists/
│   ├── cardiovascular_disease.csv
│   ├── heart_failure.csv
│   ├── hypertension.csv
│   ├── chronic_kidney_disease.csv
│   ├── diabetes.csv
│   ├── mi_codes.csv
│   ├── medications/
│   │   ├── ace_inhibitors.csv
│   │   ├── arbs.csv
│   │   ├── beta_blockers.csv
│   │   ├── statins.csv
│   │   ├── anticoagulants.csv
│   │   └── antiplatelets.csv
│   └── biomarkers/
│       ├── lpa_testing.csv
│       ├── lipid_profile.csv
│       └── renal_function.csv
├── outputs/
│   └── .gitkeep
├── tests/
│   ├── test_codelists.py
│   ├── test_cohort.py
│   └── test_variables.py
└── README.md
```

## project.yaml
```yaml
version: "3.0"
expectations:
  population_size: 100000

actions:
  # Generate study population
  generate_cohort:
    run: python:latest analysis/cohort_definition.py
    outputs:
      highly_sensitive:
        cohort: output/cohort.parquet
        cohort_csv: output/cohort.csv

  # Generate dataset with all variables
  generate_dataset:
    run: python:latest analysis/dataset_definition.py
    needs: [generate_cohort]
    outputs:
      highly_sensitive:
        dataset: output/dataset.parquet
        dataset_csv: output/dataset.csv

  # Run main analysis
  run_analysis:
    run: python:latest analysis/main.py
    needs: [generate_dataset]
    outputs:
      moderately_sensitive:
        results: output/results/*.csv
        figures: output/results/*.png
        logs: output/logs/*.log

  # Generate measures for reporting
  generate_measures:
    run: python:latest analysis/measures.py
    needs: [generate_dataset]
    outputs:
      moderately_sensitive:
        measures: output/measures/*.csv
```

## analysis/codelists.py
```python
"""
Codelist definitions aligned with BHF DSC / HDRUK Phenotype Library
Maps PH5, PH25, PH26, PH22, PH24, PH10, PH16, PH17 phenotypes to OpenSAFELY codelists
"""

from ehrql import codelist_from_csv
from ehrql.tables.tpp import clinical_events, medications, patients

# ============================================================
# CARDIOVASCULAR DISEASE PHENOTYPES (PH5 - Cardiovascular Disease)
# ============================================================

# Primary CVD codelist (Read v2 codes from PH5)
cvd_codelist = codelist_from_csv(
    "codelists/cardiovascular_disease.csv",
    column="code",
    category_column="category"
)

# Myocardial Infarction specific codes
mi_codelist = codelist_from_csv(
    "codelists/mi_codes.csv",
    column="code",
    category_column="category"
)

# Heart Failure (PH25)
heart_failure_codelist = codelist_from_csv(
    "codelists/heart_failure.csv",
    column="code",
    category_column="category"
)

# Hypertension (PH26)
hypertension_codelist = codelist_from_csv(
    "codelists/hypertension.csv",
    column="code",
    category_column="category"
)

# Chronic Kidney Disease (PH22)
ckd_codelist = codelist_from_csv(
    "codelists/chronic_kidney_disease.csv",
    column="code",
    category_column="category"
)

# Diabetes (PH24)
diabetes_codelist = codelist_from_csv(
    "codelists/diabetes.csv",
    column="code",
    category_column="category"
)

# ============================================================
# MEDICATION CODELISTS (BNF chapters)
# ============================================================

# ACE Inhibitors (BNF 2.5.5.1)
ace_inhibitors_codelist = codelist_from_csv(
    "codelists/medications/ace_inhibitors.csv",
    column="code",
    category_column="bnf_subsection"
)

# ARBs (BNF 2.5.5.2)
arbs_codelist = codelist_from_csv(
    "codelists/medications/arbs.csv",
    column="code",
    category_column="bnf_subsection"
)

# Beta Blockers (BNF 2.4)
beta_blockers_codelist = codelist_from_csv(
    "codelists/medications/beta_blockers.csv",
    column="code",
    category_column="bnf_subsection"
)

# Statins (BNF 2.12)
statins_codelist = codelist_from_csv(
    "codelists/medications/statins.csv",
    column="code",
    category_column="bnf_subsection"
)

# Anticoagulants (BNF 2.8.2)
anticoagulants_codelist = codelist_from_csv(
    "codelists/medications/anticoagulants.csv",
    column="code",
    category_column="bnf_subsection"
)

# Antiplatelets (BNF 2.9)
antiplatelets_codelist = codelist_from_csv(
    "codelists/medications/antiplatelets.csv",
    column="code",
    category_column="bnf_subsection"
)

# ============================================================
# BIOMARKER CODELISTS
# ============================================================

# Lipoprotein(a) testing (from dataset 1906)
lpa_testing_codelist = codelist_from_csv(
    "codelists/biomarkers/lpa_testing.csv",
    column="code",
    category_column="test_type"
)

# Lipid profile
lipid_profile_codelist = codelist_from_csv(
    "codelists/biomarkers/lipid_profile.csv",
    column="code",
    category_column="test_type"
)

# Renal function (eGFR, creatinine)
renal_function_codelist = codelist_from_csv(
    "codelists/biomarkers/renal_function.csv",
    column="code",
    category_column="test_type"
)

# Blood Pressure measurements (PH16)
bp_systolic_codelist = codelist_from_csv(
    "codelists/biomarkers/bp_systolic.csv",
    column="code"
)

bp_diastolic_codelist = codelist_from_csv(
    "codelists/biomarkers/bp_diastolic.csv",
    column="code"
)

# BMI measurements (PH17)
bmi_codelist = codelist_from_csv(
    "codelists/biomarkers/bmi.csv",
    column="code"
)

# Heart Rate (PH10)
heart_rate_codelist = codelist_from_csv(
    "codelists/biomarkers/heart_rate.csv",
    column="code"
)
```

## analysis/cohort_definition.py
```python
"""
Cohort definition for cardiovascular research
Aligns with BHF DSC services: population data access, cohort linkage, computable phenotypes
"""

from ehrql import create_dataset, case, when, minimum_of, maximum_of
from ehrql.tables.tpp import (
    patients, clinical_events, medications, practice_registrations,
    hospital_admissions, hospital_diagnoses, hospital_procedures,
    ons_deaths, addresses
)
from analysis.codelists import (
    cvd_codelist, mi_codelist, heart_failure_codelist,
    hypertension_codelist, ckd_codelist, diabetes_codelist,
    ace_inhibitors_codelist, arbs_codelist, beta_blockers_codelist,
    statins_codelist, anticoagulants_codelist, antiplatelets_codelist,
    lpa_testing_codelist, lipid_profile_codelist, renal_function_codelist,
    bp_systolic_codelist, bp_diastolic_codelist, bmi_codelist, heart_rate_codelist
)

# Create dataset
dataset = create_dataset()

# ============================================================
# STUDY PERIOD & INDEX DATES
# ============================================================

# Study period (aligns with BHF DSC CVD-COVID-UK timeframe)
study_start = "2019-01-01"
study_end = "2026-12-31"

# Index date for cohort entry (e.g., first CVD diagnosis)
index_date = clinical_events.where(
    clinical_events.snomedct_code.is_in(cvd_codelist)
).sort_by(clinical_events.date).first_for_patient().date

# Alternative: Fixed index date for prevalent cohort
# index_date = "2020-01-01"

# ============================================================
# POPULATION DEFINITION
# ============================================================

# Registered at a practice during study period
has_registration = practice_registrations.where(
    practice_registrations.start_date <= study_end
).where(
    practice_registrations.end_date >= study_start
).exists_for_patient()

# Age criteria (adults 18+)
age_at_index = patients.age_on(index_date)
is_adult = age_at_index >= 18

# Sex
sex = patients.sex

# Alive at index date
alive_at_index = patients.date_of_death.is_after(index_date) | patients.date_of_death.is_null()

# Define population
dataset.define_population(
    has_registration & is_adult & alive_at_index
)

# ============================================================
# COHORT DEFINITIONS
# ============================================================

# --- Primary CVD Cohort (PH5) ---
has_cvd = clinical_events.where(
    clinical_events.snomedct_code.is_in(cvd_codelist)
).where(
    clinical_events.date <= index_date
).exists_for_patient()

# CVD diagnosis date
cvd_date = clinical_events.where(
    clinical_events.snomedct_code.is_in(cvd_codelist)
).where(
    clinical_events.date <= index_date
).sort_by(clinical_events.date).first_for_patient().date

# --- MI Sub-cohort ---
has_mi = clinical_events.where(
    clinical_events.snomedct_code.is_in(mi_codelist)
).where(
    clinical_events.date <= index_date
).exists_for_patient()

mi_date = clinical_events.where(
    clinical_events.snomedct_code.is_in(mi_codelist)
).where(
    clinical_events.date <= index_date
).sort_by(clinical_events.date).first_for_patient().date

# --- Heart Failure Sub-cohort (PH25) ---
has_hf = clinical_events.where(
    clinical_events.snomedct_code.is_in(heart_failure_codelist)
).where(
    clinical_events.date <= index_date
).exists_for_patient()

hf_date = clinical_events.where(
    clinical_events.snomedct_code.is_in(heart_failure_codelist)
).where(
    clinical_events.date <= index_date
).sort_by(clinical_events.date).first_for_patient().date

# HF type classification
hf_type = case(
    when(clinical_events.where(
        clinical_events.snomedct_code.is_in(["418304008"])  # Diastolic HF
    ).where(clinical_events.date <= index_date).exists_for_patient()).then("HFpEF"),
    when(clinical_events.where(
        clinical_events.snomedct_code.is_in(["426263006"])  # HF due to LV systolic dysfunction
    ).where(clinical_events.date <= index_date).exists_for_patient()).then("HFrEF"),
    when(has_hf).then("HF_unspecified"),
    otherwise="No_HF"
)

# --- Hypertension (PH26) ---
has_htn = clinical_events.where(
    clinical_events.snomedct_code.is_in(hypertension_codelist)
).where(
    clinical_events.date <= index_date
).exists_for_patient()

htn_date = clinical_events.where(
    clinical_events.snomedct_code.is_in(hypertension_codelist)
).where(
    clinical_events.date <= index_date
).sort_by(clinical_events.date).first_for_patient().date

# --- Chronic Kidney Disease (PH22) ---
has_ckd = clinical_events.where(
    clinical_events.snomedct_code.is_in(ckd_codelist)
).where(
    clinical_events.date <= index_date
).exists_for_patient()

ckd_date = clinical_events.where(
    clinical_events.snomedct_code.is_in(ckd_codelist)
).where(
    clinical_events.date <= index_date
).sort_by(clinical_events.date).first_for_patient().date

# CKD stage (if available)
ckd_stage = case(
    when(clinical_events.where(
        clinical_events.snomedct_code.is_in(["433144002"])  # CKD stage 3
    ).where(clinical_events.date <= index_date).exists_for_patient()).then("Stage_3"),
    when(clinical_events.where(
        clinical_events.snomedct_code.is_in(["709044004", "90688005"])  # CKD, CRF
    ).where(clinical_events.date <= index_date).exists_for_patient()).then("Other_CKD"),
    otherwise="No_CKD"
)

# --- Diabetes (PH24) ---
has_diabetes = clinical_events.where(
    clinical_events.snomedct_code.is_in(diabetes_codelist)
).where(
    clinical_events.date <= index_date
).exists_for_patient()

diabetes_date = clinical_events.where(
    clinical_events.snomedct_code.is_in(diabetes_codelist)
).where(
    clinical_events.date <= index_date
).sort_by(clinical_events.date).first_for_patient().date

# Diabetes type
diabetes_type = case(
    when(clinical_events.where(
        clinical_events.snomedct_code.is_in(["44054006", "237599002"])  # T2DM
    ).where(clinical_events.date <= index_date).exists_for_patient()).then("T2DM"),
    when(clinical_events.where(
        clinical_events.snomedct_code.is_in(["230572002", "49455004"])  # Diabetic neuropathy
    ).where(clinical_events.date <= index_date).exists_for_patient()).then("T2DM_complications"),
    otherwise="No_Diabetes"
)

# ============================================================
# COMORBIDITY INDICES
# ============================================================

# Charlson Comorbidity Index components
comorbidities = {
    "mi": has_mi,
    "chf": has_hf,
    "pvd": clinical_events.where(
        clinical_events.snomedct_code.is_in(["G73..00"])  # Peripheral vascular disease
    ).where(clinical_events.date <= index_date).exists_for_patient(),
    "cerebrovascular": clinical_events.where(
        clinical_events.snomedct_code.is_in(["G6...00"])  # Cerebrovascular disease
    ).where(clinical_events.date <= index_date).exists_for_patient(),
    "dementia": clinical_events.where(
        clinical_events.snomedct_code.is_in(["Eu0..00", "Eu1..00", "Eu2..00"])  # Dementia
    ).where(clinical_events.date <= index_date).exists_for_patient(),
    "copd": clinical_events.where(
        clinical_events.snomedct_code.is_in(["H3...00"])  # COPD
    ).where(clinical_events.date <= index_date).exists_for_patient(),
    "rheumatic": clinical_events.where(
        clinical_events.snomedct_code.is_in(["N0...00"])  # Rheumatic disease
    ).where(clinical_events.date <= index_date).exists_for_patient(),
    "peptic_ulcer": clinical_events.where(
        clinical_events.snomedct_code.is_in(["J1...00"])  # Peptic ulcer
    ).where(clinical_events.date <= index_date).exists_for_patient(),
    "liver_mild": clinical_events.where(
        clinical_events.snomedct_code.is_in(["J61..00"])  # Chronic liver disease
    ).where(clinical_events.date <= index_date).exists_for_patient(),
    "diabetes": has_diabetes,
    "diabetes_complications": clinical_events.where(
        clinical_events.snomedct_code.is_in(["230572002", "49455004"])
    ).where(clinical_events.date <= index_date).exists_for_patient(),
    "ckd": has_ckd,
    "cancer": clinical_events.where(
        clinical_events.snomedct_code.is_in(["B...00"])  # Malignant neoplasm
    ).where(clinical_events.date <= index_date).exists_for_patient(),
    "metastatic_cancer": clinical_events.where(
        clinical_events.snomedct_code.is_in(["B...10"])  # Metastatic cancer
    ).where(clinical_events.date <= index_date).exists_for_patient(),
    "liver_severe": clinical_events.where(
        clinical_events.snomedct_code.is_in(["J615.00"])  # Liver failure
    ).where(clinical_events.date <= index_date).exists_for_patient(),
    "hiv": clinical_events.where(
        clinical_events.snomedct_code.is_in(["B18..00"])  # HIV
    ).where(clinical_events.date <= index_date).exists_for_patient(),
}

# Calculate Charlson score
charlson_score = sum(
    1 * (comorbidities["mi"] | comorbidities["chf"] | comorbidities["pvd"] | 
         comorbidities["cerebrovascular"] | comorbidities["dementia"] | 
         comorbidities["copd"] | comorbidities["rheumatic"] | comorbidities["peptic_ulcer"] | 
         comorbidities["liver_mild"] | comorbidities["diabetes"]),
    2 * (comorbidities["diabetes_complications"] | comorbidities["ckd"] | 
         comorbidities["cancer"] | comorbidities["liver_severe"]),
    3 * comorbidities["metastatic_cancer"],
    6 * comorbidities["hiv"]
)

# ============================================================
# DEMOGRAPHICS (BHF DSC Harmonised Demographics Table)
# ============================================================

# Age at index
dataset.age_at_index = age_at_index

# Age groups
dataset.age_group = case(
    when(age_at_index < 40).then("18-39"),
    when(age_at_index < 50).then("40-49"),
    when(age_at_index < 60).then("50-59"),
    when(age_at_index < 70).then("60-69"),
    when(age_at_index < 80).then("70-79"),
    otherwise="80+"
)

# Sex
dataset.sex = sex

# Ethnicity (from clinical events or patient record)
ethnicity = clinical_events.where(
    clinical_events.snomedct_code.is_in([
        "224100000000", "224110000000", "224120000000",  # White
        "224130000000", "224140000000", "224150000000",  # Mixed
        "224160000000", "224170000000", "224180000000",  # Asian
        "224190000000", "224200000000", "224210000000",  # Black
        "224220000000", "224230000000", "224240000000",  # Other
    ])
).sort_by(clinical_events.date).last_for_patient().snomedct_code

dataset.ethnicity = case(
    when(ethnicity.is_in(["224100000000", "224110000000", "224120000000"])).then("White"),
    when(ethnicity.is_in(["224130000000", "224140000000", "224150000000"])).then("Mixed"),
    when(ethnicity.is_in(["224160000000", "224170000000", "224180000000"])).then("Asian"),
    when(ethnicity.is_in(["224190000000", "224200000000", "224210000000"])).then("Black"),
    when(ethnicity.is_in(["224220000000", "224230000000", "224240000000"])).then("Other"),
    otherwise="Unknown"
)

# Deprivation (IMD quintile from address)
imd = addresses.for_patient_on(index_date).imd_quintile
dataset.imd_quintile = imd

# Region
region = addresses.for_patient_on(index_date).region
dataset.region = region

# Rural/urban classification
dataset.rural_urban = addresses.for_patient_on(index_date).rural_urban_classification

# ============================================================
# COHORT FLAGS
# ============================================================

dataset.has_cvd = has_cvd
dataset.cvd_date = cvd_date
dataset.has_mi = has_mi
dataset.mi_date = mi_date
dataset.has_hf = has_hf
dataset.hf_date = hf_date
dataset.hf_type = hf_type
dataset.has_htn = has_htn
dataset.htn_date = htn_date
dataset.has_ckd = has_ckd
dataset.ckd_date = ckd_date
dataset.ckd_stage = ckd_stage
dataset.has_diabetes = has_diabetes
dataset.diabetes_date = diabetes_date
dataset.diabetes_type = diabetes_type
dataset.charlson_score = charlson_score

# Cardiovascular-renal-metabolic (CRM) multimorbidity
dataset.crm_multimorbidity = (
    (has_cvd.cast(int) + has_hf.cast(int) + has_htn.cast(int) + 
     has_ckd.cast(int) + has_diabetes.cast(int)) >= 2
)

# Export cohort
dataset.configure_dummy_data(population_size=10000)
```

## analysis/dataset_definition.py
```python
"""
Full dataset definition with medications, biomarkers, prior events
Aligns with BHF DSC data curation services: creating cohorts, exposures, outcomes, covariates
"""

from ehrql import create_dataset, case, when, minimum_of, maximum_of, days_between
from ehrql.tables.tpp import (
    patients, clinical_events, medications, practice_registrations,
    hospital_admissions, hospital_diagnoses, hospital_procedures,
    ons_deaths, addresses, apcs
)
from analysis.codelists import (
    cvd_codelist, mi_codelist, heart_failure_codelist,
    hypertension_codelist, ckd_codelist, diabetes_codelist,
    ace_inhibitors_codelist, arbs_codelist, beta_blockers_codelist,
    statins_codelist, anticoagulants_codelist, antiplatelets_codelist,
    lpa_testing_codelist, lipid_profile_codelist, renal_function_codelist,
    bp_systolic_codelist, bp_diastolic_codelist, bmi_codelist, heart_rate_codelist
)

# Import cohort definition
from analysis.cohort_definition import (
    dataset, index_date, study_start, study_end,
    has_cvd, cvd_date, has_mi, mi_date, has_hf, hf_date, hf_type,
    has_htn, htn_date, has_ckd, ckd_date, ckd_stage,
    has_diabetes, diabetes_date, diabetes_type,
    charlson_score, age_at_index, sex, ethnicity, imd_quintile, region
)

# ============================================================
# MEDICATION EXPOSURES (at index date and prior)
# ============================================================

# Define lookback periods
lookback_6m = index_date - days(180)
lookback_1y = index_date - days(365)
lookback_5y = index_date - days(1825)

# --- Current medications at index (issued within 6 months prior) ---
def current_medication(codelist, name):
    """Check if medication issued in 6 months before index"""
    return medications.where(
        medications.dmd_code.is_in(codelist)
    ).where(
        medications.date >= lookback_6m
    ).where(
        medications.date <= index_date
    ).exists_for_patient()

# --- Prior medication history (ever before index) ---
def prior_medication(codelist, name):
    """Check if medication ever issued before index"""
    return medications.where(
        medications.dmd_code.is_in(codelist)
    ).where(
        medications.date < index_date
    ).exists_for_patient()

# --- Medication counts ---
def medication_count(codelist, name, start_date, end_date):
    """Count medication issues in period"""
    return medications.where(
        medications.dmd_code.is_in(codelist)
    ).where(
        medications.date >= start_date
    ).where(
        medications.date <= end_date
    ).count_for_patient()

# Current cardiovascular medications
dataset.current_acei = current_medication(ace_inhibitors_codelist, "acei")
dataset.current_arb = current_medication(arbs_codelist, "arb")
dataset.current_bb = current_medication(beta_blockers_codelist, "bb")
dataset.current_statin = current_medication(statins_codelist, "statin")
dataset.current_anticoag = current_medication(anticoagulants_codelist, "anticoag")
dataset.current_antiplatelet = current_medication(antiplatelets_codelist, "antiplatelet")

# Prior cardiovascular medications (ever)
dataset.prior_acei = prior_medication(ace_inhibitors_codelist, "acei")
dataset.prior_arb = prior_medication(arbs_codelist, "arb")
dataset.prior_bb = prior_medication(beta_blockers_codelist, "bb")
dataset.prior_statin = prior_medication(statins_codelist, "statin")
dataset.prior_anticoag = prior_medication(anticoagulants_codelist, "anticoag")
dataset.prior_antiplatelet = prior_medication(antiplatelets_codelist, "antiplatelet")

# Medication counts in year before index
dataset.acei_count_1y = medication_count(ace_inhibitors_codelist, "acei", lookback_1y, index_date)
dataset.arb_count_1y = medication_count(arbs_codelist, "arb", lookback_1y, index_date)
dataset.bb_count_1y = medication_count(beta_blockers_codelist, "bb", lookback_1y, index_date)
dataset.statin_count_1y = medication_count(statins_codelist, "statin", lookback_1y, index_date)

# Polypharmacy indicator
cv_med_count = (
    dataset.current_acei.cast(int) + dataset.current_arb.cast(int) + 
    dataset.current_bb.cast(int) + dataset.current_statin.cast(int) + 
    dataset.current_anticoag.cast(int) + dataset.current_antiplatelet.cast(int)
)
dataset.cv_polypharmacy = cv_med_count >= 4

# ============================================================
# BIOMARKER MEASUREMENTS (closest to index date)
# ============================================================

def latest_measurement(codelist, name, lookback_days=365):
    """Get latest measurement value before index date"""
    start = index_date - days(lookback_days)
    return clinical_events.where(
        clinical_events.snomedct_code.is_in(codelist)
    ).where(
        clinical_events.date >= start
    ).where(
        clinical_events.date <= index_date
    ).sort_by(clinical_events.date).last_for_patient().numeric_value

def measurement_count(codelist, name, lookback_days=365):
    """Count measurements in period"""
    start = index_date - days(lookback_days)
    return clinical_events.where(
        clinical_events.snomedct_code.is_in(codelist)
    ).where(
        clinical_events.date >= start
    ).where(
        clinical_events.date <= index_date
    ).count_for_patient()

# Lipoprotein(a) - key for dataset 1906
dataset.lpa_value = latest_measurement(lpa_testing_codelist, "lpa", 730)
dataset.lpa_tested = dataset.lpa_value.is_not_null()
dataset.lpa_count = measurement_count(lpa_testing_codelist, "lpa", 730)

# Lipid profile
dataset.total_cholesterol = latest_measurement(lipid_profile_codelist, "total_chol", 365)
dataset.hdl_cholesterol = latest_measurement(lipid_profile_codelist, "hdl", 365)
dataset.ldl_cholesterol = latest_measurement(lipid_profile_codelist, "ldl", 365)
dataset.triglycerides = latest_measurement(lipid_profile_codelist, "trig", 365)

# Renal function
dataset.egfr = latest_measurement(renal_function_codelist, "egfr", 365)
dataset.creatinine = latest_measurement(renal_function_codelist, "creat", 365)
dataset.ckd_epi = case(
    when(dataset.egfr >= 90).then("G1"),
    when(dataset.egfr >= 60).then("G2"),
    when(dataset.egfr >= 45).then("G3a"),
    when(dataset.egfr >= 30).then("G3b"),
    when(dataset.egfr >= 15).then("G4"),
    when(dataset.egfr < 15).then("G5"),
    otherwise="Unknown"
)

# Blood Pressure (PH16)
dataset.sbp = latest_measurement(bp_systolic_codelist, "sbp", 365)
dataset.dbp = latest_measurement(bp_diastolic_codelist, "dbp", 365)

# BP categories
dataset.bp_category = case(
    when((dataset.sbp < 120) & (dataset.dbp < 80)).then("Normal"),
    when((dataset.sbp >= 120) & (dataset.sbp < 130) & (dataset.dbp < 80)).then("Elevated"),
    when((dataset.sbp >= 130) & (dataset.sbp < 140) | (dataset.dbp >= 80) & (dataset.dbp < 90)).then("Stage_1_HTN"),
    when((dataset.sbp >= 140) | (dataset.dbp >= 90)).then("Stage_2_HTN"),
    otherwise="Unknown"
)

# BMI (PH17)
dataset.bmi = latest_measurement(bmi_codelist, "bmi", 365)
dataset.bmi_category = case(
    when(dataset.bmi < 18.5).then("Underweight"),
    when(dataset.bmi < 25).then("Normal"),
    when(dataset.bmi < 30).then("Overweight"),
    when(dataset.bmi < 35).then("Obese_I"),
    when(dataset.bmi < 40).then("Obese_II"),
    when(dataset.bmi >= 40).then("Obese_III"),
    otherwise="Unknown"
)

# Heart Rate (PH10)
dataset.heart_rate = latest_measurement(heart_rate_codelist, "hr", 365)

# ============================================================
# PRIOR CARDIOVASCULAR EVENTS (Hospital admissions)
# ============================================================

# Prior MI (hospital diagnosis)
prior_mi_admission = hospital_admissions.where(
    hospital_diagnoses.icd10_code.is_in(["I21", "I22", "I23", "I24", "I25.2"])
).where(
    hospital_admissions.admission_date < index_date
).exists_for_patient()

dataset.prior_mi_admission = prior_mi_admission

# Prior HF admission
prior_hf_admission = hospital_admissions.where(
    hospital_diagnoses.icd10_code.is_in(["I50", "I11.0", "I13.0", "I13.2"])
).where(
    hospital_admissions.admission_date < index_date
).exists_for_patient()

dataset.prior_hf_admission = prior_hf_admission

# Prior stroke/TIA
prior_stroke = hospital_admissions.where(
    hospital_diagnoses.icd10_code.is_in(["I60", "I61", "I62", "I63", "I64", "G45"])
).where(
    hospital_admissions.admission_date < index_date
).exists_for_patient()

dataset.prior_stroke = prior_stroke

# Prior revascularization (PCI/CABG)
prior_pci = hospital_procedures.where(
    hospital_procedures.opcs4_code.is_in(["K49", "K50", "K75"])
).where(
    hospital_procedures.date < index_date
).exists_for_patient()

dataset.prior_pci = prior_pci

prior_cabg = hospital_procedures.where(
    hospital_procedures.opcs4_code.is_in(["K40", "K41", "K42", "K43", "K44", "K45", "K46"])
).where(
    hospital_procedures.date < index_date
).exists_for_patient()

dataset.prior_cabg = prior_cabg

# Prior hospitalization count (all-cause, 1 year)
prior_admissions_1y = hospital_admissions.where(
    hospital_admissions.admission_date >= lookback_1y
).where(
    hospital_admissions.admission_date < index_date
).count_for_patient()

dataset.prior_admissions_1y = prior_admissions_1y

# ============================================================
# OUTCOMES (Post-index events)
# ============================================================

# Follow-up end (earliest of: death, deregistration, study end)
followup_end = minimum_of(
    patients.date_of_death,
    practice_registrations.where(
        practice_registrations.start_date <= index_date
    ).sort_by(practice_registrations.end_date).last_for_patient().end_date,
    study_end
)

# Time to follow-up
dataset.followup_days = days_between(index_date, followup_end)

# --- Primary composite outcome: MACE ---
# CV death, MI, stroke, HF hospitalization
cv_death = ons_deaths.where(
    ons_deaths.underlying_cause_of_death.is_in(["I20", "I21", "I22", "I23", "I24", "I25", "I50", "I60", "I61", "I62", "I63", "I64"])
).where(
    ons_deaths.date > index_date
).where(
    ons_deaths.date <= followup_end
).exists_for_patient()

mi_event = hospital_admissions.where(
    hospital_diagnoses.icd10_code.is_in(["I21", "I22"])
).where(
    hospital_admissions.admission_date > index_date
).where(
    hospital_admissions.admission_date <= followup_end
).exists_for_patient()

stroke_event = hospital_admissions.where(
    hospital_diagnoses.icd10_code.is_in(["I60", "I61", "I62", "I63", "I64"])
).where(
    hospital_admissions.admission_date > index_date
).where(
    hospital_admissions.admission_date <= followup_end
).exists_for_patient()

hf_hosp = hospital_admissions.where(
    hospital_diagnoses.icd10_code.is_in(["I50", "I11.0", "I13.0", "I13.2"])
).where(
    hospital_admissions.admission_date > index_date
).where(
    hospital_admissions.admission_date <= followup_end
).exists_for_patient()

dataset.mace = cv_death | mi_event | stroke_event | hf_hosp
dataset.mace_date = minimum_of(
    ons_deaths.where(ons_deaths.underlying_cause_of_death.is_in(["I20", "I21", "I22", "I23", "I24", "I25", "I50", "I60", "I61", "I62", "I63", "I64"])).where(ons_deaths.date > index_date).sort_by(ons_deaths.date).first_for_patient().date,
    hospital_admissions.where(hospital_diagnoses.icd10_code.is_in(["I21", "I22"])).where(hospital_admissions.admission_date > index_date).sort_by(hospital_admissions.admission_date).first_for_patient().admission_date,
    hospital_admissions.where(hospital_diagnoses.icd10_code.is_in(["I60", "I61", "I62", "I63", "I64"])).where(hospital_admissions.admission_date > index_date).sort_by(hospital_admissions.admission_date).first_for_patient().admission_date,
    hospital_admissions.where(hospital_diagnoses.icd10_code.is_in(["I50", "I11.0", "I13.0", "I13.2"])).where(hospital_admissions.admission_date > index_date).sort_by(hospital_admissions.admission_date).first_for_patient().admission_date
)

# --- Individual outcomes ---
dataset.cv_death = cv_death
dataset.mi_event = mi_event
dataset.stroke_event = stroke_event
dataset.hf_hospitalization = hf_hosp

# All-cause mortality
dataset.all_cause_death = ons_deaths.where(
    ons_deaths.date > index_date
).where(
    ons_deaths.date <= followup_end
).exists_for_patient()

dataset.death_date = ons_deaths.where(
    ons_deaths.date > index_date
).sort_by(ons_deaths.date).first_for_patient().date

# ============================================================
# COVARIATES FOR ADJUSTMENT
# ============================================================

# Smoking status (most recent)
smoking = clinical_events.where(
    clinical_events.snomedct_code.is_in([
        "266919005", "266920001", "266921002", "266922009",  # Current
        "8517006", "266927004", "266928009",  # Former
        "266927004", "266928009",  # Never
    ])
).sort_by(clinical_events.date).last_for_patient().snomedct_code

dataset.smoking_status = case(
    when(smoking.is_in(["266919005", "266920001", "266921002", "266922009"])).then("Current"),
    when(smoking.is_in(["8517006", "266927004", "266928009"])).then("Former"),
    when(smoking.is_in(["266927004", "266928009"])).then("Never"),
    otherwise="Unknown"
)

# Alcohol consumption (PH9)
alcohol = clinical_events.where(
    clinical_events.snomedct_code.is_in([
        "160621000000100", "160622000000100",  # Non-drinker
        "160623000000100", "160624000000100",  # Ex-drinker
        "160625000000100", "160626000000100",  # Current drinker
    ])
).sort_by(clinical_events.date).last_for_patient().snomedct_code

dataset.alcohol_status = case(
    when(alcohol.is_in(["160621000000100", "160622000000100"])).then("Never"),
    when(alcohol.is_in(["160623000000100", "160624000000100"])).then("Former"),
    when(alcohol.is_in(["160625000000100", "160626000000100"])).then("Current"),
    otherwise="Unknown"
)

# ============================================================
# EXPORT DATASET
# ============================================================

dataset.configure_dummy_data(population_size=10000)
```

## analysis/variables.py
```python
"""
Variable definitions for analysis
Derived variables, risk scores, and analysis-ready variables
"""

from ehrql import case, when
from analysis.dataset_definition import dataset

# ============================================================
# RISK SCORES
# ============================================================

# QRISK3 variables (if available)
# Note: Full QRISK3 requires additional variables not in core dataset

# CHA2DS2-VASc for AF patients
dataset.chads2vasc = (
    (dataset.age_at_index >= 75).cast(int) * 2 +
    (dataset.age_at_index >= 65).cast(int) * 1 +
    dataset.has_htn.cast(int) * 1 +
    dataset.has_diabetes.cast(int) * 1 +
    dataset.prior_stroke.cast(int) * 2 +
    dataset.has_hf.cast(int) * 1 +
    dataset.has_cvd.cast(int) * 1 +
    (dataset.sex == "female").cast(int) * 1
)

# HAS-BLED for bleeding risk
dataset.hasbled = (
    dataset.has_htn.cast(int) * 1 +
    (dataset.egfr < 30).cast(int) * 1 +
    (dataset.has_liver_disease).cast(int) * 1 +
    dataset.prior_stroke.cast(int) * 1 +
    (dataset.age_at_index >= 65).cast(int) * 1 +
    dataset.current_anticoag.cast(int) * 1 +
    (dataset.alcohol_status == "Current").cast(int) * 1
)

# ============================================================
# CARDIOVASCULAR-RENAL-METABOLIC (CRM) PROFILES
# ============================================================

# CRM clusters based on multimorbidity patterns
dataset.crm_profile = case(
    when(dataset.has_cvd & dataset.has_hf & dataset.has_ckd & dataset.has_diabetes).then("CVD+HF+CKD+DM"),
    when(dataset.has_cvd & dataset.has_hf & dataset.has_ckd).then("CVD+HF+CKD"),
    when(dataset.has_cvd & dataset.has_hf & dataset.has_diabetes).then("CVD+HF+DM"),
    when(dataset.has_cvd & dataset.has_ckd & dataset.has_diabetes).then("CVD+CKD+DM"),
    when(dataset.has_hf & dataset.has_ckd & dataset.has_diabetes).then("HF+CKD+DM"),
    when(dataset.has_cvd & dataset.has_hf).then("CVD+HF"),
    when(dataset.has_cvd & dataset.has_ckd).then("CVD+CKD"),
    when(dataset.has_cvd & dataset.has_diabetes).then("CVD+DM"),
    when(dataset.has_hf & dataset.has_ckd).then("HF+CKD"),
    when(dataset.has_hf & dataset.has_diabetes).then("HF+DM"),
    when(dataset.has_ckd & dataset.has_diabetes).then("CKD+DM"),
    when(dataset.has_cvd).then("CVD_only"),
    when(dataset.has_hf).then("HF_only"),
    when(dataset.has_ckd).then("CKD_only"),
    when(dataset.has_diabetes).then("DM_only"),
    otherwise="No_CRM"
)

# ============================================================
# TREATMENT PATTERNS
# ============================================================

# Guideline-directed medical therapy (GDMT) for HF
dataset.gdmt_hf = (
    (dataset.current_acei | dataset.current_arb).cast(int) +
    dataset.current_bb.cast(int) +
    dataset.current_statin.cast(int)
)

dataset.gdmt_complete = dataset.gdmt_hf >= 3

# Secondary prevention medications post-MI
dataset.secondary_prevention_mi = (
    dataset.current_antiplatelet.cast(int) +
    dataset.current_statin.cast(int) +
    (dataset.current_acei | dataset.current_arb).cast(int) +
    dataset.current_bb.cast(int)
)

dataset.secondary_prevention_complete = dataset.secondary_prevention_mi >= 4

# ============================================================
# Lp(a) SPECIFIC VARIABLES (for dataset 1906 alignment)
# ============================================================

# Lp(a) risk categories (based on ESC/EAS guidelines)
dataset.lpa_risk = case(
    when(dataset.lpa_value < 30).then("Low"),
    when(dataset.lpa_value < 50).then("Intermediate"),
    when(dataset.lpa_value < 100).then("High"),
    when(dataset.lpa_value < 180).then("Very_High"),
    when(dataset.lpa_value >= 180).then("Extreme"),
    otherwise="Not_Tested"
)

# Lp(a) testing indicator (key for dataset 1906 research question)
dataset.lpa_tested_ever = clinical_events.where(
    clinical_events.snomedct_code.is_in(lpa_testing_codelist)
).where(
    clinical_events.date <= index_date
).exists_for_patient()

# ============================================================
# TIME-VARYING COVARIATES (for landmark analysis)
# ============================================================

# Medication changes in first year
dataset.acei_started_1y = (
    ~dataset.prior_acei & dataset.current_acei
)
dataset.arb_started_1y = (
    ~dataset.prior_arb & dataset.current_arb
)
dataset.statin_started_1y = (
    ~dataset.prior_statin & dataset.current_statin
)

# ============================================================
# EXPORT
# ============================================================

# All variables are attached to dataset object
# Access via dataset.variable_name in analysis scripts
```

## analysis/measures.py
```python
"""
Measures for reporting and monitoring
Aligns with BHF DSC Population Data Dashboard metrics
"""

from ehrql import create_measures, months_interval
from analysis.dataset_definition import dataset

measures = create_measures()

# ============================================================
# POPULATION MEASURES
# ============================================================

# Total population
measures.define_measure(
    name="total_population",
    numerator=dataset.population,
    denominator=dataset.population,
    group_by={"age_group": dataset.age_group, "sex": dataset.sex},
    intervals=months_interval(start="2019-01-01", end="2026-12-31", months=12)
)

# CVD prevalence
measures.define_measure(
    name="cvd_prevalence",
    numerator=dataset.has_cvd,
    denominator=dataset.population,
    group_by={"age_group": dataset.age_group, "sex": dataset.sex, "imd_quintile": dataset.imd_quintile},
    intervals=months_interval(start="2019-01-01", end="2026-12-31", months=12)
)

# HF prevalence
measures.define_measure(
    name="hf_prevalence",
    numerator=dataset.has_hf,
    denominator=dataset.population,
    group_by={"age_group": dataset.age_group, "sex": dataset.sex, "hf_type": dataset.hf_type},
    intervals=months_interval(start="2019-01-01", end="2026-12-31", months=12)
)

# ============================================================
# MEDICATION MEASURES
# ============================================================

# Statin prescribing in CVD
measures.define_measure(
    name="statin_in_cvd",
    numerator=dataset.current_statin & dataset.has_cvd,
    denominator=dataset.has_cvd,
    group_by={"age_group": dataset.age_group, "sex": dataset.sex},
    intervals=months_interval(start="2019-01-01", end="2026-12-31", months=12)
)

# ACEi/ARB in HF
measures.define_measure(
    name="acei_arb_in_hf",
    numerator=(dataset.current_acei | dataset.current_arb) & dataset.has_hf,
    denominator=dataset.has_hf,
    group_by={"hf_type": dataset.hf_type},
    intervals=months_interval(start="2019-01-01", end="2026-12-31", months=12)
)

# Beta-blocker in HF
measures.define_measure(
    name="bb_in_hf",
    numerator=dataset.current_bb & dataset.has_hf,
    denominator=dataset.has_hf,
    group_by={"hf_type": dataset.hf_type},
    intervals=months_interval(start="2019-01-01", end="2026-12-31", months=12)
)

# GDMT completion in HFrEF
measures.define_measure(
    name="gdmt_complete_hfref",
    numerator=dataset.gdmt_complete & (dataset.hf_type == "HFrEF"),
    denominator=dataset.hf_type == "HFrEF",
    group_by={"age_group": dataset.age_group},
    intervals=months_interval(start="2019-01-01", end="2026-12-31", months=12)
)

# ============================================================
# BIOMARKER TESTING MEASURES
# ============================================================

# Lp(a) testing rate (key for dataset 1906)
measures.define_measure(
    name="lpa_testing_rate",
    numerator=dataset.lpa_tested_ever & dataset.has_cvd,
    denominator=dataset.has_cvd,
    group_by={"age_group": dataset.age_group, "sex": dataset.sex, "imd_quintile": dataset.imd_quintile},
    intervals=months_interval(start="2019-01-01", end="2026-12-31", months=12)
)

# Lp(a) testing by CVD subtype
measures.define_measure(
    name="lpa_testing_by_cvd_type",
    numerator=dataset.lpa_tested_ever,
    denominator=dataset.population,
    group_by={
        "has_mi": dataset.has_mi,
        "has_hf": dataset.has_hf,
        "has_ckd": dataset.has_ckd,
        "has_diabetes": dataset.has_diabetes
    },
    intervals=months_interval(start="2019-01-01", end="2026-12-31", months=12)
)

# ============================================================
# OUTCOME MEASURES
# ============================================================

# MACE incidence rate
measures.define_measure(
    name="mace_incidence",
    numerator=dataset.mace,
    denominator=dataset.population,
    group_by={"crm_profile": dataset.crm_profile},
    intervals=months_interval(start="2019-01-01", end="2026-12-31", months=12)
)

# All-cause mortality
measures.define_measure(
    name="all_cause_mortality",
    numerator=dataset.all_cause_death,
    denominator=dataset.population,
    group_by={"age_group": dataset.age_group, "sex": dataset.sex},
    intervals=months_interval(start="2019-01-01", end="2026-12-31", months=12)
)

# CV mortality
measures.define_measure(
    name="cv_mortality",
    numerator=dataset.cv_death,
    denominator=dataset.population,
    group_by={"crm_profile": dataset.crm_profile},
    intervals=months_interval(start="2019-01-01", end="2026-12-31", months=12)
)

# Hospitalization rates
measures.define_measure(
    name="hf_hospitalization_rate",
    numerator=dataset.hf_hospitalization,
    denominator=dataset.population,
    group_by={"hf_type": dataset.hf_type},
    intervals=months_interval(start="2019-01-01", end="2026-12-31", months=12)
)

# ============================================================
# HEALTHCARE UTILIZATION (HCRU) - aligns with dataset 1906
# ============================================================

# Prior admissions
measures.define_measure(
    name="mean_prior_admissions",
    numerator=dataset.prior_admissions_1y,
    denominator=dataset.population,
    group_by={"crm_profile": dataset.crm_profile},
    intervals=months_interval(start="2019-01-01", end="2026-12-31", months=12)
)

# ============================================================
# EQUITY MEASURES
# ============================================================

# CVD prevalence by IMD
measures.define_measure(
    name="cvd_by_imd",
    numerator=dataset.has_cvd,
    denominator=dataset.population,
    group_by={"imd_quintile": dataset.imd_quintile, "ethnicity": dataset.ethnicity},
    intervals=months_interval(start="2019-01-01", end="2026-12-31", months=12)
)

# Medication access by IMD
measures.define_measure(
    name="statin_by_imd",
    numerator=dataset.current_statin & dataset.has_cvd,
    denominator=dataset.has_cvd,
    group_by={"imd_quintile": dataset.imd_quintile},
    intervals=months_interval(start="2019-01-01", end="2026-12-31", months=12)
)

# Lp(a) testing equity
measures.define_measure(
    name="lpa_testing_equity",
    numerator=dataset.lpa_tested_ever & dataset.has_cvd,
    denominator=dataset.has_cvd,
    group_by={"imd_quintile": dataset.imd_quintile, "ethnicity": dataset.ethnicity, "region": dataset.region},
    intervals=months_interval(start="2019-01-01", end="2026-12-31", months=12)
)
```

## analysis/main.py
```python
"""
Main analysis script
Implements cardiovascular research analyses aligned with BHF DSC priorities
"""

import pandas as pd
import numpy as np
from ehrql import create_dataset
from analysis.dataset_definition import dataset
from analysis.variables import *

# ============================================================
# ANALYSIS 1: Lp(a) TESTING PATTERNS (Dataset 1906 alignment)
# ============================================================

def analyze_lpa_testing():
    """Analyze Lp(a) testing patterns in ASCVD cohorts"""
    
    # Load dataset
    df = dataset.to_pandas()
    
    # ASCVD cohorts (from dataset 1906)
    ascvd = df[df.has_cvd]
    premature_ascvd = ascvd[ascvd.age_at_index < 55]
    recurrent_ascvd = ascvd[ascvd.prior_mi_admission | ascvd.prior_stroke]
    new_ascvd = ascvd[~(ascvd.prior_mi_admission | ascvd.prior_stroke)]
    
    results = {}
    
    for cohort_name, cohort_df in [
        ("all_ascvd", ascvd),
        ("premature_ascvd", premature_ascvd),
        ("recurrent_ascvd", recurrent_ascvd),
        ("new_ascvd", new_ascvd)
    ]:
        n = len(cohort_df)
        tested = cohort_df.lpa_tested_ever.sum()
        rate = tested / n * 100 if n > 0 else 0
        
        # By year
        yearly = cohort_df.groupby(cohort_df.cvd_date.dt.year).agg(
            n=("patient_id", "count"),
            tested=("lpa_tested_ever", "sum")
        )
        yearly["rate"] = yearly["tested"] / yearly["n"] * 100
        
        # By IMD
        imd_rates = cohort_df.groupby("imd_quintile").agg(
            n=("patient_id", "count"),
            tested=("lpa_tested_ever", "sum")
        )
        imd_rates["rate"] = imd_rates["tested"] / imd_rates["n"] * 100
        
        results[cohort_name] = {
            "n": int(n),
            "tested": int(tested),
            "rate_pct": round(rate, 1),
            "yearly": yearly.to_dict(),
            "by_imd": imd_rates.to_dict()
        }
    
    return results

# ============================================================
# ANALYSIS 2: CRM MULTIMORBIDITY OUTCOMES
# ============================================================

def analyze_crm_outcomes():
    """Analyze outcomes by cardiovascular-renal-metabolic profiles"""
    
    df = dataset.to_pandas()
    
    # Follow-up time in years
    df["followup_years"] = df["followup_days"] / 365.25
    
    results = {}
    
    for profile in df["crm_profile"].unique():
        if profile == "No_CRM":
            continue
            
        cohort = df[df.crm_profile == profile]
        n = len(cohort)
        
        if n == 0:
            continue
        
        # Incidence rates per 1000 person-years
        py = cohort["followup_years"].sum()
        
        mace_rate = cohort.mace.sum() / py * 1000 if py > 0 else 0
        mortality_rate = cohort.all_cause_death.sum() / py * 1000 if py > 0 else 0
        cv_mortality_rate = cohort.cv_death.sum() / py * 1000 if py > 0 else 0
        hf_hosp_rate = cohort.hf_hospitalization.sum() / py * 1000 if py > 0 else 0
        
        # Medication use
        statin_use = (cohort.current_statin & cohort.has_cvd).mean() * 100
        acei_arb_use = ((cohort.current_acei | cohort.current_arb) & cohort.has_hf).mean() * 100
        bb_use = (cohort.current_bb & cohort.has_hf).mean() * 100
        gdmt = cohort.gdmt_complete.mean() * 100
        
        results[profile] = {
            "n": int(n),
            "person_years": round(py, 1),
            "mace_rate_per_1000py": round(mace_rate, 1),
            "mortality_rate_per_1000py": round(mortality_rate, 1),
            "cv_mortality_rate_per_1000py": round(cv_mortality_rate, 1),
            "hf_hosp_rate_per_1000py": round(hf_hosp_rate, 1),
            "statin_use_pct": round(statin_use, 1),
            "acei_arb_use_pct": round(acei_arb_use, 1),
            "bb_use_pct": round(bb_use, 1),
            "gdmt_complete_pct": round(gdmt, 1)
        }
    
    return results

# ============================================================
# ANALYSIS 3: MEDICATION INITIATION PATTERNS
# ============================================================

def analyze_medication_initiation():
    """Analyze medication initiation after CVD diagnosis"""
    
    df = dataset.to_pandas()
    
    # New CVD diagnoses (incident cases)
    incident_cvd = df[df.has_cvd & (df.cvd_date >= "2019-01-01")]
    
    results = {}
    
    for med in ["acei", "arb", "bb", "statin", "anticoag", "antiplatelet"]:
        prior_col = f"prior_{med}"
        current_col = f"current_{med}"
        started_col = f"{med}_started_1y"
        
        if prior_col in df.columns and current_col in df.columns:
            # Among those without prior use
            eligible = incident_cvd[~incident_cvd[prior_col]]
            n_eligible = len(eligible)
            
            if n_eligible > 0:
                initiated = eligible[current_col].sum()
                rate = initiated / n_eligible * 100
                
                results[med] = {
                    "eligible": int(n_eligible),
                    "initiated": int(initiated),
                    "initiation_rate_pct": round(rate, 1)
                }
    
    return results

# ============================================================
# ANALYSIS 4: EQUITY ANALYSIS
# ============================================================

def analyze_equity():
    """Analyze equity in CVD care and outcomes"""
    
    df = dataset.to_pandas()
    
    results = {}
    
    # By IMD quintile
    for measure in ["has_cvd", "current_statin", "lpa_tested_ever", "mace", "all_cause_death"]:
        if measure in df.columns:
            equity = df.groupby("imd_quintile").agg(
                n=("patient_id", "count"),
                outcome=(measure, "sum")
            )
            equity["rate"] = equity["outcome"] / equity["n"] * 100
            results[f"{measure}_by_imd"] = equity.to_dict()
    
    # By ethnicity
    for measure in ["has_cvd", "current_statin", "lpa_tested_ever", "mace"]:
        if measure in df.columns:
            equity = df.groupby("ethnicity").agg(
                n=("patient_id", "count"),
                outcome=(measure, "sum")
            )
            equity["rate"] = equity["outcome"] / equity["n"] * 100
            results[f"{measure}_by_ethnicity"] = equity.to_dict()
    
    # By region
    for measure in ["has_cvd", "lpa_tested_ever"]:
        if measure in df.columns:
            equity = df.groupby("region").agg(
                n=("patient_id", "count"),
                outcome=(measure, "sum")
            )
            equity["rate"] = equity["outcome"] / equity["n"] * 100
            results[f"{measure}_by_region"] = equity.to_dict()
    
    return results

# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    import json
    from pathlib import Path
    
    output_dir = Path("output/results")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("Running Analysis 1: Lp(a) Testing Patterns...")
    lpa_results = analyze_lpa_testing()
    with open(output_dir / "lpa_testing_results.json", "w") as f:
        json.dump(lpa_results, f, indent=2, default=str)
    
    print("Running Analysis 2: CRM Multimorbidity Outcomes...")
    crm_results = analyze_crm_outcomes()
    with open(output_dir / "crm_outcomes.json", "w") as f:
        json.dump(crm_results, f, indent=2, default=str)
    
    print("Running Analysis 3: Medication Initiation...")
    med_results = analyze_medication_initiation()
    with open(output_dir / "medication_initiation.json", "w") as f:
        json.dump(med_results, f, indent=2, default=str)
    
    print("Running Analysis 4: Equity Analysis...")
    equity_results = analyze_equity()
    with open(output_dir / "equity_analysis.json", "w") as f:
        json.dump(equity_results, f, indent=2, default=str)
    
    print("All analyses complete!")
```

## Example Codelist Files

### codelists/cardiovascular_disease.csv
```csv
code,category,description
G3...,IHD,Ischaemic heart disease
G30..,IHD,Acute myocardial infarction
G31..,IHD,Other acute ischaemic heart disease
G32..,IHD,Old myocardial infarction
G33..,IHD,Angina pectoris
G34..,IHD,Other chronic ischaemic heart disease
G35..,IHD,Subsequent myocardial infarction
G36..,IHD,Certain current complications following acute myocardial infarction
G37..,IHD,Other forms of chronic ischaemic heart disease
G38..,IHD,Ischaemic heart disease unspecified
G5...,CVD,Other forms of heart disease
G50..,CVD,Heart failure
G51..,CVD,Complications and ill-defined descriptions of heart disease
G52..,CVD,Cardiovascular disease unspecified
G6...,CVD,Cerebrovascular disease
G7...,CVD,Peripheral vascular disease
```

### codelists/heart_failure.csv
```csv
code,category,description
42343007,CHF,Congestive heart failure (disorder)
48447003,CHF,Chronic heart failure (disorder)
10633002,Acute_HF,Acute congestive heart failure (disorder)
418304008,HFpEF,Diastolic heart failure (disorder)
426263006,HFrEF,Congestive heart failure due to left ventricular systolic dysfunction (disorder)
762150007,HFmrEF,Heart failure with mildly reduced ejection fraction (disorder)
```

### codelists/medications/ace_inhibitors.csv
```csv
code,bnf_subsection,description
334321000000100,2.5.5.1,Ramipril 1.25mg capsules
334331000000100,2.5.5.1,Ramipril 2.5mg capsules
334341000000100,2.5.5.1,Ramipril 5mg capsules
334351000000100,2.5.5.1,Ramipril 10mg capsules
334361000000100,2.5.5.1,Perindopril erbumine 2mg tablets
334371000000100,2.5.5.1,Perindopril erbumine 4mg tablets
334381000000100,2.5.5.1,Perindopril erbumine 8mg tablets
334391000000100,2.5.5.1,Lisinopril 2.5mg tablets
334401000000100,2.5.5.1,Lisinopril 5mg tablets
334411000000100,2.5.5.1,Lisinopril 10mg tablets
334421000000100,2.5.5.1,Lisinopril 20mg tablets
334431000000100,2.5.5.1,Enalapril 2.5mg tablets
334441000000100,2.5.5.1,Enalapril 5mg tablets
334451000000100,2.5.5.1,Enalapril 10mg tablets
334461000000100,2.5.5.1,Enalapril 20mg tablets
```

### codelists/biomarkers/lpa_testing.csv
```csv
code,test_type,description
1026261000000100,Lp_a,Lipoprotein (a) measurement
1026271000000100,Lp_a,Lipoprotein (a) level
1026281000000100,Lp_a,Lp(a) concentration
```

## README.md
```markdown
# OpenSAFELY Cardiovascular Research Project

## Overview
This project scaffold implements cardiovascular research aligned with BHF Data Science Centre services, using:
- HDRUK Phenotype Library computable phenotypes (PH5, PH25, PH26, PH22, PH24, PH10, PH16, PH17)
- HDRUK Gateway datasets (1906 - Lp(a) testing, 1821 - MI, 1986 - HF)
- BHF DSC curated assets (harmonised demographics, HES preparation, mortality variables)

## Research Questions
1. **Lp(a) Testing Patterns**: Annual prevalence/incidence of Lp(a) testing in ASCVD cohorts (Dataset 1906)
2. **CRM Multimorbidity**: Outcomes by cardiovascular-renal-metabolic profiles
3. **Medication Initiation**: Guideline-directed therapy initiation after CVD diagnosis
4. **Health Equity**: CVD care and outcomes by IMD, ethnicity, region

## BHF DSC Service Alignment
- ✅ Population data access (NHS England SDE, SAIL, Scotland)
- ✅ Data curation/engineering (reproducible pipelines, harmonised variables)
- ✅ Computable phenotypes/codelists (PH5, PH25, PH26, PH22, PH24)
- ✅ Curated assets (demographics, HES, mortality)
- ✅ Codelist Comparison Tool (code validation)
- ✅ PPIE support (equity analysis)

## Project Structure
```
analysis/
├── cohort_definition.py    # Population, index dates, comorbidities
├── dataset_definition.py   # Medications, biomarkers, prior events, outcomes
├── variables.py            # Derived variables, risk scores, CRM profiles
├── measures.py             # Population measures for dashboard
├── codelists.py            # All codelist imports
└── main.py                 # Analysis execution
```

## Running the Project
```bash
# Generate cohort
opensafely run generate_cohort

# Generate dataset
opensafely run generate_dataset

# Run analysis
opensafely run run_analysis

# Generate measures
opensafely run generate_measures
```

## Key Variables
- **Cohort flags**: `has_cvd`, `has_mi`, `has_hf`, `has_htn`, `has_ckd`, `has_diabetes`
- **Medications**: `current_acei`, `current_arb`, `current_bb`, `current_statin`, `current_anticoag`, `current_antiplatelet`
- **Biomarkers**: `lpa_value`, `lpa_tested`, `egfr`, `sbp`, `dbp`, `bmi`, `heart_rate`
- **Prior events**: `prior_mi_admission`, `prior_hf_admission`, `prior_stroke`, `prior_pci`, `prior_cabg`
- **Outcomes**: `mace`, `cv_death`, `mi_event`, `stroke_event`, `hf_hospitalization`, `all_cause_death`
- **CRM profiles**: `crm_profile`, `crm_multimorbidity`
- **Equity**: `imd_quintile`, `ethnicity`, `region`

## Codelist Sources
- PH5: Cardiovascular Disease (Read v2)
- PH25: Heart Failure (SNOMED CT)
- PH26: Hypertension (SNOMED CT)
- PH22: Chronic Kidney Disease (SNOMED CT)
- PH24: Diabetes (SNOMED CT)
- PH10: Heart Rate (CPRD)
- PH16: Blood Pressure (CPRD)
- PH17: BMI (CPRD)
- BNF chapters for medications
- Dataset 1906 for Lp(a) testing codes

## Outputs
- `output/results/lpa_testing_results.json`
- `output/results/crm_outcomes.json`
- `output/results/medication_initiation.json`
- `output/results/equity_analysis.json`
- `output/measures/*.csv` (for Population Data Dashboard)
```
