## 1. Corregir Rerun Infinito

- [x] 1.1 Mover `st.rerun()` dentro del bloque `if submitted` inmediatamente después de `st.session_state["proyecto_guardado"] = True`
- [x] 1.2 Eliminar el bloque `if st.session_state.get("proyecto_guardado"): st.rerun()` independiente (líneas 200-201)

## 2. Condicionar Botón de IA

- [x] 2.1 Envolver el `if st.button("Generar Requisitos con IA")` dentro de `if st.session_state.get("proyecto_guardado"):` para que solo aparezca tras registrar un proyecto
- [x] 2.2 Verificar que el botón renderiza correctamente después del registro y que los requisitos se muestran al hacer clic
