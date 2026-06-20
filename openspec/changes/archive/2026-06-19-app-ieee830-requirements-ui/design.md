## Context

The current `app.py` (67 lines) implements a project registration system with Pydantic validation and JSON persistence. The IEEE 830 specification content exists as a separate document (`requisitos.md`, ~810 lines) but is not rendered interactively in the application. The goal is to add a "Generar Requisitos con IA" button that ingests structured requirement data and renders three visual blocks: vertical technical cards for functional requirements (with EARS syntax), a matrix table for non-functional requirements, and an indexed list for business rules — all within the existing Streamlit UI.

## Goals / Non-Goals

**Goals:**
- Add a "Generar Requisitos con IA" button below the project registration form
- Define structured in-memory requirement data (functional, non-functional, business rules) directly in `app.py` based on the IEEE 830/EARS spec content
- Render each functional requirement as a vertical card with fields: Identificación del requerimiento, Nombre del requerimiento, Características, Descripción del requerimiento (Sintaxis EARS), Prioridad del requerimiento
- Render "3.2 Requerimientos No Funcionales" as an interactive matrix table below the cards
- Render "3.3 Reglas de Negocio" as a formal indexed list below the table

**Non-Goals:**
- External LLM/AI integration (Ollama/LlamaCpp) — the spec data is embedded; no inference calls
- Modifying the `requisitos.md` specification document
- Editing or deleting requirements from the UI (read-only display)
- Authentication or multi-user support

## Decisions

1. **Embedded structured data over dynamic parsing** — Requirement data is defined as Python dicts/lists directly in `app.py` rather than parsing `requisitos.md` at runtime. Rationale: avoids runtime parsing complexity, keeps the UI layer deterministic, and maintains a single source of truth in the spec document while the code contains a structured snapshot.

2. **Streamlit native components for cards** — Use `st.container` + `st.markdown` with custom formatting for vertical cards rather than `st.metric` or custom HTML. Rationale: stays within Streamlit's sandbox (no raw HTML/CSS), maintains consistent theming, and supports markdown formatting for EARS syntax highlighting.

3. **`st.dataframe` for matrix table** — Non-functional requirements rendered via `st.dataframe` with renamed columns. Rationale: native sort/filter, uses container width, consistent with existing project listing table.

4. **`st.markdown` with ordered list for business rules** — Business rules rendered as a numbered markdown list. Rationale: simple, formal presentation, no interactive features needed.

5. **Session state toggle** — The "Generar Requisitos con IA" button sets `st.session_state["mostrar_requisitos"] = True`, which controls visibility of the requirements blocks. Rationale: avoids URL params, works with `st.rerun()`, maintains state across interactions.

## Risks / Trade-offs

- **Data duplication** — Requirement data exists in both `requisitos.md` and in `app.py`. Mitigation: the app.py data is a structured snapshot; the spec document remains the authoritative source.
- **Stale data risk** — If `requisitos.md` is updated, the embedded data in `app.py` may become outdated. Mitigation: requirement sync is a manual verification step in the tasks.
