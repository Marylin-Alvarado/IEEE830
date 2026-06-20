## Context

The SGR persists data via `proyectos_sgr.json` (written by `app.py` using `json.dump`), but there is no formal schema to validate the data structure. The Pydantic model (`Proyecto`) provides runtime validation in Python, but the JSON files themselves lack a contract for consumers, external tools, or thesis auditors.

## Goals / Non-Goals

**Goals:**
- Create `schemas/project_schema.json` defining JSON Schema (draft-07) for SGR data governance
- Define top-level project fields (nombre_proyecto, objetivo_general, descripcion_dominio, fecha_registro)
- Define `requisitos` array with per-requirement objects (codigo, descripcion, sintaxis_ears, tipo_ieee830)
- Enforce EARS keywords (WHEN, THE SYSTEM SHALL) as required boolean fields set to `true`

**Non-Goals:**
- No changes to `app.py` or its Pydantic model
- No runtime integration with the schema (documentation/audit only)
- No automatic schema generation from Pydantic models

## Decisions

- **JSON Schema draft-07**: Widely supported by validators (`python jsonschema` lib, ajv for Node.js), and sufficient for the required constraints.
- **`additionalProperties: false`**: Strict mode — no undeclared fields allowed in project or requirement objects.
- **`sintaxis_ears` as nested object**: Rather than flat boolean fields, grouping under `sintaxis_ears` provides semantic clarity. Both `when` and `the_system_shall` must be `true` (enforced via `const: true`).
- **`codigo` pattern**: Enforced as `^RF-\d{2}$` (e.g., RF-01, RF-42).
- **`tipo_ieee830` enum**: Restricted to `["functional", "non-functional", "interface", "business_rule"]`.

## Risks / Trade-offs

- **Schema drift**: If the Pydantic model is updated, the JSON Schema must be manually synchronized. Mitigation: add a note in the schema referencing `app.py:150-154`.
- **No runtime enforcement**: The schema is for governance documentation only. Mitigation: consider adding a CI step that validates `proyectos_sgr.json` against the schema using `npx ajv validate`.
