## Context

The app currently renders sections in a flat order (3.1, 3.2, 3.3, then 2.1–2.4). The rubric mandates a hierarchical structure: Introducción Científica → Resultados de Ingeniería (with 3 sub-sections) → Arquitectura Base. The form is inside `with st.form`, which causes Streamlit to re-run the form block on every interaction.

## Goals / Non-Goals

**Goals:**
- Reorder all sections to match the exact rubric hierarchy
- Move form submit processing outside `with st.form` via `st.session_state` flags
- Replace NFR categories with Eficiencia, Seguridad, Portabilidad
- Add Class Diagram (Pydantic models, attributes, methods, types)
- Add Deployment Diagram (Streamlit, JSON persistence, Whisper/LLM infra)
- Add traceability matrix mapping requirements to code components

**Non-Goals:**
- No changes to the 12 functional requirement cards or business rules logic
- No actual LLM HTTP call (prompt template remains prepared but unused)

## Decisions

- **Form via `st.session_state` instead of `with st.form`**: Store form field values in `st.session_state` keys. A "Registrar Proyecto" button outside the form block checks the session state, validates with Pydantic, and saves. This avoids the re-render loop issue entirely.
- **Class Diagram models mapped from actual Pydantic code**: The UML class diagram shows `Proyecto` with its fields (`nombre_proyecto: str`, `objetivo_general: str`, etc.) and the helper functions as class methods, plus the data structures (`lista_requisitos_funcionales`, etc.) as domain classes.
- **Traceability matrix as static Markdown table**: Maps each RF-0X to its corresponding Python function/module in `app.py`, demonstrating 100% sync.
- **NFR categories replaced entirely**: Old data (Usabilidad, Rendimiento, etc.) swapped for Eficiencia, Seguridad, Portabilidad with matching requirements.

## Risks / Trade-offs

- [Form breaking change] Removing `with st.form` changes the submission UX. Mitigation: add clear `st.success`/`st.error` feedback and maintain the same visual flow.
- [Static traceability matrix] The matrix is hardcoded and must be manually updated if RFs change. Mitigation: keep it short and document the sync rule in the business rules.
