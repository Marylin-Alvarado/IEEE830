## Why

The "Generar Requisitos con IA" button currently appears unconditionally in the main flow, visible even before any project is registered. Additionally, the `st.rerun()` at line 201 creates an infinite re-execution loop when `proyecto_guardado` is True, preventing the UI from rendering correctly after registration.

## What Changes

- Move `st.rerun()` inside the `if submitted` block so it runs once after saving, not in an infinite loop
- Guard the "Generar Requisitos con IA" button behind `st.session_state["proyecto_guardado"]` so it only appears after a successful project registration
- Keep the button outside the `with st.form` block (already the case)
- Clear `proyecto_guardado` after the rerun to prevent loop

## Capabilities

### New Capabilities
- (none)

### Modified Capabilities
- `requirements-ui`: Fix the logical flow of the AI generation button — conditional visibility on successful project registration, and fix the infinite rerun loop

## Impact

- `app.py`: Lines 200-209 restructured — button moved inside conditional block, rerun fixed
