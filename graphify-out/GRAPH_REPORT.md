# Graph Report - fieldshift-ai  (2026-11-13)

## Corpus Check
- 30 files · ~8,345 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 47 file(s) not represented in the graph (top: (none) 35, .ipynb 9, .example 2)
- WARNING: 47 of 79 files seen (59%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 109 nodes · 96 edges · 25 communities (9 shown, 16 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `024b6b7f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

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
6. `Soil Data Three Sources` - 4 edges
7. `FieldShift AI Data Sources and Integration` - 4 edges
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

## Communities (25 total, 16 thin omitted)

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
- **23 isolated node(s):** `DES Indian Crop Area Production and Yield`, `ERA5 Land Surface and Soil Moisture Reanalysis`, `FAO Crop Calendar Crop and Season Timing`, `FAO ECOCROP Environmental Requirements`, `Humeris Complementary Soil Properties` (+18 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 74 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `scripts` connect `Apps Api Package Scripts` to `Apps Api Package`?**
  _High betweenness centrality (0.013) - this node is a cross-community bridge._
- **What connects `DES Indian Crop Area Production and Yield`, `ERA5 Land Surface and Soil Moisture Reanalysis`, `FAO Crop Calendar Crop and Season Timing` to the rest of the system?**
  _23 weakly-connected nodes found - possible documentation gaps or missing edges._