# System Architecture

# FieldShift AI 

**Project:** FieldShift AI\
**Purpose:** Support farmers with farm-boundary mapping, environmental
context from NASA datasets, and ML-assisted crop recommendations.

> **Status:** Proposed MVP architecture. Government parcel access and
> dataset availability must be confirmed. Recommendations are
> decision-support outputs, not guarantees.

## 1. Architecture Overview

The repository uses a monorepo with a React frontend, Node.js API,
Python ML service, and PostgreSQL database.

``` mermaid
flowchart TB
    Farmer[Farmer] --> Web[React + TypeScript Web App]
    Web --> Map[MapLibre Map: draw/select farm boundary]
    Web --> API[Node.js + Express API]
    API --> Auth[Authentication and Authorization]
    Auth --> DB[(PostgreSQL + PostGIS)]
    Map -->|Boundary GeoJSON| API
    API --> NASA[NASA Data Providers: POWER / optional SMAP, GPM, MODIS]
    API --> Parcel[Government Parcel Source, if available and authorized]
    API -->|Validated features| ML[Python FastAPI ML Service]
    ML --> Model[Scikit-learn model artifact]
    ML --> API
    API --> Web
```

### Components

-   **Web --- `apps/web`:** React, TypeScript, Vite, MapLibre GL JS.
    Provides login, dashboard, farm mapping, crop inputs, environmental
    views, and recommendation display.
-   **Application API --- `apps/api`:** Node.js, Express, TypeScript.
    Handles REST endpoints, authentication, ownership checks, database
    access, NASA data orchestration, and ML service requests.
-   **ML service --- `apps/ml-service`:** Python, FastAPI, Scikit-learn,
    Pandas, NumPy, Joblib. Loads the model, validates and preprocesses
    inputs, and performs inference.
-   **Database --- `database`:** PostgreSQL; PostGIS is recommended for
    geometry storage and spatial queries.
-   **Data --- `data`:** Local datasets and processing artifacts.
    Respect licensing, access conditions, and repository size limits.

## 2. Farm Boundary Flow

1.  Farmer signs in and opens the map.
2.  Farmer searches for a location or uses location permission.
3.  Farmer draws a polygon or selects a parcel from a permitted
    government layer, if available.
4.  Frontend sends boundary GeoJSON to the API.
5.  API validates geometry, checks authorization, and stores it.
6.  Farm area is calculated using a suitable geospatial method.

A boundary is a GeoJSON `Polygon` or `MultiPolygon`, not just a single
coordinate. GeoJSON coordinate order is **longitude, latitude**.

## 3. Environmental Data Flow

1.  API receives farm geometry or a representative coordinate.
2.  API retrieves supported environmental values from NASA services.
3.  API records source, parameters, units, location/grid, and time
    period.
4.  Values are transformed only according to the model's documented
    feature contract.
5.  Farmer-provided values and environmental values are combined into a
    validated prediction request.

NASA datasets have differing spatial and temporal resolutions. A grid
value should not be presented as a direct measurement of the exact farm.

Potential sources: - **NASA POWER:** temperature, precipitation,
humidity, solar radiation, depending on selected parameters and temporal
coverage. - **NASA SMAP:** soil-moisture information; resolution may be
too coarse for field-level ground truth. - **NASA GPM IMERG:**
precipitation estimates. - **NASA MODIS:** vegetation/land-surface
observations for monitoring workflows.

For the first MVP, start with one verified NASA source and farmer-drawn
boundaries.

## 4. Prediction Flow

``` mermaid
sequenceDiagram
    participant F as Farmer
    participant W as React Web
    participant A as Node API
    participant N as NASA Data API
    participant M as FastAPI ML Service
    participant D as PostgreSQL

    F->>W: Submit farm and crop-plan inputs
    W->>A: Authenticated prediction request
    A->>D: Verify farm ownership / read farm
    A->>N: Fetch environmental values
    N-->>A: Environmental data + metadata
    A->>M: Validated model features
    M-->>A: Prediction + model metadata
    A->>D: Save prediction record
    A-->>W: Recommendation response
    W-->>F: Show result and limitations
```

**Model compatibility requirement:** The inference feature names,
ordering, units, missing-value handling, and preprocessing must match
the training pipeline. Do not add NASA variables to an existing `.pkl`
model unless it was trained to accept them.

## 5. Proposed API Endpoints

These are planned endpoints, not necessarily implemented yet.

  ----------------------------------------------------------------------------------
  Method                  Endpoint                           Purpose
  ----------------------- ---------------------------------- -----------------------
  `POST`                  `/api/auth/register`               Create an account

  `POST`                  `/api/auth/login`                  Authenticate

  `POST`                  `/api/auth/logout`                 End session /
                                                             invalidate refresh
                                                             token if used

  `GET`                   `/api/auth/me`                     Current user profile

  `GET`                   `/api/farms`                       List accessible farms

  `POST`                  `/api/farms`                       Create farm and
                                                             boundary

  `GET`                   `/api/farms/:farmId`               Retrieve farm

  `PATCH`                 `/api/farms/:farmId`               Update farm

  `DELETE`                `/api/farms/:farmId`               Delete farm, subject to
                                                             product rules

  `GET`                   `/api/farms/:farmId/environment`   Retrieve environmental
                                                             context

  `POST`                  `/api/farms/:farmId/predictions`   Request crop
                                                             recommendation

  `GET`                   `/api/farms/:farmId/predictions`   Prediction history

  `GET`                   `/api/health`                      API health
  ----------------------------------------------------------------------------------

Internal ML endpoints:

  Method   Endpoint     Purpose
  -------- ------------ -------------------
  `GET`    `/health`    ML service health
  `POST`   `/predict`   Model inference

All protected routes must enforce authorization on the backend. Hiding a
frontend page is not sufficient.

## 6. Core Data Entities

### User

-   `id`, `name`, `email`, `password_hash`, `role`, `created_at`

### Farm

-   `id`, `user_id`, `name`, `boundary` (GeoJSON/PostGIS geometry),
    `area`, `area_unit`, `location_metadata`, `created_at`, `updated_at`

### Crop Plan

-   `id`, `farm_id`, `season`, `planned_crop`, `previous_crop`,
    `soil_type`, `irrigation`, `farmer_inputs`, `created_at`

### Environmental Retrieval Metadata

-   `id`, `farm_id` or location reference, `source`, `parameters`,
    `units`, `period_start`, `period_end`, `retrieved_at`, `payload` or
    normalized values

### Prediction

-   `id`, `farm_id`, `crop_plan_id`, `model_version`, `input_snapshot`,
    `predicted_crop`, `scores` (only if meaningful), `created_at`

## 7. Authentication and Authorization

Suggested roles: - **Farmer:** manage own farms, inputs, and prediction
history. - **Expert:** access only records explicitly assigned to them,
if this feature is added. - **Admin:** manage platform-level resources.

Security rules: - Verify farm ownership on every farm operation. - Do
not trust a browser-supplied `user_id` without checking the
authenticated identity. - Hash passwords with a suitable
password-hashing algorithm such as Argon2id or bcrypt. - Keep secrets
out of frontend code and source control. - Use HTTPS in deployment,
validate input, and rate-limit authentication/prediction endpoints. -
Avoid logging credentials, tokens, or sensitive personal data.

## 8. Deployment

Suggested arrangement: - Frontend: static hosting such as Vercel or
equivalent. - Node API: Node-compatible application host. - ML service:
Python/FastAPI-compatible host. - Database: managed PostgreSQL; enable
PostGIS if supported. - Secrets: host environment settings or secret
manager.

``` mermaid
flowchart LR
    Browser[Farmer Browser] --> Frontend[Frontend Hosting]
    Frontend --> API[Node API Host]
    API --> DB[(Managed PostgreSQL)]
    API --> ML[FastAPI ML Host]
    API --> NASA[NASA APIs]
```

Confirm provider availability, limits, and pricing before deployment.

## 9. Responsible Use and Data Quality

-   Display units, source, and time period for environmental data.
-   State known spatial/temporal resolution limitations.
-   Distinguish model outputs from measured or official field
    conditions.
-   Do not claim recommendations guarantee yield, profit, or crop
    success.
-   Record model version and input snapshot for reproducibility.
-   Handle missing, delayed, or unavailable external data gracefully.
-   Government cadastral boundaries may not equal the currently
    cultivated area and should not be presented as legal survey
    determinations unless the source and use support that claim.

## 10. Repository Mapping

``` text
fieldshift-ai/
├── apps/
│   ├── web/             # React UI and MapLibre
│   ├── api/              # Express API, auth, farm/NASA orchestration
│   └── ml-service/       # FastAPI, preprocessing, inference
├── packages/
│   └── shared-types/     # Shared TypeScript types
├── database/             # Prisma schema and migrations
├── data/                 # Datasets (respect size/access restrictions)
└── docs/
    └── ARCHITECTURE.md
```

