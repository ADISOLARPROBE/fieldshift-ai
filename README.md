# FieldShift AI

NASA Space Apps Challenge project for farm boundary mapping, NASA environmental data integration, and ML-assisted crop recommendations.

## Repository layout
- `apps/web` — React + TypeScript frontend and interactive map
- `apps/api` — Node.js + Express API
- `apps/ml-service` — Python + FastAPI model inference service
- `database` — Prisma schema and migrations
- `data` — datasets (avoid committing large/restricted data)
- `docs` — project documentation

Copy `.env.example` to `.env` and configure local values.

```
fieldshift-ai/
│
├── apps/
│   │
│   ├── web/                           # React Frontend
│   │   ├── public/
│   │   │   ├── images/
│   │   │   ├── icons/
│   │   │   └── logo.svg
│   │   │
│   │   ├── src/
│   │   │   ├── assets/
│   │   │   ├── components/
│   │   │   │   ├── ui/
│   │   │   │   ├── layout/
│   │   │   │   ├── map/
│   │   │   │   │   ├── FarmMap.tsx
│   │   │   │   │   ├── FarmBoundary.tsx
│   │   │   │   │   ├── MapControls.tsx
│   │   │   │   │   └── MapLayers.tsx
│   │   │   │   └── dashboard/
│   │   │   │
│   │   │   ├── pages/
│   │   │   │   ├── Home.tsx
│   │   │   │   ├── Login.tsx
│   │   │   │   ├── Register.tsx
│   │   │   │   ├── Dashboard.tsx
│   │   │   │   ├── FarmDetails.tsx
│   │   │   │   ├── CropRecommendation.tsx
│   │   │   │   └── Profile.tsx
│   │   │   │
│   │   │   ├── features/
│   │   │   │   ├── auth/
│   │   │   │   ├── farm/
│   │   │   │   ├── nasa-data/
│   │   │   │   └── crop-recommendation/
│   │   │   │
│   │   │   ├── hooks/
│   │   │   ├── services/
│   │   │   │   ├── api.ts
│   │   │   │   ├── auth.service.ts
│   │   │   │   ├── farm.service.ts
│   │   │   │   └── nasa.service.ts
│   │   │   │
│   │   │   ├── types/
│   │   │   ├── utils/
│   │   │   ├── App.tsx
│   │   │   ├── main.tsx
│   │   │   └── index.css
│   │   │
│   │   ├── .env.example
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   └── vite.config.ts
│   │
│   ├── api/                           # Node.js + Express Backend
│   │   ├── src/
│   │   │   ├── config/
│   │   │   │   ├── database.ts
│   │   │   │   └── env.ts
│   │   │   │
│   │   │   ├── controllers/
│   │   │   │   ├── auth.controller.ts
│   │   │   │   ├── farm.controller.ts
│   │   │   │   ├── nasa.controller.ts
│   │   │   │   └── crop.controller.ts
│   │   │   │
│   │   │   ├── routes/
│   │   │   │   ├── auth.routes.ts
│   │   │   │   ├── farm.routes.ts
│   │   │   │   ├── nasa.routes.ts
│   │   │   │   └── crop.routes.ts
│   │   │   │
│   │   │   ├── middleware/
│   │   │   │   ├── auth.middleware.ts
│   │   │   │   ├── role.middleware.ts
│   │   │   │   ├── error.middleware.ts
│   │   │   │   └── validate.middleware.ts
│   │   │   │
│   │   │   ├── services/
│   │   │   │   ├── auth.service.ts
│   │   │   │   ├── farm.service.ts
│   │   │   │   ├── nasa.service.ts
│   │   │   │   └── ml.service.ts
│   │   │   │
│   │   │   ├── repositories/
│   │   │   ├── validators/
│   │   │   ├── utils/
│   │   │   ├── app.ts
│   │   │   └── server.ts
│   │   │
│   │   ├── tests/
│   │   ├── .env.example
│   │   ├── package.json
│   │   └── tsconfig.json
│   │
│   └── ml-service/                    # Python + FastAPI
│       ├── app/
│       │   ├── api/
│       │   │   ├── routes/
│       │   │   │   ├── predict.py
│       │   │   │   └── health.py
│       │   │   └── schemas/
│       │   │       └── prediction_schema.py
│       │   │
│       │   ├── services/
│       │   │   ├── prediction_service.py
│       │   │   ├── nasa_service.py
│       │   │   └── preprocessing.py
│       │   │
│       │   ├── models/
│       │   │   └── model_loader.py
│       │   │
│       │   ├── config.py
│       │   └── main.py
│       │
│       ├── model/
│       │   ├── crop_model.pkl
│       │   └── model_metadata.json
│       │
│       ├── notebooks/
│       │   ├── data_exploration.ipynb
│       │   └── model_training.ipynb
│       │
│       ├── tests/
│       ├── requirements.txt
│       ├── Dockerfile
│       └── .env.example
│
├── packages/
│   └── shared-types/                  # Shared API types
│       ├── src/
│       │   ├── auth.ts
│       │   ├── farm.ts
│       │   ├── nasa.ts
│       │   └── crop.ts
│       └── package.json
│
├── database/
│   ├── schema.prisma
│   ├── migrations/
│   └── seed.ts
│
├── data/
│   ├── raw/                           # Original datasets
│   ├── processed/                     # Cleaned datasets
│   ├── external/
│   │   ├── nasa/
│   │   └── government/
│   └── README.md
│
├── docs/
│   ├── PRD.md
│   ├── ARCHITECTURE.md
│   ├── API_DOCUMENTATION.md
│   ├── NASA_DATA_SOURCES.md
│   ├── ML_MODEL_DOCUMENTATION.md
│   └── CONTRIBUTING.md
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .gitignore
├── .env.example
├── docker-compose.yml
├── package.json
├── README.md
└── LICENSE
```

## Important Instructions
- Everyone will work on their separate branches and only after accepting PR will it be merged in main branch later
- Give proper commit message for all commits
