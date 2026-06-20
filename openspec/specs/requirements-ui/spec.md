# Requirements UI

## Purpose

Define the capabilities for rendering IEEE 830 requirement data (functional requirement cards, non-functional requirements matrix, and business rules) in the Streamlit user interface, with toggle visibility controlled by session state.

## Requirements

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

### Requirement: Non-functional requirements matrix table
The system SHALL render section "3.2 Requerimientos No Funcionales" as an interactive matrix table below the functional requirement cards, organized by the quality attributes Eficiencia, Seguridad, and Portabilidad.

#### Scenario: Table displays NFRs by new categories
- **WHEN** the non-functional requirements section is rendered
- **THEN** the system SHALL display a `st.dataframe` with columns for ID, requisito, and categoria (Eficiencia, Seguridad, Portabilidad)

### Requirement: Business rules indexed list
The system SHALL render section "3.3 Reglas de Negocio" as a formal numbered list below the non-functional requirements table.

#### Scenario: Business rules displayed
- **WHEN** the business rules section is rendered
- **THEN** the system SHALL display each rule as a numbered item (1., 2., 3., ...) with bold rule name followed by the rule description

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

### Requirement: Class UML diagram via Mermaid
The system SHALL display a Mermaid `classDiagram` block in section "2.2 Código Generado e Implementado" showing the Pydantic data models with attributes, methods, and Python data types.

#### Scenario: Class diagram shows Proyecto model
- **WHEN** the class diagram section is rendered
- **THEN** the system SHALL display the `Proyecto` class with fields (`nombre_proyecto`, `objetivo_general`, `descripcion_dominio`, `fecha_registro`) and their Python types

### Requirement: Deployment UML diagram via Mermaid
The system SHALL display a Mermaid deployment diagram in section "2.2 Código Generado e Implementado" showing the local Streamlit environment, JSON persistence, and AI infrastructure.

#### Scenario: Deployment diagram shows nodes
- **WHEN** the deployment diagram section is rendered
- **THEN** the system SHALL display nodes for "Streamlit Local", "proyectos_sgr.json", "Whisper Local", and "LLM Local (Ollama)"

### Requirement: Traceability matrix table
The system SHALL render a formal Markdown traceability matrix in section "2.3 Validación, Coherencia y Análisis" mapping each functional requirement to its corresponding software component.

#### Scenario: Matrix shows 100% traceability
- **WHEN** the traceability matrix is rendered
- **THEN** the system SHALL display a table with columns "Requerimiento", "Componente", and "Estado" demonstrating no discrepancies

### Requirement: Introducción Científica section display
The system SHALL render static sections 1.1 Problemática, 1.2 Justificación, and 1.3 Objetivos with content extracted from the `requisitos.md` document.

#### Scenario: Introduction shown in rubric order
- **WHEN** the specifications are displayed
- **THEN** the sections SHALL appear in the order: 1. Introducción Científica → 2. Resultados de Ingeniería → 3. Arquitectura y Requisitos Base

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
