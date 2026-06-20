## Purpose

This capability defines the formal metadata and revision history requirements for the IEEE 830 Software Requirements Specification document (`requisitos.md`), providing traceability of document versions and authorship.

## Requirements

### Requirement: Metadata block at document header
The IEEE 830 document SHALL include a YAML-style metadata block at the top, before the main title, containing `status`, `version`, and `authors` fields.

#### Scenario: Metadata fields present
- **WHEN** the document header is inspected
- **THEN** the first non-comment lines SHALL contain `status: proposed`, `version: 1.0`, and `authors: Marylin Alvarado`

### Requirement: Revision history table
The document SHALL include a "Historial de Revisiones" table immediately below the metadata block with columns: Versión, Fecha, Autor, Descripción del Cambio.

#### Scenario: Revision history rendered
- **WHEN** the document is reviewed
- **THEN** a markdown table titled "Historial de Revisiones" SHALL exist with entries for each revision version

#### Scenario: Initial revision entry
- **WHEN** the document is first created
- **THEN** the revision history SHALL contain at least one row: v1.0, current date, Marylin Alvarado, "Versión inicial del documento ERS IEEE 830"
