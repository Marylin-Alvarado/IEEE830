## ADDED Requirements

### Requirement: Project table display
The system SHALL display all registered projects in an organized table using Streamlit's data table component.

#### Scenario: View projects table
- **WHEN** the application loads or a new project is saved
- **THEN** the system SHALL render a table with all registered projects showing all fields

#### Scenario: Table updates after save
- **WHEN** a new project is successfully registered
- **THEN** the system SHALL refresh the table to include the newly added project
