## 1. Define Structured Requirement Data

- [x] 1.1 Define lista_requisitos_funcionales as a list of dicts with fields: id, nombre, caracteristicas, descripcion_ears, prioridad — covering all EARS categories (Ubiquitous, Event-Driven, State-Driven, Optional, Desired)
- [x] 1.2 Define tabla_no_funcionales as a list of dicts with fields: id, requisito, categoria — covering usabilidad, rendimiento, confiabilidad, precisión, mantenibilidad, hardware
- [x] 1.3 Define reglas_negocio as a list of dicts with fields: id, nombre, descripcion — covering operational constraints and business policies

## 2. Add Button and Session State Toggle

- [x] 2.1 Add "Generar Requisitos con IA" button after the project dataframe using `st.button`
- [x] 2.2 Implement session state toggle: set `st.session_state["mostrar_requisitos"]` on click
- [x] 2.3 Add conditional rendering block guarded by `st.session_state.get("mostrar_requisitos")`

## 3. Implement Functional Requirement Cards

- [x] 3.1 Add section header "### 3.1 Requerimientos Funcionales" with IEEE 830/EARS subtitle
- [x] 3.2 Iterate over lista_requisitos_funcionales and render each as a vertical card inside `st.container`
- [x] 3.3 For each card, render all five fields in order: Identificación del requerimiento, Nombre del requerimiento, Características, Descripción del requerimiento (Sintaxis EARS), Prioridad del requerimiento — using `st.markdown` with bold labels

## 4. Implement Non-Functional Requirements Matrix Table

- [x] 4.1 Add section header "### 3.2 Requerimientos No Funcionales"
- [x] 4.2 Convert tabla_no_funcionales into a pandas DataFrame with Spanish column headers
- [x] 4.3 Render as `st.dataframe` with `use_container_width=True`

## 5. Implement Business Rules Indexed List

- [x] 5.1 Add section header "### 3.3 Reglas de Negocio"
- [x] 5.2 Render reglas_negocio as a numbered markdown list using `st.markdown`, each item as `**<name>**: <description>`

## 6. Final Review

- [x] 6.1 Run `app.py` with `streamlit run app.py` and verify the button, cards, table, and list render correctly
- [x] 6.2 Verify all five card fields are present and correctly labeled
- [x] 6.3 Verify non-functional table has correct columns and data
- [x] 6.4 Verify business rules list is numbered and formatted
