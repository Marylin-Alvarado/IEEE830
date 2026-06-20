## Context

Currently `app.py` has two bugs in the post-registration flow:
1. Lines 200-201: `if st.session_state.get("proyecto_guardado"): st.rerun()` creates an infinite re-execution loop because the flag is never cleared
2. Lines 208-209: The "Generar Requisitos con IA" button appears unconditionally, even before any project is registered

## Goals / Non-Goals

**Goals:**
- Move `st.rerun()` inside the `if submitted` block (runs once after save, not in a loop)
- Guard the "Generar Requisitos con IA" button behind `proyecto_guardado`
- Button stays visible after registration (no need to show it only once)

**Non-Goals:**
- No changes to the requirements card rendering logic
- No changes to data model or form validation
- No changes to spec files

## Decisions

- **`st.rerun()` inside submitted block**: Called once after `guardar_proyecto()` succeeds, ensuring the project list refreshes. After rerun, `proyecto_guardado` remains True but without triggering another rerun.
- **Button guarded by `proyecto_guardado`**: After rerun, the condition `st.session_state.get("proyecto_guardado")` is True, so the button renders. On fresh load (no registration yet), it's False, button hidden.
- **`st.rerun()` not needed on the button path**: When the user clicks "Generar Requisitos con IA", only `mostrar_requisitos` is set — no rerun needed, the display section below reacts immediately.

## Risks / Trade-offs

- **Button persists forever after first registration**: The button remains visible for the entire session once a project is registered. Mitigation: acceptable UX — having registered at least one project implies the user is ready for requirements generation.
