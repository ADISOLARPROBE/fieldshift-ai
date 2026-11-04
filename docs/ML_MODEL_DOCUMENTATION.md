# FieldShift AI — ML Model and Recommendation Engine

**Project:** FieldShift AI  
**Challenge:** NASA Space Apps Challenge 2026 — Adapting Farms with NASA Data  
**Status:** Proposed design; the trained model and evaluation results are **not yet available**  
**Last reviewed:** November 2026

> **Scope:** This file defines **what is predicted**, training data joins, crop-specific feature engineering, validation, inference, and rotation recommendations. Dataset origins, access methods, units and limitations are documented in [NASA_DATA_SOURCES.md](./NASA_DATA_SOURCES.md).

## 1. Problem definition and architecture

The goal is to help a farmer **compare feasible crop-rotation strategies**, rather than choose only the crop with the highest estimated yield.

### Predictive target

- **Primary supervised model:** `XGBRegressor` (XGBoost regression).
- **Inputs:** Candidate crop, region, crop-specific growing-season climate features, soil characteristics, and available management information.
- **Output:** `predicted_yield_t_ha` — expected crop yield in **tonnes per hectare**.
- **Ground-truth labels:** Verified historical crop yields from Indian DES agricultural statistics.

**Yield prediction is not the same as rotation recommendation.** Rotation suitability, seasonal feasibility, water considerations and soil-health tradeoffs are evaluated in a **separate agronomic rule engine**; a ranking layer combines the results according to farmer priorities.

```text
Farmer farm polygon / location + chosen planning season
                |
                v
Crop catalog + FAO/regional crop calendars
                |
                v
Per-crop growing windows + candidate rotation sequences
                |
                +----------------------------+
                |                            |
                v                            v
NASA POWER climate features       SoilGrids soil features
                |                            |
                +-------------+--------------+
                              |
                              v
                      Feature builder
                              |
                +-------------+--------------+
                |                            |
                v                            v
       XGBoost yield model          Suitability/rotation rules
                |                            |
                +-------------+--------------+
                              |
                              v
             Explainable rotation comparison and ranking
```

## 2. Sources and their ML roles

| Source | Model role | Other role |
|---|---|---|
| DES Area/Production/Yield | **Target:** historical yield in t/ha | Establish crop/regional coverage |
| NASA POWER | Crop-window climate features | Climate context and scenario inputs |
| ISRIC SoilGrids | Soil-property features | Soil suitability context |
| FAO Crop Calendar | Determines growing-season dates and derived temporal features | Prevents infeasible crop timing |
| FAO ECOCROP | Optional suitability-derived features | Environmental suitability checks |
| Curated agronomic references | Not a yield label | Previous-crop rules, water and rotation constraints |

Only predict yields for crop-region combinations for which training data and evaluation support inference. Do not train a regression model on ECOCROP requirements as though they were observed yields.

## 3. Training observation and target construction

**Unit of supervised observation:**

`state_id × district_id × agricultural_year × crop_id × season`

This may need an additional source-specific record identifier if DES publishes multiple observations for a single combination.

The target is:

```text
yield_t_ha = production_tonnes / harvested_or_reported_area_hectares
```

Verify the DES definition of area and units. Do not invent missing area, production or yield values.

### Required join workflow

1. **DES:** Standardize district/state IDs, crop names, agricultural year and season; compute/validate yield.
2. **Calendar:** Resolve the correct region, crop, season, sowing and harvest windows. Record how agricultural years crossing January are handled.
3. **NASA POWER:** Build weather aggregates for those **exact crop windows**, with the training/inference time policy specified below.
4. **SoilGrids:** Derive a documented district-level soil summary from appropriate map layers and depths. Keep field-level soil retrieval separate from district-level target interpretation.
5. **Merge:** Join on validated geography/crop/season/time identifiers, retain provenance and missingness indicators.
6. **Quality assurance:** Deduplicate true records; quarantine mismatched geographies, unknown seasons, invalid units or impossible yields.

Never expand one district-year-season yield label into hundreds of supposedly independent labeled rows by repeating the same yield for daily weather records or raster pixels.

## 4. Crop-specific feature engineering

**Why:** Rainfall in a rice growing season and rainfall in a wheat growing season are usually drawn from **different months**. They must not receive the same annual rainfall or temperature values simply because they share a district and year.

For each observation, identify `window_start` and `window_end` from the regional crop calendar. Then aggregate NASA daily values over that window.

### Candidate features (initial schema)

| Group | Feature | Definition |
|---|---|---|
| Identity | `crop_id` | Categorical crop identity |
| Geography | `state_id` | Categorical state |
| Geography | `district_id` | Categorical district |
| Timing | `season` | Kharif/Rabi/etc. as supported |
| Timing | `sowing_month` | Planting month from verified calendar |
| Timing | `growing_days` | Planned growing-window length |
| Climate | `avg_temp_c` | Mean of daily `T2M` |
| Climate | `avg_daily_max_temp_c` | Mean of daily `T2M_MAX` |
| Climate | `avg_daily_min_temp_c` | Mean of daily `T2M_MIN` |
| Climate | `total_rainfall_mm` | Sum of daily precipitation |
| Climate | `avg_humidity_pct` | Mean of daily `RH2M` |
| Climate | `avg_solar_radiation` | Mean daily `ALLSKY_SFC_SW_DWN` in source-documented units |
| Soil | `soil_ph` | Normalized soil pH |
| Soil | `sand_pct` | Sand content |
| Soil | `silt_pct` | Silt content |
| Soil | `clay_pct` | Clay content |
| Soil | `soc_g_kg` | Soil organic carbon |
| Soil | `cec_cmol_kg` | Cation exchange capacity |

This is an **18-feature candidate design**, not a fixed promise. Include irrigation or previous-crop features in the regressor **only when corresponding reliable training labels exist**. Source units and soil-depth aggregation must match training and inference.

Useful later experiments: rainfall-day counts, longest dry spell, heat-stress counts, climate anomalies, crop-stage-specific climate features and ECOCROP-derived distance-to-suitability-boundary features. Define thresholds and validate their benefit before adoption.

### Example (illustrative only)

A verified regional rice calendar might span June–October, while a wheat calendar might span November–March. For agricultural year `2022-23`, wheat's features must use records from **both 2022 and 2023** as appropriate. Real dates must come from the actual local calendar, not these examples.

## 5. Pre-planting predictions vs retrospective analysis

**This distinction is mandatory.** A model trained using weather observed at the **end** of a season cannot be described as making a reliable **before-planting** forecast from data that did not yet exist.

### A. Preferred MVP: pre-planting expected-yield model

Define a precise **prediction issue date** (e.g., immediately before the sowing window) for *every historical training record*.

Construct climate predictors using only information that would have been available then, such as:

- Previous 10 complete years of daily NASA POWER observations, aggregated to the *corresponding crop-specific calendar window*, producing a historical seasonal normal.
- Recent past climate trends or anomalies ending before the issue date.
- An actual archived pre-season forecast, if a credible archive and alignment method are available.

**No observation from after the historical prediction issue date may enter a predictor.** For an upcoming season, construct the exact same types of features at the current issue date.

This model estimates a **baseline expected yield conditional on historical climate context and other available features**, not the yield under the future season's unknown actual weather. It may have limited predictive power; evaluate that honestly.

### B. Optional research track: observed-weather hindcast model

A second XGBoost model may use **actual observed weather during completed seasons** to explain/reconstruct historical yield variation.

- Label this model **retrospective / hindcast**.
- It cannot be presented as a validated pre-planting predictor without a separate forecast-to-inference validation study.
- If used with hypothetical weather scenarios, label outputs **exploratory what-if estimates** and state that scenario calibration is uncertain.

**Do not silently train on observed seasonal weather and serve historical-normal inputs as though the two distributions were identical.** If that approach is experimentally used, benchmark the train–serve mismatch explicitly.

## 6. Training implementation

### Recommended algorithm

`xgboost.XGBRegressor` trained on structured tabular data.

Use **one shared model with crop identity encoded** as the initial design. If crop-specific errors vary significantly, compare a separate regressor per well-covered crop.

### Preprocessing contract

- Ensure all numerical columns use consistent units; preserve metadata.
- Encode `crop_id`, `state_id`, `district_id`, and `season` using a saved categorical preprocessing pipeline (e.g., `OneHotEncoder(handle_unknown='ignore')`), or a consistently configured XGBoost categorical strategy.
- Handle missing numeric features with a documented, train-fitted method and missingness checks. Do not leak test-set statistics into preprocessing.
- Reject unsupported crops/regions and invalid feature combinations before inference.
- Save the preprocessing pipeline **with** the model; never rely on hand-assembled feature ordering at serving time.

### Starting hyperparameters (tune after establishing baselines)

```python
XGBRegressor(
    objective="reg:squarederror",
    n_estimators=500,
    max_depth=5,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    tree_method="hist",
    random_state=42,
    n_jobs=-1,
)
```

These are **starting settings, not optimized results**. Use validation-based early stopping where applicable, and record the chosen hyperparameters and random seed. Try other tree counts and depths only after checking generalization.

**Repository dependency:** Add a pinned compatible `xgboost` package to `apps/ml-service/requirements.txt` when implementing this design; the current scaffold lists scikit-learn but not XGBoost.

## 7. Evaluation and leakage prevention

### Baselines

Compare XGBoost against at least:

1. Historical crop-by-district yield average calculated **from the training period only**.
2. A simple regularized linear model or comparable tabular baseline.

### Primary metrics

- **MAE** (t/ha): interpretable average absolute error.
- **RMSE** (t/ha): highlights large errors.
- **R²**, as supplementary context only.
- Per-crop and per-region breakdowns; training-label counts per group.

### Split design

- **Temporal holdout:** Train on older agricultural years; validate on later years; test on the most recent usable held-out years.
- **Geographic stress test:** Separately hold out whole districts/regions to measure out-of-region generalization.
- Keep repeated records derived from the same DES observation in the same split.
- Fit all imputers, encoders, encodings and feature selection on training data only.
- For pre-planting evaluation, reproduce the historical **as-of** feature cutoff for each record.
- Report coverage limitations. High overall R² does not prove accuracy for every crop or location.

### Uncertainty and reliability

Start with empirical validation-error summaries by crop/region; optionally estimate calibrated prediction intervals using a held-out calibration set or conformal methods. Do not display arbitrary percentages as model confidence.

Reject or warn on unsupported crops, distant extrapolation, extreme climate scenarios and missing important features. Display the model version, prediction mode and date.

## 8. Rule-based crop suitability and rotation engine

This system uses the **same environment data** as the ML model but evaluates a different question: *Is a proposed sequence feasible and reasonably suitable?*

### Inputs

- Crop-specific FAO ECOCROP requirements, verified against Indian regional guidance.
- FAO/local planting and harvest calendars.
- Available irrigation information, temperature/rainfall/soil estimates.
- Curated crop-family, previous-crop, pest/disease and rotation considerations from independently verified agronomic sources.
- Farmer priorities and available crop-cost/market-price information, where sourced.

### Pipeline

1. **Generate candidate rotations:** Include the farmer's current plan and at least two locally plausible alternatives when evidence supports them.
2. **Check hard constraints:** Missing crop support, impossible planting windows, severe incompatibility, or known resource limitations. Mark infeasible plans rather than giving them misleading numerical ranks.
3. **Assess suitability:** Temperature, water and soil constraints with transparent source-specific thresholds. Ensure **annual** ECOCROP rainfall ranges are not compared directly to a **seasonal** NASA rainfall sum.
4. **Predict supported yields:** Call the XGBoost service for each crop/season using the correct prediction mode and features. Do not extrapolate unsupported crop yields.
5. **Compare full sequences:** Evaluate timing, approximate total production, water needs, qualitative soil-health implications and potential costs/revenue only when the inputs are supported.
6. **Rank eligible candidates:** Apply normalized, documented criteria and user-adjustable weights. Keep the score separate from the model-predicted yield.
7. **Explain:** Show assumptions, rule sources, limitations, and why each alternative ranks above or below the baseline.

**Rotation caution:** Crop-family alternation or legume inclusion may be agronomically promising, but without local management information and longitudinal soil observations, do not claim a measured soil-health improvement or guaranteed profit.

### Illustrative ranking scheme

```text
For each feasible rotation:
  score =
      w_yield  * normalized_yield_indicator
    + w_water  * normalized_water_indicator
    + w_soil   * evidence_based_soil_indicator
    + w_profit * normalized_profit_indicator

Constraints:
  each weight >= 0
  weights sum to 1
  undefined indicators are displayed as unavailable, not silently set to 0
```

If a criterion is unavailable, show that fact and recalculate using only explicitly eligible criteria with the farmer informed. No default score or rule weight is a scientific certainty.

## 9. Service integration and artifact layout

The existing repository separates a Node/Express API from a Python/FastAPI ML service.

### Proposed structure

```text
apps/ml-service/
├── app/
│   ├── api/routes/predict.py
│   ├── api/schemas/prediction_schema.py
│   ├── services/preprocessing.py
│   ├── services/prediction_service.py
│   └── models/model_loader.py
├── notebooks/
│   └── model_training.ipynb
├── training/
│   ├── build_dataset.py
│   ├── train.py
│   └── evaluate.py
├── model/
│   ├── crop_yield_pipeline.joblib
│   └── model_metadata.json
└── requirements.txt
```

The `training/` scripts and saved artifacts are **proposed**, not already implemented.

### Prediction input (illustrative contract)

```json
{
  "farm_id": "farm_example",
  "crop_id": "rice",
  "season": "kharif",
  "prediction_mode": "preplant_historical_normal",
  "planting_year": 2027
}
```

The Node API should resolve the authenticated farm/location, obtain the approved climate and soil features, and send the complete validated model feature payload to the Python service. The UI must **not** be trusted to provide unverified NASA measurements or a fabricated district label.

### Prediction output (illustrative, not a real result)

```json
{
  "crop_id": "rice",
  "prediction_mode": "preplant_historical_normal",
  "predicted_yield_t_ha": 3.2,
  "model_version": "example-v0",
  "supported": true,
  "warnings": ["Regional estimate; not a validated field-specific forecast"]
}
```

The number `3.2` is a **format example only**. Never ship fabricated model responses as production predictions. Actual response schemas must include units, source vintage and meaningful failure states.

### Model metadata checklist

Store feature names/types/units, crop and region support, calendar-source version, climate issue-date policy, training date range, split design, metrics, model parameters, pipeline version and training data manifest.

## 10. MVP implementation checklist

- [ ] Audit DES yield-label coverage and choose 3–5 crops with adequate observations.
- [ ] Verify region-specific calendars and map agricultural years to actual date windows.
- [ ] Produce NASA POWER and SoilGrids features with full provenance.
- [ ] Build a **pre-planting as-of** training matrix without future-weather leakage.
- [ ] Train baseline and XGBoost models; report temporal holdout MAE/RMSE.
- [ ] Evaluate performance separately by crop and region.
- [ ] Save a single validated preprocessing + model artifact.
- [ ] Add `xgboost` to the pinned Python dependencies.
- [ ] Implement candidate rotations and documented suitability/compatibility rules.
- [ ] Compare the current rotation against at least two supported alternatives.
- [ ] Surface limitations, unavailable estimates, source references and prediction mode in the UI.

## 11. Scientific and product limitations

- The target is **district-level historical yield**, not ground-truth farm yield.
- NASA POWER and SoilGrids are gridded/model-based environmental products, not direct on-field measurements.
- A pre-planting expected-yield model trained on prior climate history cannot know the coming season's weather.
- Crop calendars and ECOCROP are references with uneven locality/coverage, not universal prescriptions.
- Irrigation, seeds, fertilizer, pests, management and market prices may be missing or inaccurate.
- Predicted yield, crop suitability and overall rotation rank are **distinct outputs**; none guarantees success.
- Do not quantify soil regeneration, water savings or profit without a defensible calculation and evidence.

## 12. References

- [Data-source definitions, endpoints, units and access limitations](./NASA_DATA_SOURCES.md)
- [NASA POWER Daily API](https://power.larc.nasa.gov/docs/services/api/temporal/daily/)
- [Government of India DES APY Reports](https://data.desagri.gov.in/website/crops-apy-report-web)
- [ISRIC SoilGrids](https://docs.isric.org/globaldata/soilgrids/)
- [FAO ECOCROP](https://www.fao.org/geospatial/data-and-tools/data-portals/ecocrop/)
- [FAO Crop Calendar](https://cropcalendar.apps.fao.org/)
- [XGBoost Python documentation](https://xgboost.readthedocs.io/en/stable/python/python_api.html)

> **Core design decision:** Use **XGBoost to estimate yields**, a **source-backed rule engine to assess suitability and rotation feasibility**, and a **transparent ranking layer** to compare crop-rotation strategies. Keep retrospective weather analysis separate from claims about predictions made before planting.
