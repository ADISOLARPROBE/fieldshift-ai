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



## Shree



## Antima
4/11/2026 Added PRD.md 



## Tanmay



## Arshdeepp
