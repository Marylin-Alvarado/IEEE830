## MODIFIED Requirements

### Requirement: Non-functional requirements matrix table
The system SHALL render section "3.2 Requerimientos No Funcionales" as an interactive matrix table below the functional requirement cards, organized by the quality attributes Eficiencia, Seguridad, and Portabilidad.

#### Scenario: Table displays NFRs by new categories
- **WHEN** the non-functional requirements section is rendered
- **THEN** the system SHALL display a `st.dataframe` with columns for ID, requisito, and categoria (Eficiencia, Seguridad, Portabilidad)

## ADDED Requirements

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
