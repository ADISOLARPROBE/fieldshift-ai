# NASA Data Sources

## Overview

FieldShift AI integrates environmental datasets with machine learning to predict crop yields and recommend suitable crops based on local growing conditions.

The initial implementation focuses on two primary environmental data sources:

1. **NASA POWER** — Weather and climate data.
2. **ISRIC SoilGrids** — Soil characteristics.

The platform will use a farmer's geographical location to retrieve environmental information automatically, minimizing manual input.

## 1. NASA POWER — Climate Data

NASA POWER (Prediction of Worldwide Energy Resources) provides historical meteorological and solar radiation data through a publicly accessible API.

**Official website:** https://power.larc.nasa.gov/

### Selected Parameters

| Parameter | API Code | Description |
|---|---|---|
| Average temperature | `T2M` | Daily average air temperature |
| Maximum temperature | `T2M_MAX` | Daily maximum temperature |
| Minimum temperature | `T2M_MIN` | Daily minimum temperature |
| Precipitation | `PRECTOTCORR` | Daily precipitation |
| Relative humidity | `RH2M` | Atmospheric moisture |
| Solar radiation | `ALLSKY_SFC_SW_DWN` | Surface solar energy |

### API

**Endpoint:**

`https://power.larc.nasa.gov/api/temporal/daily/point`

**Example request:**

```text
https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M,T2M_MAX,T2M_MIN,PRECTOTCORR,RH2M,ALLSKY_SFC_SW_DWN&community=AG&longitude=80.6&latitude=16.5&start=20200101&end=20201231&format=JSON
```

The data will be processed to calculate relevant environmental features such as average seasonal temperature, total rainfall, and average humidity.

**Documentation:** https://power.larc.nasa.gov/docs/services/api/

## 2. ISRIC SoilGrids — Soil Data

SoilGrids provides global estimates of soil properties at approximately 250-metre spatial resolution.

It is developed by ISRIC — World Soil Information and is not a NASA dataset.

### Selected Soil Parameters

| Parameter | Description |
|---|---|
| Soil pH | Soil acidity or alkalinity |
| Sand content | Percentage of sand particles |
| Clay content | Percentage of clay particles |
| Silt content | Percentage of silt particles |
| Soil organic carbon | Indicator of organic matter |
| Cation exchange capacity | Soil nutrient-retention capacity |

### Data Retrieval

Soil characteristics will be estimated using the geographical coordinates of the farmer's selected location.

Because the SoilGrids REST API has experienced availability issues, FieldShift may use regional SoilGrids datasets obtained through supported services such as WCS or Google Earth Engine.

The values will be treated as regional soil estimates rather than exact field measurements.

**Documentation:** https://docs.isric.org/globaldata/soilgrids/

## 3. Data Processing Pipeline

The proposed environmental data workflow consists of:

1. Retrieve the farmer's latitude and longitude.
2. Fetch historical climate data from NASA POWER.
3. Obtain corresponding soil-property estimates from SoilGrids.
4. Clean and preprocess the collected data using Pandas and NumPy.
5. Generate the features required by the trained ML model.
6. Combine environmental features with farmer-provided inputs.
7. Pass the processed data to the XGBoost model for crop yield prediction.

## 4. Machine Learning Integration

FieldShift AI will initially use an XGBoost regression model to estimate crop yield.

### Initial Input Features

**Climate features:**

- Average temperature
- Total rainfall
- Relative humidity
- Solar radiation

**Soil features:**

- Soil pH
- Sand percentage
- Clay percentage
- Silt percentage
- Soil organic carbon

**Additional features:**

- Crop type
- Growing season
- Geographical region
- Irrigation availability, where suitable training data exists

### Prediction Target

The primary output will be:

**Expected crop yield (tonnes per hectare).**

Historical crop-yield records will be required to train the model.

Predicted yields will subsequently be used by a separate recommendation and profitability calculation system.

## 5. Limitations

- Climate and soil datasets provide geographical estimates rather than exact farm measurements.
- Historical weather observations do not represent guaranteed future conditions.
- Pre-season predictions must use information available before planting.
- SoilGrids data does not replace laboratory soil testing.
- The model's reliability depends on the quality of historical training data and geographical coverage.
- Input features and preprocessing must remain consistent between training and inference.

## 6. Initial Development Scope

The first version of FieldShift AI will prioritize:

- Automatic location-based environmental data retrieval.
- NASA POWER weather integration.
- SoilGrids soil-property integration.
- Data preprocessing and feature engineering.
- XGBoost-based crop yield prediction.
- Basic crop suitability and profitability comparison.

Advanced remote-sensing image processing, vegetation-index analysis, and automatic satellite-based field segmentation are outside the initial implementation scope.

## References

1. NASA POWER — https://power.larc.nasa.gov/
2. NASA POWER API — https://power.larc.nasa.gov/docs/services/api/
3. ISRIC SoilGrids — https://docs.isric.org/globaldata/soilgrids/
4. Indian Agricultural Statistics — https://data.desagri.gov.in/website/crops-report-district-level-web