## ADDED Requirements

### Requirement: JSON Schema for project data
The system SHALL include a JSON Schema file at `schemas/project_schema.json` that defines the structure and validation rules for SGR project data.

#### Scenario: Schema validates project metadata
- **WHEN** a project record is validated against the schema
- **THEN** it SHALL enforce required fields: `nombre_proyecto`, `objetivo_general`, `descripcion_dominio`, `fecha_registro` with appropriate types

### Requirement: JSON Schema for requirements
The schema SHALL define a `requisitos` array with objects containing: `codigo`, `descripcion`, `sintaxis_ears` (keywords WHEN and THE SYSTEM SHALL), and `tipo_ieee830` (functional, non-functional, interface, business rule).

#### Scenario: Requirement object structure
- **WHEN** a requirement object is validated
- **THEN** it SHALL contain `codigo` (string pattern RF-XXX), `descripcion` (non-empty string), `sintaxis_ears` (object with `when` and `the_system_shall` boolean flags), and `tipo_ieee830` (enum of valid types)

### Requirement: EARS keyword enforcement
The schema SHALL enforce that every requirement includes `sintaxis_ears.when` and `sintaxis_ears.the_system_shall` as boolean fields that must be `true` for valid requirements.

#### Scenario: EARS validation in schema
- **WHEN** a requirement is validated
- **THEN** `sintaxis_ears.when` and `sintaxis_ears.the_system_shall` SHALL both be `true`

### Requirement: Schema discoverability
The `project_schema.json` file SHALL be placed in the `schemas/` directory at the project root.

#### Scenario: Schema file exists
- **WHEN** the project root is inspected
- **THEN** the `schemas/` directory SHALL contain `project_schema.json`
