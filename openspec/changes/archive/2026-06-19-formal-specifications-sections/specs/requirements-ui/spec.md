## ADDED Requirements

### Requirement: Formal specifications section display
The system SHALL render four formal specification sections (2.1–2.4) below the business rules when the "Generar Requisitos con IA" button is activated.

#### Scenario: Spech & Tech Specifications rendered
- **WHEN** the formal specifications section is shown
- **THEN** the system SHALL display "## 2.1 Spech & Tech Specifications" with architecture, API, and schema descriptions

#### Scenario: User Stories rendered with Gherkin
- **WHEN** the formal specifications section is shown
- **THEN** the system SHALL display "## 2.2 Historias de Usuario" with at least 3 stories in "Como [rol], quiero [acción], para [beneficio]" format, each with Gherkin acceptance criteria (Dado, Cuando, Entonces)

#### Scenario: Use Case UML diagram rendered via Mermaid
- **WHEN** the formal specifications section is shown
- **THEN** the system SHALL display a Mermaid `graph TD` diagram showing actors (Analista, Revisor) and their interactions with the SGR system

#### Scenario: Sequence UML diagram rendered via Mermaid
- **WHEN** the formal specifications section is shown
- **THEN** the system SHALL display a Mermaid `sequenceDiagram` showing the temporal flow: Streamlit UI → Pydantic validation → LLM query → proyectos_sgr.json persistence
