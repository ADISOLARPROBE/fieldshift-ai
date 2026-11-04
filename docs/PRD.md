# Product Requirements Document
# FieldShift AI --- Product Requirements Document

**Version:** 1.0 \| **Status:** Hackathon MVP

## 1. Product Goal

Help farmers understand field conditions using farm boundaries, NASA
Earth-observation/climate data, and machine-learning insights.

## 2. Target Users

-   **Farmer:** Adds farms, views conditions, and receives risk
    insights.
-   **Expert/Admin:** Reviews data and manages platform activity.

## 3. MVP Features

1.  **Authentication:** Sign up, sign in, role-based access.
2.  **Dashboard:** Farm summary, climate indicators, and alerts.
3.  **Farm Management:** Add farms, crop type, and location.
4.  **Farm Map:** Draw/edit field boundaries; calculate area; save
    GeoJSON.
5.  **Climate Insights:** Visualize available temperature, rainfall,
    humidity, and solar-radiation trends.
6.  **AI Insights:** Display model predictions, risk levels, and
    explanations.
7.  **Alerts & Reports:** Show risk alerts and export a basic farm
    report.

## 4. Core User Flow

Sign up → Add farm → Draw boundary → Select crop → Retrieve data → Run
model → View insights.

## 5. Recommended Technology Stack & Frameworks

  -----------------------------------------------------------------------
  Layer                   Framework / Technology  Purpose
  ----------------------- ----------------------- -----------------------
  Frontend                React + TypeScript +    Web application
                          Vite                    

  UI                      Tailwind CSS +          Styling and components
                          shadcn/ui               

  Maps                    MapLibre GL JS + Terra  Interactive maps and
                          Draw                    boundary drawing

  Geospatial              Turf.js                 Polygon and area
                                                  calculations

  Backend                 Node.js + Express +     REST API and business
                          TypeScript              logic

  ML service              Python + FastAPI        Serve the trained model

  ML libraries            scikit-learn, pandas,   Prediction and
                          NumPy, joblib           processing

  Database                PostgreSQL + PostGIS    Relational and
                                                  geospatial storage

  ORM                     Prisma                  Database access and
                                                  migrations

  Authentication          JWT + bcrypt            Token authentication
                                                  and password hashing

  Charts                  Recharts                Climate and prediction
                                                  charts

  Validation              Zod + Pydantic          Validate API inputs

  Data                    NASA POWER; optional    Climate and
                          SMAP, GPM, MODIS        Earth-observation data

  Collaboration           Git + GitHub            Version control
  -----------------------------------------------------------------------

## 6. Key Data Entities

-   **User:** id, name, email, password hash, role, profile picture 
-   **Farm:** id, owner id, name, crop, area, boundary GeoJSON
-   **ClimateRecord:** farm id, date, variable, value, source
-   **Prediction:** farm id, model version, result, risk level,
    timestamp
-   **Alert:** farm id, type, severity, message, status

## 7. System Architecture

React frontend → Express API → PostgreSQL/PostGIS\
Express API → NASA data sources\
Express API → FastAPI ML service → trained model → prediction\
Frontend displays observations, predictions, and alerts.

## 8. Non-Functional Requirements

-   Responsive on desktop and mobile.
-   Enforce farm ownership and role-based access.
-   Keep secrets and API keys on the server.
-   Show data source, units, and observation date.
-   Handle missing data and model errors clearly.

## 9. MVP Acceptance Criteria

-   Users can register and sign in.
-   Farmers can create farms and save boundaries.
-   Available climate data is displayed for a farm.
-   The ML service returns predictions using the model's expected input
    schema.
-   Dashboard results and alerts use real data; no fabricated values.

## 10. Dependencies & Setup Notes

-   **Frontend:** `react`, `react-dom`, `typescript`, `vite`,
    `tailwindcss`, `maplibre-gl`, `@turf/turf`, `recharts`, `zod`.
-   **Backend:** `express`, `cors`, `dotenv`, `jsonwebtoken`, `bcrypt`,
    `zod`, `prisma`, `@prisma/client`.
-   **ML service:** `fastapi`, `uvicorn`, `scikit-learn`, `pandas`,
    `numpy`, `joblib`, `pydantic`.
-   Enable the **PostGIS** extension in PostgreSQL.
-   Use npm for JavaScript packages and a Python virtual environment
    with `requirements.txt` for ML packages.
-   Pin dependency versions; store secrets in environment variables.
-   **Model compatibility:** The `.pkl` model must receive the same
    features and preprocessing used during training. Only pass NASA
    variables if the model was trained to accept them.
-   NASA datasets differ in resolution, coverage, and update frequency;
    display their limitations.

## 11. Out of Scope for MVP

Native mobile apps, automated land-record integration, payments, social
features, and fully automated agronomic prescriptions.
