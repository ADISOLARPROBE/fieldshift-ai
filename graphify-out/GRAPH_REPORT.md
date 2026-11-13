# Graph Report - fieldshift-ai  (2026-11-13)

## Corpus Check
- Corpus is ~11,331 words - fits in a single context window. You may not need a graph.

## Summary
- 113 nodes · 98 edges · 27 communities (9 shown, 18 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Apps Api Package
- Apps Api Tsconfig
- Docs Nasa Data Sources Da
- Tsconfig
- Docs Architecture Authent
- Apps Api Package Dependen
- Package
- Apps Api Readme Api
- Apps Api Package Scripts
- Apps Ml Service App Main
- Apps Ml Service Requireme
- Requirements Dependencies

## God Nodes (most connected - your core abstractions)
1. `compilerOptions` - 10 edges
2. `compilerOptions` - 10 edges
3. `FieldShift AI Architecture` - 10 edges
4. `Data-source Overview` - 6 edges
5. `scripts` - 4 edges
6. `FieldShift AI Data Sources and Integration` - 4 edges
7. `Soil Data Three Sources` - 4 edges
8. `cors` - 3 edges
9. `dotenv` - 3 edges
10. `express` - 3 edges

## Surprising Connections (you probably didn't know these)
- `FieldShift AI` --references--> `Node API Express Service`  [EXTRACTED]
  README.md → apps/api/README.md
- `FieldShift AI` --references--> `ML Service FastAPI`  [EXTRACTED]
  README.md → apps/ml-service/README.md
- `FieldShift AI` --references--> `Web Frontend React App`  [EXTRACTED]
  README.md → apps/web/README.md

## Import Cycles
- None detected.

## Communities (27 total, 18 thin omitted)

### Community 0 - "Apps Api Package"
Cohesion: 0.17
Nodes (15): description, devDependencies, ts-node-dev@^2.0.0, @types/cors@^2.8.17, @types/express@^5.0.0, @types/node@^22.10.1, typescript@^5.7.2, main (+7 more)

### Community 1 - "Apps Api Tsconfig"
Cohesion: 0.15
Nodes (12): compilerOptions, esModuleInterop, forceConsistentCasingInFileNames, module, moduleResolution, outDir, rootDir, skipLibCheck (+4 more)

### Community 2 - "Docs Nasa Data Sources Da"
Cohesion: 0.15
Nodes (13): Data-source Overview, DES Indian Crop Area Production and Yield, ERA5 Land Surface and Soil Moisture Reanalysis, FAO Crop Calendar Crop and Season Timing, FAO ECOCROP Environmental Requirements, FieldShift AI Data Sources and Integration, Humeris Complementary Soil Properties, ISRIC SoilGrids (+5 more)

### Community 3 - "Tsconfig"
Cohesion: 0.15
Nodes (12): compilerOptions, esModuleInterop, forceConsistentCasingInFileNames, module, moduleResolution, outDir, rootDir, skipLibCheck (+4 more)

### Community 4 - "Docs Architecture Authent"
Cohesion: 0.18
Nodes (9): System Components, Core Data Entities, Deployment Architecture, Environmental Data Flow, Farm Boundary Flow, FieldShift AI Architecture, Prediction Flow, Proposed API Endpoints (+1 more)

### Community 5 - "Apps Api Package Dependen"
Cohesion: 0.28
Nodes (8): dependencies, cors@^2.8.5, dotenv@^16.4.7, express@^4.21.2, app, cors, dotenv, express

### Community 6 - "Package"
Cohesion: 0.33
Nodes (5): name, private, scripts, build:api, dev:api

### Community 7 - "Apps Api Readme Api"
Cohesion: 0.40
Nodes (5): Node API Express Service, ML Service FastAPI, Web Frontend React App, Map Components, FieldShift AI

### Community 8 - "Apps Api Package Scripts"
Cohesion: 0.50
Nodes (4): scripts, build, dev, start

## Knowledge Gaps
- **23 isolated node(s):** `ML Service Python Dependencies`, `Node API Express Service`, `ML Service FastAPI`, `Python Data Science Dependencies`, `Map Components` (+18 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 78 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **18 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `scripts` connect `Apps Api Package Scripts` to `Apps Api Package`?**
  _High betweenness centrality (0.013) - this node is a cross-community bridge._
- **What connects `ML Service Python Dependencies`, `Node API Express Service`, `ML Service FastAPI` to the rest of the system?**
  _23 weakly-connected nodes found - possible documentation gaps or missing edges._