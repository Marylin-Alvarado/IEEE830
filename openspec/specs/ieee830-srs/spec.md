## Purpose

This capability produces a Software Requirements Specification document (`requisitos.md`) following the IEEE 830-1998 standard, providing formal documentation of the SGR system's requirements, architecture, and design rationale for the thesis deliverable.

## Requirements

### Requirement: IEEE 830 SRS document
The system SHALL provide a Software Requirements Specification document (`requisitos.md`) following the IEEE 830-1998 standard structure, including a metadata header, revision history table, and per-subsection EARS validation workflow.

#### Scenario: Document metadata header
- **WHEN** the document is inspected
- **THEN** its first lines SHALL contain a metadata block with `status: proposed`, `version: 1.0`, and `authors: Marylin Alvarado`, followed by a "Historial de Revisiones" table

#### Scenario: Document contains section 1 (Introducción)
- **WHEN** the document is reviewed
- **THEN** it SHALL include: Problemática, Justificación, Objetivos, Propósito, Ámbito del producto, Definiciones y siglas, Referencias, Visión general del documento

#### Scenario: Document contains section 2 (Descripción General)
- **WHEN** the document is reviewed
- **THEN** it SHALL include: Perspectiva del producto, Funciones del producto, Características de los usuarios, Restricciones, Suposiciones y dependencias

#### Scenario: Document contains section 3 (Requisitos Específicos)
- **WHEN** the document is reviewed
- **THEN** it SHALL include: Requisitos funcionales (mapeados a app.py), Requisitos no funcionales, Interfaces externas, and a "Workflow de Validación EARS" checklist at the end of each functional subsection

### Requirement: Traceability to implementation
Every functional requirement in the IEEE 830 document SHALL reference its corresponding implementation in `app.py` or the capability specs.

#### Scenario: Code reference present
- **WHEN** a functional requirement is described
- **THEN** it SHALL include a reference to the relevant `app.py` lines or spec file

### Requirement: Spanish language
The IEEE 830 document SHALL be written entirely in Spanish.

#### Scenario: Document language
- **WHEN** the document content is inspected
- **THEN** all sections SHALL be written in Spanish

### Requirement: Revision history table
The document SHALL include a "Historial de Revisiones" table immediately after the metadata block with columns: Versión, Fecha, Autor, Descripción del Cambio.

#### Scenario: Revision history rendered
- **WHEN** the document is reviewed
- **THEN** a markdown table titled "Historial de Revisiones" SHALL exist with at least one entry documenting the initial version

### Requirement: EARS validation checklist per functional subsection
Each functional requirement subsection (3.1.1 through 3.1.13) SHALL end with a "Workflow de Validación EARS" checklist verifying that every requirement contains the keywords WHEN and THE SYSTEM SHALL.

#### Scenario: Checklist in each subsection
- **WHEN** a functional requirement subsection is inspected
- **THEN** it SHALL contain a "Workflow de Validación EARS" block with per-RF keyword checks and a general status indicator

#### Scenario: State transition to approved
- **WHEN** all requirements in the subsection pass keyword validation
- **THEN** the checklist SHALL show "Estado general: approved"
