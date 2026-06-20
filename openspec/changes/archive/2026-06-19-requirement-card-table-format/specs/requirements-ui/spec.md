## MODIFIED Requirements

### Requirement: IEEE 830 requirement card display
The system SHALL render each functional requirement as a Ficha Técnica Estructurada (structured technical card) in the Streamlit UI when the "Generar Requisitos con IA" button is activated.

#### Scenario: Card is a two-column table
- **WHEN** a functional requirement is displayed
- **THEN** the card SHALL be rendered as a Markdown table with exactly two columns: "Campo" and "Detalle"

#### Scenario: Card contains all required rows
- **WHEN** the requirement card is rendered
- **THEN** the table SHALL include exactly six rows: "Identificación", "Nombre", "Características", "Sintaxis EARS", "Categoría", and "Prioridad"

#### Scenario: Card layout uses table per requirement
- **WHEN** the requirement card is rendered
- **THEN** each requirement SHALL be rendered as an independent Markdown table separated from other requirements by a horizontal divider
