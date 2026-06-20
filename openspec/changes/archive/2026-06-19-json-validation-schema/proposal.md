## Why

The SGR system stores project data in JSON files (`proyectos_sgr.json`) without a formal schema for validation. There is no governance mechanism to enforce data integrity, field types, or compliance with the IEEE 830 and EARS syntactic rules at the data layer. This poses a risk for the thesis reproducibility requirement.

## What Changes

- Create `schemas/` directory at project root
- Create `schemas/project_schema.json` defining a JSON Schema for SGR data validation
- Schema covers: project metadata (nombre, objetivo, descripción, fecha), requirements (código, descripción, EARS keywords WHEN/THE SYSTEM SHALL, tipo IEEE 830)

## Capabilities

### New Capabilities
- `data-validation-schema`: JSON Schema definition for structured validation of SGR project and requirement data, enforcing IEEE 830 data governance

### Modified Capabilities
- (none)

## Impact

- New directory: `schemas/`
- New file: `schemas/project_schema.json`
- No changes to existing code (schema is for documentation and external validation)
