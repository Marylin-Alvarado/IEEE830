## ADDED Requirements

### Requirement: IEEE 830 requirement card display
The system SHALL render each functional requirement as a vertical technical card in the Streamlit UI when the "Generar Requisitos con IA" button is activated.

#### Scenario: Card contains all required fields
- **WHEN** a functional requirement is displayed
- **THEN** the card SHALL include exactly five labeled fields: "Identificación del requerimiento", "Nombre del requerimiento", "Características", "Descripción del requerimiento (Sintaxis EARS)", and "Prioridad del requerimiento"

#### Scenario: Card layout is vertical
- **WHEN** the requirement card is rendered
- **THEN** each field SHALL be stacked vertically with the field name in bold followed by its value

### Requirement: EARS syntax display in requirement cards
The system SHALL display the EARS classification and formal syntax for each functional requirement within the "Descripción del requerimiento (Sintaxis EARS)" field of the card.

#### Scenario: EARS syntax shown
- **WHEN** the card shows the description field
- **THEN** it SHALL include the EARS category (Ubiquitous, Event-Driven, State-Driven, Optional, Desired) and the formal syntax pattern

### Requirement: Non-functional requirements matrix table
The system SHALL render section "3.2 Requerimientos No Funcionales" as an interactive matrix table below the functional requirement cards.

#### Scenario: Table displays NFRs
- **WHEN** the non-functional requirements section is rendered
- **THEN** the system SHALL display a `st.dataframe` with columns for ID, requisito, and category (usabilidad, rendimiento, confiabilidad, precisión, mantenibilidad, hardware)

### Requirement: Business rules indexed list
The system SHALL render section "3.3 Reglas de Negocio" as a formal numbered list below the non-functional requirements table.

#### Scenario: Business rules displayed
- **WHEN** the business rules section is rendered
- **THEN** the system SHALL display each rule as a numbered item (1., 2., 3., ...) with bold rule name followed by the rule description

### Requirement: Toggle visibility via button
The system SHALL show/hide the requirements sections based on a "Generar Requisitos con IA" button using Streamlit session state.

#### Scenario: Button activates display
- **WHEN** the user clicks "Generar Requisitos con IA"
- **THEN** the system SHALL set `st.session_state["mostrar_requisitos"] = True` and render all three requirement sections

#### Scenario: Initial state is hidden
- **WHEN** the application first loads
- **THEN** the requirements sections SHALL be hidden until the user clicks the button
