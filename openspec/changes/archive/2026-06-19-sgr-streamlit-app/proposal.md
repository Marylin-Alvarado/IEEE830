## Why

Software requirements specification is a critical yet often overlooked phase in software development. IEEE 830 provides a standard structure for SRS documents, and EARS (Easy Approach to Requirements Syntax) offers a taxonomy for writing clear, consistent requirements. Currently, there is no lightweight tool that guides users through creating structured requirements following both standards. This change introduces **SGR - Sistema de Generación de Requisitos**, a Streamlit-based application that simplifies project registration and sets the foundation for generating IEEE 830/EARS-compliant requirement documents.

## What Changes

- Create a new Streamlit application (`app.py`) as the SGR system entry point
- Implement a project registration form with fields: *Nombre del Proyecto*, *Objetivo General*, *Descripción del Dominio*
- Add Pydantic-based strict validation ensuring no fields are empty
- Implement JSON-based persistence to `proyectos_sgr.json`
- Display registered projects in an organized Streamlit data table with save confirmation feedback
- Add the `pydantic` and `streamlit` dependencies

## Capabilities

### New Capabilities
- `project-registration`: Form-based registration of software projects with validated fields (nombre, objetivo, dominio)
- `data-persistence`: Save projects to local JSON file and load them on app startup
- `project-listing`: Display all registered projects in a structured Streamlit table

### Modified Capabilities

*(None — this is a new application with no existing capabilities)*

## Impact

- **New file**: `app.py` — Streamlit application entry point
- **New file**: `proyectos_sgr.json` — local data store (created at runtime)
- **New dependency**: `streamlit` — UI framework
- **New dependency**: `pydantic` — data validation
