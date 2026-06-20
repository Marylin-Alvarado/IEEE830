## MODIFIED Requirements

### Requirement: Toggle visibility via button
The system SHALL show/hide the requirements sections based on a "Generar Requisitos con IA" button using Streamlit session state. The button SHALL only appear after a project has been successfully registered.

#### Scenario: Button activates display
- **WHEN** the user clicks "Generar Requisitos con IA"
- **THEN** the system SHALL set `st.session_state["mostrar_requisitos"] = True` and render all three requirement sections

#### Scenario: Button hidden before registration
- **WHEN** the application first loads and no project has been registered yet
- **THEN** the "Generar Requisitos con IA" button SHALL NOT be displayed

#### Scenario: Button visible after registration
- **WHEN** a project is successfully saved to `proyectos_sgr.json`
- **THEN** the system SHALL display the "Generar Requisitos con IA" button
