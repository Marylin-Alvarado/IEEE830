## 1. Setup

- [x] 1.1 Install streamlit and pydantic dependencies
- [x] 1.2 Create empty `app.py` entry point

## 2. Pydantic Model

- [x] 2.1 Define `Proyecto` model with `StrictStr` fields and `min_length=1`
- [x] 2.2 Add `fecha_registro` field with auto-generated timestamp
- [x] 2.3 Implement validation error handling for empty fields

## 3. Data Persistence

- [x] 3.1 Implement `cargar_proyectos()` function to read from `proyectos_sgr.json`
- [x] 3.2 Implement `guardar_proyecto()` function to append to `proyectos_sgr.json`
- [x] 3.3 Handle file-not-found case gracefully on first run

## 4. Streamlit UI - Form

- [x] 4.1 Set page title to "SGR - Sistema de Generación de Requisitos basado en IEEE 830 y EARS"
- [x] 4.2 Create form with three text inputs: Nombre del Proyecto, Objetivo General, Descripción del Dominio
- [x] 4.3 Add form submit button with Pydantic validation on submit
- [x] 4.4 Display success confirmation on save using session_state
- [x] 4.5 Display validation error messages on empty fields

## 5. Streamlit UI - Project Listing

- [x] 5.1 Load and display all projects in a Streamlit data table
- [x] 5.2 Refresh table after a new project is saved
