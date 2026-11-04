# FieldShift AI — Data Sources and Integration

**Project:** FieldShift AI  
**Challenge:** NASA Space Apps Challenge 2026 — Adapting Farms with NASA Data  
**Status:** Proposed MVP data plan (not a statement that all data has been downloaded)  
**Last reviewed:** November 2026

> **Scope:** This file describes **what data we use**, where it comes from, how we access and store it, and its limitations. Feature engineering, XGBoost training, evaluation, and the rotation-ranking algorithm are documented in [ML_MODEL_DOCUMENTATION.md](./ML_MODEL_DOCUMENTATION.md).

## 1. Data-source overview

| Source | Provider | Data | Role in FieldShift AI |
|---|---|---|---|
| **Crop Area, Production & Yield (APY)** | Government of India, Directorate of Economics and Statistics (DES) | Crop, state/district, season, year, area, production and/or yield | **Historical target labels** for supervised yield prediction |
| **POWER Daily** | **NASA** | Temperature, precipitation, relative humidity, solar radiation | Historical climate features, historical normals, climate scenarios and dashboard context |
| **SoilGrids** | ISRIC — World Soil Information | Soil pH, texture fractions, organic carbon, cation exchange capacity | Regional soil-property features and suitability context |
| **ECOCROP** | FAO | Plant environmental requirements and tolerances | Suitability-rule reference; optional engineered ML features |
| **Crop Calendar** | FAO | Planting/harvest windows by crop and agroecological zone | **Crop- and region-specific season mapping** for climate aggregation and rotation scheduling |

**Only POWER is a NASA dataset in this five-source MVP.** SoilGrids, DES and FAO data complement the NASA measurements. The crop calendar and ECOCROP are **not** sources of measured historical yield.

## 2. DES — Indian Crop Area, Production & Yield

- **Report:** https://data.desagri.gov.in/website/crops-apy-report-web
- **Additional reports:** https://data.desagri.gov.in/website/crops-report-district-level-web
- **Source:** Directorate of Economics and Statistics, Department of Agriculture and Farmers Welfare, Government of India.
- **Access:** Select state, district, crop, season, years and report format in the reporting interface. Confirm export format and allowed reuse for the retrieved records; do not assume a stable public bulk-download API exists.

### Required raw fields

`state`, `district`, `crop`, `agricultural_year`, `season`, `area`, `production`, and/or `yield`, plus original units and source metadata.

**Yield target:**

```text
if production is in tonnes and area is in hectares:
    yield_tonnes_per_hectare = production_tonnes / area_hectares
```

Convert units **before** computing yield. Exclude or investigate zero-area, invalid or inconsistent records. Preserve original agricultural-year labels (for example, `2022-23`) and document how each is assigned to sowing and harvest dates.

**Granularity:** A DES district-level observation is a **district aggregate**, not a farmer-field measurement. Historical yield observations provide the supervised target; multiple NASA daily values do not create additional independent yield labels.

**Main risks:** Missing crop/district/season combinations, changing district boundaries, varying crop names, different area/production units, and absent information on irrigation, varieties and management.

## 3. NASA POWER — daily climate data

- **Website:** https://power.larc.nasa.gov/
- **Daily API documentation:** https://power.larc.nasa.gov/docs/services/api/temporal/daily/
- **Endpoint:** `https://power.larc.nasa.gov/api/temporal/daily/point`
- **Access:** Public HTTP API; use the `AG` community and document returned metadata, parameter units and missing-value conventions.

| Parameter | API code | Intended use |
|---|---|---|
| Mean 2-m air temperature | `T2M` | Temperature conditions |
| Maximum 2-m air temperature | `T2M_MAX` | Heat-exposure indicators |
| Minimum 2-m air temperature | `T2M_MIN` | Cold-exposure indicators |
| Precipitation | `PRECTOTCORR` | Rainfall totals and dry-spell context |
| Relative humidity | `RH2M` | Humidity features |
| All-sky surface shortwave radiation | `ALLSKY_SFC_SW_DWN` | Solar-energy features |

### Example request

```text
https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M,T2M_MAX,T2M_MIN,PRECTOTCORR,RH2M,ALLSKY_SFC_SW_DWN&community=AG&longitude=80.45&latitude=16.30&start=20220101&end=20221231&format=JSON
```

The coordinate is illustrative. Confirm each requested parameter is available for the selected location and dates; check the response for API errors and missing-data sentinels.

### Extraction policy

1. Match each historical yield observation to an appropriate district geometry or documented representative coordinate.
2. Retrieve daily climate records for the relevant period, including previous calendar years when a growing season spans New Year.
3. Use the **verified crop/region/season calendar** to identify the appropriate time window.
4. Cache API responses by location/grid cell, date range, parameter set, and retrieval version; do not repeatedly request nearby coordinates representing the same POWER grid cell.
5. Preserve raw data, provenance, units, coverage and retrieval timestamps.

**Critical time distinction:** Recorded weather **during** a historical crop season can support a retrospective/hindcast analysis. A prediction issued **before planting** must instead rely on information available at that time (e.g., prior-year normals, an actual pre-season forecast, or an explicitly labeled scenario). Historical observed weather is **not** a future forecast.

**Spatial limitation:** POWER data are gridded environmental estimates, not measurements taken inside an individual farm. Dataset source resolutions can vary by variable.

## 4. ISRIC SoilGrids — soil properties

- **Documentation:** https://docs.isric.org/globaldata/soilgrids/
- **Property definitions and unit conversions:** https://docs.isric.org/globaldata/soilgrids/SoilGrids_faqs_01.html
- **Google Earth Engine access:** https://docs.isric.org/globaldata/soilgrids/access_on_gee.html
- **Provider:** ISRIC — World Soil Information (**not NASA**).

SoilGrids offers modeled soil-property estimates at approximately **250 m** resolution. For the MVP, use a documented depth selection (such as the topsoil 0–30 cm, properly aggregated from depth layers) and consistent prediction statistic (e.g., mean).

| Property | Layer | Convert stored values into |
|---|---|---|
| Soil pH (water) | `phh2o` | pH = raw / 10 |
| Sand | `sand` | percent = raw / 10 |
| Silt | `silt` | percent = raw / 10 |
| Clay | `clay` | percent = raw / 10 |
| Soil organic carbon | `soc` | g/kg = raw / 10 |
| Cation exchange capacity | `cec` | cmol(c)/kg = raw / 10 |

**Access status (November 2026):** ISRIC reports that its SoilGrids REST API is temporarily paused. Use **WCS**, **WebDAV/raster extracts**, or the available **Google Earth Engine community assets** rather than relying on the REST API.

**Spatial matching:** For model training, calculate a representative **district-level** soil summary using a documented spatial aggregation procedure. For farm display, extract the relevant map-cell or polygon summary, clearly labeled as a regional estimate. These are different geographical supports; do not claim the model was trained on laboratory-confirmed farm soil tests.

**Main risks:** Spatial heterogeneity, uncertainty in modeled layers, differences between map depth and crop-root zone, and limited ability to represent year-to-year soil changes. ISRIC cautions against treating SoilGrids as a substitute for local farm-scale soil testing.

## 5. FAO ECOCROP — environmental requirements

- **Official page:** https://www.fao.org/geospatial/data-and-tools/data-portals/ecocrop/
- **Provider:** Food and Agriculture Organization of the United Nations.
- **Status:** A **legacy** database discontinued around 2015, now accessible through the FAO Global Agro-Ecological Zoning (GAEZ) environment. Confirm how each selected record can currently be exported or transcribed and record its source.

ECOCROP may provide minimum/maximum temperature, **annual** precipitation, soil pH, light, altitude and other environmental descriptors for crops.

**MVP use:** Curate verified requirements for supported crops into `crop_requirements.csv`; use them in crop suitability explanations and rules. Optionally create ML features from these requirements, but only after testing their value on held-out data.

**Important:** An ECOCROP **annual rainfall** range is **not automatically comparable** to NASA rainfall summed over a three- or four-month growing season. Record the period and interpretation of each threshold. ECOCROP neither supplies historical yield labels nor establishes whether a crop rotation improves soil health.

Validate requirements against region-specific Indian agronomic guidance wherever possible.

## 6. FAO Crop Calendar — crop and season timing

- **Tool:** https://cropcalendar.apps.fao.org/
- **Provider:** FAO.
- **Access:** Interactive crop/country/agroecological-zone calendar. Do not assume a documented bulk API for every country and crop; curate a local calendar table with source references where necessary.

Required normalized fields:

`crop_id`, `country`, `region_or_agroecological_zone`, `season`, `sowing_window_start`, `sowing_window_end`, `harvest_window_start`, `harvest_window_end`, `source`, `reviewed_at`.

**Use cases:**

- Define the crop-specific weather aggregation window when joining NASA POWER data to DES yield records.
- Derive sowing month, growing period and possible crop-sequence timing.
- Check whether rotation candidates overlap or leave sufficient transition time.

A crop grown in **November–March** crosses calendar years. Map the reported agricultural year to the correct sowing and harvesting dates; do not naïvely aggregate only January–December of the reported year.

**Coverage caveat:** FAO's calendars may be unavailable or insufficiently localized for some Indian districts, varieties or seasons. Use verified Indian agricultural-university or extension calendars as fallback, with separate provenance; never invent missing crop dates.

## 7. Shared identifiers and data handling

All extracted data must be mapped to common identifiers before model development:

| Concept | Suggested normalized field | Notes |
|---|---|---|
| Crop | `crop_id` | Maintain a versioned crop-name alias table |
| Region | `state_id`, `district_id` | Retain source names/codes and boundary versions |
| Agricultural time | `agricultural_year`, `season` | Explicitly map to planting/harvest dates |
| Geography | `latitude`, `longitude` or geometry | Record coordinate reference system and aggregation method |
| Provenance | `source`, `source_version`, `retrieved_at` | Retain metadata and access/license terms |

**Do not join data solely on a text district name** without checking the state, year/boundary definition and aliases. Exclude uncertain spatial/temporal mappings or flag them for manual review.

### Proposed file organization

```text
 data/
 ├── raw/
 │   ├── des_crop_apy.csv
 │   ├── nasa_power_daily.csv
 │   └── soilgrids_extract.csv
 ├── external/
 │   ├── nasa/
 │   ├── government/
 │   └── fao/
 │       ├── crop_requirements.csv
 │       └── crop_calendar.csv
 └── processed/
     ├── crop_yield_labels.csv
     ├── seasonal_climate_features.csv
     ├── district_soil_features.csv
     ├── crop_yield_training.csv
     └── crop_rules.csv
```

These are **proposed output filenames**, not datasets already present in Git. Store large files outside the repository and commit only small licensed samples, manifests or scripts. Follow each provider's attribution and usage terms.

### Data quality checklist

- [ ] Record official source URL, license/terms, retrieval date and version.
- [ ] Validate units, null/missing-value codes, and physically implausible values.
- [ ] Document district boundary/centroid method and any gridded-data aggregation.
- [ ] Harmonize crop IDs, agricultural years, seasons and calendar windows.
- [ ] Confirm that supported crops have real historical yield labels.
- [ ] Keep historical observations separate from forecasts and scenarios.
- [ ] Retain the original source files and repeatable transformation scripts.

## 8. Optional sources (not required for initial model)

| Source | Possible use | Official site |
|---|---|---|
| NASA SMAP | Regional soil-moisture context; too coarse for exact field measurements | https://smap.jpl.nasa.gov/ |
| NASA GPM | Additional precipitation monitoring | https://gpm.nasa.gov/ |
| NASA MODIS | Vegetation monitoring **after planting**, not a pre-planting input | https://modis.gsfc.nasa.gov/ |
| AGMARKNET | Historical market prices for **illustrative** revenue estimates | https://agmarknet.gov.in/ |
| FAO CROPWAT | Methodology for estimating crop-water needs | https://www.fao.org/land-water/resources/tools/software/cropwat/en/ |

## 9. Responsibilities and next steps

1. **Verify DES coverage first** for 3–5 selected crops and the initial geographic region.
2. Confirm calendar dates and regional coverage before building seasonal climate aggregates.
3. Retrieve NASA POWER daily records and SoilGrids regional extracts for matching historical observations.
4. Curate ECOCROP-based requirements plus independently sourced rotation rules.
5. Publish dataset manifests, feature definitions and dataset versions.
6. Follow [ML_MODEL_DOCUMENTATION.md](./ML_MODEL_DOCUMENTATION.md) for joins, training, inference, validation and recommendation logic.

> **Scientific boundary:** Gridded climate, modeled soil and district yield labels support **regional decision assistance**. They do **not** substantiate a claim of validated field-level yield forecasts or quantified future soil-health improvements.
