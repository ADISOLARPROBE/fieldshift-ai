# Contributing

## ADI




## Deb

### Responsibilities: Data Cleaning, Processing & ML Model Training

- **Data Cleaning & Dataset Preprocessing**:
  - Extracted and processed NASA POWER climate datasets, aggregating and merging daily temperature records into 8 distinct model-specific CSV files (`M1_daily_merged.csv` to `M8_daily_merged.csv` in `data/processed/Temperature/`).
  - Implemented `fieldshift_gdhy_spaced_coordinates.py` to generate 1,200 nominal GDHY 0.5-degree grid-center coordinate candidate pairs across 8 agro-climatic zones (M1–M8), ensuring global spacing ≥80 km using WGS84 (EPSG:4326).
  - Configured git data-tracking policies in `.gitignore` to prevent committing large raw/processed dataset files.

- **ML Model Architecture & Documentation**:
  - Authored comprehensive ML Model Documentation (`docs/ML_MODEL_DOCUMENTATION.md`), establishing the problem definition, target label calculation (`yield_t_ha`), candidate 18-feature schema, XGBoost regressor baseline hyperparameters, temporal/geographic validation split design, and pre-planting forecast vs retrospective hindcast policies.
  - Designed the interface between the XGBoost yield prediction model and the agronomic crop suitability/rotation engine.

- **Data Source Integration Standards**:
  - Authored `docs/NASA_DATA_SOURCES.md`, documenting integration standards, extraction policies, unit conversions, and spatial/temporal limitations for NASA POWER daily API (`T2M`, `PRECTOTCORR`, `RH2M`, `ALLSKY_SFC_SW_DWN`), ISRIC SoilGrids, India DES APY, and FAO crop calendars.

- **Repository Guidelines & Governance**:
  - Updated root `README.md` with guidelines on branch workflows, pull requests, and commit message standards.

### November 2026 — Dataset Integrity Audit & Temperature Optimization

- **Full-dataset sanity check (ERA5 soil + NASA POWER)**:
  - Audited all 16 zone files against the 1,200 planned coordinates — 8 ERA5 soil CSVs in `data/raw/soil era5/` and the 8 merged Temperature CSVs in `data/processed/Temperature/`. Verified per location: row count against 150 × 7,305 daily records, date-range span 2000-01-01 to 2019-12-31, no duplicate `id + date` rows, no internal date gaps, and no blank/NaN, non-numeric, sentinel or physically implausible values.
  - Confirmed NASA POWER coverage is complete at **1,200 / 1,200 locations** with full daily series (26 isolated blank `ALLSKY_SFC_SW_DWN` cells remain in M6/M7).
  - Identified **91 of 1,200 planned points never fetched** in the ERA5 soil download (M1: 10, M2: 6, M3: 2, M4: 20, M5: 23, M6: 8, M7: 19, M8: 3). Every fetched ERA5 location is otherwise complete, establishing the issue as a fetch-coverage gap rather than a date-pipeline defect.
  - Authored `data/processed/missing_coordinates.py`, listing the missing locations as 8 separate `[latitude, longitude]` lists (`MISSING_ERA5_SOIL_M1`–`M8`) keyed to the planned-point index, ready to feed into the soil fetch script for refetching.
  - Corrected `docs/NASA_DATA_SOURCES.md` to state actual ERA5 soil coverage instead of assuming all 1,200 points were retrieved.

- **Temperature data optimization & memory reduction**:
  - Built per-zone exploration notebooks `m1_temperature_data.ipynb` through `m4_temperature_data.ipynb` (`apps/ml-service/notebooks/`) covering schema inspection, null counts, duplicate-row verification, and correlation checks.
  - Downcast column dtypes (`float64 → float16` for `T2M`, `PRECTOTCORR`, `ALLSKY_SFC_SW_DWN`, `latitude`, `longitude`; `int64 → int16` for `year`, `month`, `day`) to shrink in-memory footprint on the 1.1-million-row zone files before ML feature engineering.
  - Moved the bulk Temperature CSVs out of git tracking (`data/processed/*` now ignored, with `fieldshift_gdhy_spaced_coordinates.py` and the missing-coordinates manifest explicitly un-ignored) so datasets are held locally only and the repository stays lightweight.

- **Environment & tooling**:
  - Populated root `requirements.txt` with the data-processing stack (`numpy`, `pandas`, `matplotlib`, `seaborn`).



## Shree



## Antima
4/11/2026 Added PRD.md 



## Tanmay



## Arshdeepp
