## Context

SGR (Sistema de Generación de Requisitos) is a greenfield Streamlit application for registering software projects as the first step toward IEEE 830 / EARS-compliant requirements generation. The initial scope is a single-page app with a registration form, Pydantic validation, and JSON file persistence. No existing codebase or infrastructure exists — this is built from scratch.

## Goals / Non-Goals

**Goals:**
- Provide a clean Streamlit form for project registration with three fields
- Enforce strict validation via Pydantic (no empty strings allowed)
- Persist projects to a local `proyectos_sgr.json` file
- Display all registered projects in a Streamlit data table
- Show a success confirmation on save

**Non-Goals:**
- User authentication or multi-user support
- Database backend (SQL, NoSQL)
- IEEE 830 / EARS document generation (future capability)
- Editing or deleting existing projects
- Cloud deployment or hosting configuration

## Decisions

1. **Streamlit over Flask/FastAPI** — Streamlit provides the fastest path to a functional UI with forms, data tables, and state management out of the box. No HTML/JS/CSS required. For a tool focused on form input and data display, it is the right fit.

2. **Pydantic v2 BaseModel with `StrictStr`** — Using `pydantic.BaseModel` with fields typed as `StrictStr` ensures empty strings are rejected at the model level before any business logic runs. `StrictStr` does not coerce non-string values and rejects empty strings when combined with `min_length=1`.

3. **JSON file as storage** — A local JSON file (`proyectos_sgr.json`) is the simplest persistence layer for a single-user desktop-style tool. No database setup, no migrations. The file is read on startup and written on each registration. Concurrent writes are not a concern for single-user usage.

4. **Session state for UI flow** — Streamlit `session_state` is used to track whether a project was just saved, enabling the success confirmation message. This avoids page re-run issues with Streamlit's execution model.

## Risks / Trade-offs

- **No concurrency safety** — JSON file writes are not atomic. If the app is ever used concurrently, data loss is possible. For the intended single-user scope, this is acceptable.
- **Data grows unbounded** — No pagination or search. If hundreds of projects accumulate, the table may become unwieldy. Acceptable for the MVP.
- **Streamlit re-run model** — Every interaction triggers a full script re-run. The JSON file is re-read on every re-run, which is fine for small datasets but could be slow with thousands of records.
