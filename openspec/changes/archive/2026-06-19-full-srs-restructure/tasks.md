## 1. Form Restructuring (Outside `with st.form`)

- [x] 1.1 Move nombre/objetivo/dominio to `st.session_state` keys with defaults
- [x] 1.2 Replace `with st.form` block with standalone inputs and a button that reads from session state
- [x] 1.3 Validate and save project on button click, set `proyecto_guardado` flag

## 2. Introducción Científica (Section 1)

- [x] 2.1 Add static content for 1.1 Problemática from requisitos.md
- [x] 2.2 Add static content for 1.2 Justificación from requisitos.md
- [x] 2.3 Add static content for 1.3 Objetivos Generales y Específicos from requisitos.md

## 3. NFR Data Update

- [x] 3.1 Replace `tabla_no_funcionales` data with new categories: Eficiencia, Seguridad, Portabilidad

## 4. New Mermaid Diagrams

- [x] 4.1 Add Class UML diagram string (`classDiagram` showing Proyecto model with fields and types)
- [x] 4.2 Add Deployment UML diagram string (nodes: Streamlit, JSON, Whisper, LLM)

## 5. Traceability Matrix

- [x] 5.1 Add traceability matrix data mapping RF-01–RF-12 to code components

## 6. Rendering Reorder

- [x] 6.1 Replace all rendering blocks to follow rubric hierarchy: 1. Introducción → 2. Resultados → 3. Arquitectura
- [x] 6.2 Add rendering for Class Diagram and Deployment Diagram under 2.2
- [x] 6.3 Add rendering for traceability matrix under 2.3
