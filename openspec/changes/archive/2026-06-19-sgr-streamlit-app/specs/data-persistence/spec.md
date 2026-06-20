## ADDED Requirements

### Requirement: JSON file storage
The system SHALL persist all registered projects to a local file named `proyectos_sgr.json`.

#### Scenario: Save project to file
- **WHEN** a new project passes validation
- **THEN** the system SHALL append the project to the `proyectos_sgr.json` file

#### Scenario: Load projects on startup
- **WHEN** the application starts
- **THEN** the system SHALL read `proyectos_sgr.json` and load all existing projects into memory

### Requirement: Data structure
Each project SHALL be stored as a JSON object with fields: `nombre_proyecto`, `objetivo_general`, `descripcion_dominio`, and `fecha_registro`.

#### Scenario: Verify stored format
- **WHEN** a project is saved to `proyectos_sgr.json`
- **THEN** the JSON record SHALL contain all four fields with correct types
