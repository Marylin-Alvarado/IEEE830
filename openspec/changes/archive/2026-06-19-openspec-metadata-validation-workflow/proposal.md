## Why

The `requisitos.md` document lacks formal metadata (status, version, authors), a revision history, and a structured validation mechanism to track requirement approval states. This makes it difficult to audit which requirements have passed EARS grammar validation and which are still pending review, impacting the thesis traceability and IEEE 830 compliance.

## What Changes

- Add metadata block at the top of `requisitos.md`: `status: proposed`, `version: 1.0`, `authors: Marylin Alvarado`
- Add "Historial de Revisiones" table just below the metadata (Version, Fecha, Autor, Descripción del Cambio)
- Add "Workflow de Validación EARS" checklist section at the end of each functional requirement subsection (3.1.1 through 3.1.13), verifying keyword presence (WHEN, THE SYSTEM SHALL) to advance status to `approved`
- Update the `ieee830-srs` capability spec to reflect these new document requirements

## Capabilities

### New Capabilities
- `document-metadata`: Formal metadata and revision history tracking for the IEEE 830 document
- `ears-validation-workflow`: Structured EARS validation checklist per functional requirement with state transition (proposed → approved)

### Modified Capabilities
- `ieee830-srs`: Add requirements for metadata block, revision history, and per-requirement EARS validation workflow

## Impact

- `requisitos.md`: Header restructured, ~13 validation checklist sections added (one per functional subsection)
- `openspec/specs/ieee830-srs/spec.md`: New requirements for metadata and validation workflow
