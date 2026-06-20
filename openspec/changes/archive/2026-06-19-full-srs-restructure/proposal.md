## Why

The current `app.py` displays sections in an order that doesn't match the IEEE 830–based evaluation rubric (APE). The rubric requires a specific hierarchy: Introducción Científica → Resultados de Ingeniería (2.1, 2.2, 2.3) → Arquitectura Base (3.1, 3.2, 3.3). Additionally, the form logic uses `with st.form` which can cause re-render issues, the NFR categories are outdated, and the app lacks Class UML, Deployment UML, and a traceability matrix.

## What Changes

- **Restructure form processing**: Move form submission handling outside `with st.form` using `st.session_state` flags
- **Add Introducción Científica**: Static sections 1.1, 1.2, 1.3 with content from `requisitos.md`
- **Add 2.2 Código Generado e Implementado**: Mermaid Class Diagram + Deployment Diagram
- **Add 2.3 Validación, Coherencia y Análisis**: Traceability matrix table
- **Update NFR categories**: Replace current categories (Usabilidad, Rendimiento, Confiabilidad, etc.) with Eficiencia, Seguridad, Portabilidad
- **Reorder sections**: Match the exact rubric hierarchy
- **Update `requirements-ui` spec**: New rendering sections and NFR categories

## Capabilities

### New Capabilities
- (none)

### Modified Capabilities
- `requirements-ui`: Complete restructure — new section hierarchy, new NFR categories, Class/Deployment diagrams, traceability matrix

## Impact

- `app.py`: Complete rewrite of the rendering section (~200 lines changed); form logic restructured; NFR data replaced; 2 new Mermaid diagrams added; traceability matrix added; prompt template updated
- `openspec/specs/requirements-ui/spec.md`: Updated to reflect new section hierarchy and diagram requirements
