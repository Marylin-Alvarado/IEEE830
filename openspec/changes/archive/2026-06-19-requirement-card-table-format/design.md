## Context

The functional requirement rendering at `app.py:215-231` uses `st.container()` + `st.markdown()` with raw `**label:** value` per field. The `descripcion_ears` field bundles both "Categoría EARS" and "Sintaxis formal" inside a single string separated by `\n`. This design lacks visual structure and makes the category non-extractable.

## Goals / Non-Goals

**Goals:**
- Render each functional requirement as a Markdown table with two columns: Campo | Detalle
- Extract Categoría and Sintaxis EARS as separate rows from the current `descripcion_ears` field
- Apply the new format to all existing requirements (RF-01 through RF-12)

**Non-Goals:**
- No changes to data model (the dict structure stays the same)
- No changes to non-functional requirements or business rules rendering
- No new external dependencies

## Decisions

- **`st.markdown()` with inline Markdown table syntax** over `st.table()`: `st.table()` expects a DataFrame or array-like and renders a static table without the flexibility of inline markdown. Using a GFM table string inside `st.markdown()` gives full control over alignment and works with `st.container()` for per-card separation.
- **Inline parsing of `descripcion_ears`**: Split on `\n` then strip `**Categoría:** ` and `**Sintaxis:** ` prefixes using simple string operations. No regex needed — the format is consistent.
- **Keep `st.container()` wrapper**: Provides visual card separation (borders/margins). The table replaces the raw text inside each container.

## Risks / Trade-offs

- [Hidden newline in table cells] Markdown tables don't support multi-line cell content naturally. Mitigation: keep Sintaxis EARS value on a single line or use `<br>` within the cell.
- [Parsing fragility] If `descripcion_ears` format changes in the future, the split logic breaks. Mitigation: use a helper function with fallback that displays the raw string if parsing fails.
