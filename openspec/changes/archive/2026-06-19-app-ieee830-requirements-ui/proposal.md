## Why

The current `app.py` only supports project registration and listing. It does not render the detailed IEEE 830 requirements defined in the specification (`requisitos.md`) as interactive UI cards. Users cannot visualize functional requirements with EARS syntax, non-functional requirement tables, or business rules directly in the application. Adding a "Generar Requisitos con IA" button that parses and displays structured requirement cards bridges the gap between the specification document and the running application, making the IEEE 830 content accessible and navigable.

## What Changes

- Add a "Generar Requisitos con IA" button to `app.py` that triggers reading and processing of the IEEE 830 specification rules
- Display vertical technical cards for each functional requirement with exact fields: Identificación, Nombre, Características, Descripción del requerimiento (Sintaxis EARS), Prioridad
- Render section "3.2 Requerimientos No Funcionales" as a matrix table below the cards
- Render section "3.3 Reglas de Negocio" as a formal indexed list
- Parse and organize requirement data from the specification content embedded in the application

## Capabilities

### New Capabilities
- `requirements-ui`: Streamlit-based UI component that renders IEEE 830 requirement cards (functional cards, non-functional matrix table, business rules indexed list) from parsed specification data

### Modified Capabilities
- `ieee830-srs`: The specification rendering behavior changes — requirements defined in the SRS spec are now displayed interactively in the running application rather than existing only as a document

## Impact

- **Modified file**: `app.py` — new button, card rendering logic, matrix table, indexed list, and spec data parsing
- **Dependencies**: `streamlit` (already present); no new external dependencies
- **No spec changes**: The specification content itself (`requisitos.md`) is not modified — only its in-app rendering
