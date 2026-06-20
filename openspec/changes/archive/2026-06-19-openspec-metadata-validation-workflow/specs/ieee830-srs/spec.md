## ADDED Requirements

### Requirement: Document metadata block
The IEEE 830 document SHALL include a metadata header with `status`, `version`, and `authors` fields, and a "Historial de Revisiones" table tracking all document versions.

#### Scenario: Metadata presence
- **WHEN** the document is read
- **THEN** the top of the document SHALL contain `status: proposed`, `version: 1.0`, and `authors: Marylin Alvarado`

#### Scenario: Revision history
- **WHEN** the document is reviewed
- **THEN** a "Historial de Revisiones" table SHALL be present below the metadata with columns: Versión, Fecha, Autor, Descripción del Cambio

### Requirement: EARS validation workflow per functional requirement
Each functional requirement subsection SHALL include a "Workflow de Validación EARS" checklist that validates keyword presence and tracks approval state.

#### Scenario: Checklist in each subsection
- **WHEN** a functional requirement subsection (3.1.1–3.1.13) is inspected
- **THEN** it SHALL contain a "Workflow de Validación EARS" checklist block

#### Scenario: State transition to approved
- **WHEN** all requirements in the subsection pass keyword validation
- **THEN** the checklist SHALL show `Estado: approved`

## MODIFIED Requirements

### Requirement: IEEE 830 SRS document
The system SHALL provide a Software Requirements Specification document (`requisitos.md`) following the IEEE 830-1998 standard structure, including a metadata header, revision history table, and per-subsection EARS validation workflow.

#### Scenario: Document contains section 1 (Introducción)
- **WHEN** the document is reviewed
- **THEN** it SHALL include: Problemática, Justificación, Objetivos, Propósito, Ámbito del producto, Definiciones y siglas, Referencias, Visión general del documento

#### Scenario: Document contains section 2 (Descripción General)
- **WHEN** the document is reviewed
- **THEN** it SHALL include: Perspectiva del producto, Funciones del producto, Características de los usuarios, Restricciones, Suposiciones y dependencias

#### Scenario: Document contains section 3 (Requisitos Específicos)
- **WHEN** the document is reviewed
- **THEN** it SHALL include: Requisitos funcionales (mapeados a app.py), Requisitos no funcionales, Interfaces externas, and a Workflow de Validación EARS at the end of each functional subsection
