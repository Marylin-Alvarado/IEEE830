## Why

Currently each functional requirement renders as unstructured plain markdown text (`**label:** value` stacked vertically). This makes it hard to scan and compare requirements. A structured two-column table format improves readability, visual consistency, and aligns with technical card conventions expected in engineering documentation.

## What Changes

- Replace the plain markdown rendering loop (lines 215-231) with per-requirement two-column tables
- Each requirement becomes a "Ficha Técnica Estructurada" rendered via `st.markdown()` with Markdown table syntax
- Each table has columns "Campo" and "Detalle" with rows: Identificación, Nombre, Características, Sintaxis EARS, Categoría, Prioridad
- Extract Categoría and Sintaxis as separate rows from the current combined `descripcion_ears` field

## Capabilities

### New Capabilities
- (none)

### Modified Capabilities
- `requirements-ui`: Change the "IEEE 830 requirement card display" requirement — cards must render as two-column tables instead of plain vertical text

## Impact

- `app.py`: Lines 215-231 — replace `with st.container(): st.markdown(...)` with per-requirement table rendering, parse `descripcion_ears` to extract Categoría and Sintaxis separately
