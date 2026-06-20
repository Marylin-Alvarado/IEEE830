## Context

The `requisitos.md` document (1062 lines, 60KB) is an IEEE 830-1998 Software Requirements Specification. It currently has no metadata header, revision history, or structured validation workflow. The document has 13 functional requirement subsections (3.1.1–3.1.13) with 42 RFs written in EARS syntax. Each subsection ends with examples (ejemplos válidos/inválidos) but lacks a formal validation checklist.

## Goals / Non-Goals

**Goals:**
- Add a metadata block at the very top of `requisitos.md` (before the main title)
- Add a "Historial de Revisiones" table below the metadata
- Append a "Workflow de Validación EARS" checklist at the end of each of the 13 functional requirement subsections
- Update the `ieee830-srs` capability spec to reflect new document requirements

**Non-Goals:**
- No structural reorganization of existing content
- No behavioral changes to `app.py` or any code
- No new test files
- No changes to EARS grammar rules themselves

## Decisions

- **Metadata format**: YAML-style block (```---``` fenced) placed before the `# SGR` title, consistent with Markdown front matter conventions
- **Revision history as markdown table**: Using standard GFM table syntax, placed immediately after the metadata block and before `# 1. Introducción`
- **Workflow checklist inserted per subsection**: Each of the 13 subsections gets the checklist appended at its end (after the last line of examples/scenarios), using `### Workflow de Validación EARS` as the subsection header. The checklist iterates over all RF-# in that subsection and checks keyword presence.
- **State transition**: All RFs passing → `approved`; any failure → `proposed (pendiente de corrección)`
- **Delta spec for ieee830-srs**: Modified the main requirement to include metadata + workflow; added new requirements for metadata and validation

## Risks / Trade-offs

- **Document length increase**: ~13 checklists × ~15 lines each ≈ +200 lines. Acceptable for a 1062-line document.
- **Checklist maintenance**: If new functional subsections are added later, the checklist must be added manually. Mitigation: document this in the spec requirement.
