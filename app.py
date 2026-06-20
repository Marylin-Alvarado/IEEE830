import json
import os
from datetime import datetime

import pandas as pd
import streamlit as st
from pydantic import BaseModel, Field, ValidationError

DATA_FILE = "proyectos_sgr.json"

lista_requisitos_funcionales = [
    {
        "id": "RF-01",
        "nombre": "Registro de proyectos",
        "caracteristicas": "Formulario de entrada, validación Pydantic, campos obligatorios",
        "descripcion_ears": "**Categoría:** Ubiquitous\n**Sintaxis:** El sistema SHALL proporcionar un formulario con tres campos de texto",
        "prioridad": "Alta",
    },
    {
        "id": "RF-02",
        "nombre": "Validación de datos",
        "caracteristicas": "Pydantic StrictStr, min_length=1, mensajes de error en español",
        "descripcion_ears": "**Categoría:** Ubiquitous\n**Sintaxis:** El sistema SHALL validar mediante Pydantic que ningún campo esté vacío",
        "prioridad": "Alta",
    },
    {
        "id": "RF-03",
        "nombre": "Persistencia local JSON",
        "caracteristicas": "Archivo proyectos_sgr.json, codificación UTF-8, carga automática",
        "descripcion_ears": "**Categoría:** Ubiquitous\n**Sintaxis:** El sistema SHALL guardar los proyectos en un archivo local JSON",
        "prioridad": "Alta",
    },
    {
        "id": "RF-04",
        "nombre": "Visualización de proyectos",
        "caracteristicas": "Tabla interactiva, actualización post-registro, ancho completo",
        "descripcion_ears": "**Categoría:** Ubiquitous\n**Sintaxis:** El sistema SHALL mostrar todos los proyectos registrados en una tabla interactiva",
        "prioridad": "Alta",
    },
    {
        "id": "RF-05",
        "nombre": "Retroalimentación al usuario",
        "caracteristicas": "Mensajes de éxito, manejo de errores, session_state",
        "descripcion_ears": "**Categoría:** Event-Driven\n**Sintaxis:** WHEN el usuario envía el formulario THEN el sistema SHALL mostrar un mensaje de confirmación",
        "prioridad": "Alta",
    },
    {
        "id": "RF-06",
        "nombre": "Clasificación EARS Ubicuo",
        "caracteristicas": "Detección de SHALL sin condicionales, validación sintáctica",
        "descripcion_ears": "**Categoría:** Ubiquitous\n**Sintaxis:** El sistema SHALL clasificar un requisito como Ubicuo cuando contenga SHALL sin cláusulas condicionales",
        "prioridad": "Alta",
    },
    {
        "id": "RF-07",
        "nombre": "Clasificación EARS Event-Driven",
        "caracteristicas": "Patrón WHEN-THEN, detección de disparadores",
        "descripcion_ears": "**Categoría:** Event-Driven\n**Sintaxis:** WHEN <trigger> THEN <entity> SHALL <response>",
        "prioridad": "Alta",
    },
    {
        "id": "RF-08",
        "nombre": "Clasificación EARS State-Driven",
        "caracteristicas": "Patrón WHILE, detección de estados continuos",
        "descripcion_ears": "**Categoría:** State-Driven\n**Sintaxis:** WHILE <state> <entity> SHALL <action>",
        "prioridad": "Media",
    },
    {
        "id": "RF-09",
        "nombre": "Clasificación EARS Optional",
        "caracteristicas": "Patrón WHERE, características condicionales",
        "descripcion_ears": "**Categoría:** Optional\n**Sintaxis:** WHERE <feature> <entity> SHALL <action>",
        "prioridad": "Media",
    },
    {
        "id": "RF-10",
        "nombre": "Clasificación EARS Desired",
        "caracteristicas": "Patrón SHOULD/WANT, prioridad reducida",
        "descripcion_ears": "**Categoría:** Desired\n**Sintaxis:** <entity> SHOULD <action>",
        "prioridad": "Baja",
    },
    {
        "id": "RF-11",
        "nombre": "Validación gramatical EARS",
        "caracteristicas": "Motor de validación, mensajes de error, sugerencias de corrección",
        "descripcion_ears": "**Categoría:** Ubiquitous\n**Sintaxis:** El sistema SHALL validar que cada requisito conforme a una de las cinco categorías EARS",
        "prioridad": "Alta",
    },
    {
        "id": "RF-12",
        "nombre": "Orquestación del pipeline IA",
        "caracteristicas": "Secuencia audio→transcripción→LLM→validación→SRS",
        "descripcion_ears": "**Categoría:** Event-Driven\n**Sintaxis:** WHEN el usuario inicia el flujo THEN el sistema SHALL ejecutar todas las etapas en secuencia",
        "prioridad": "Media",
    },
]

tabla_no_funcionales = [
    {"id": "RNF-01", "requisito": "Interfaz intuitiva sin necesidad de capacitación", "categoria": "Usabilidad"},
    {"id": "RNF-02", "requisito": "Mensajes de error en español descriptivos", "categoria": "Usabilidad"},
    {"id": "RNF-03", "requisito": "Visibilidad del progreso del pipeline por etapa", "categoria": "Usabilidad"},
    {"id": "RNF-04", "requisito": "Respuesta a acciones del usuario en menos de 2 segundos", "categoria": "Rendimiento"},
    {"id": "RNF-05", "requisito": "Soporte para al menos 100 proyectos sin degradación", "categoria": "Rendimiento"},
    {"id": "RNF-06", "requisito": "Inferencia LLM en menos de 30s con GPU disponible", "categoria": "Rendimiento"},
    {"id": "RNF-07", "requisito": "Manejo de ausencia de archivo de datos sin excepciones", "categoria": "Confiabilidad"},
    {"id": "RNF-08", "requisito": "Reintento de conexión LLM antes de reportar fallo", "categoria": "Confiabilidad"},
    {"id": "RNF-09", "requisito": "Preservación de datos entre reinicios de la aplicación", "categoria": "Confiabilidad"},
    {"id": "RNF-10", "requisito": "WER menor al 10% en transcripción Whisper small+", "categoria": "Precisión"},
    {"id": "RNF-11", "requisito": "Precisión de clasificación EARS mayor al 95%", "categoria": "Precisión"},
    {"id": "RNF-12", "requisito": "Código documentado con referencias a requisitos IEEE 830", "categoria": "Mantenibilidad"},
    {"id": "RNF-13", "requisito": "Validadores EARS independientes y testeables", "categoria": "Mantenibilidad"},
    {"id": "RNF-14", "requisito": "Funcionamiento con 8GB RAM mínimo", "categoria": "Hardware"},
    {"id": "RNF-15", "requisito": "Recomendación de 16GB RAM para operación completa", "categoria": "Hardware"},
    {"id": "RNF-16", "requisito": "10GB espacio libre en disco para modelos descargados", "categoria": "Hardware"},
]

reglas_negocio = [
    {
        "id": "RN-01",
        "nombre": "Fuente única de verdad",
        "descripcion": "El archivo requisitos.md es la especificación autoritativa. Los datos embebidos en app.py son una instantánea estructurada que debe sincronizarse manualmente tras cada actualización del documento.",
    },
    {
        "id": "RN-02",
        "nombre": "Clasificación EARS obligatoria",
        "descripcion": "Todo requisito funcional registrado en el sistema debe pertenecer a una de las cinco categorías EARS (Ubiquitous, Event-Driven, State-Driven, Optional, Desired). No se permiten requisitos sin clasificación.",
    },
    {
        "id": "RN-03",
        "nombre": "Prioridad por defecto",
        "descripcion": "Los requisitos clasificados como Ubiquitous o Event-Driven obtienen prioridad Alta. State-Driven y Optional obtienen prioridad Media. Desired obtiene prioridad Baja.",
    },
    {
        "id": "RN-04",
        "nombre": "Trazabilidad código-especificación",
        "descripcion": "Cada requisito funcional en la interfaz debe incluir una referencia a su implementación en app.py o a su especificación en openspec/specs/.",
    },
    {
        "id": "RN-05",
        "nombre": "Modo solo lectura",
        "descripcion": "La interfaz de visualización de requisitos es de solo lectura. No se permite editar, eliminar ni reordenar requisitos desde la UI.",
    },
    {
        "id": "RN-06",
        "nombre": "Ejecución local obligatoria",
        "descripcion": "Todos los componentes del pipeline IA (Whisper, LLM) deben ejecutarse localmente. No está permitido el uso de servicios en la nube para procesamiento de datos.",
    },
]

class Proyecto(BaseModel):
    nombre_proyecto: str = Field(..., min_length=1, strict=True)
    objetivo_general: str = Field(..., min_length=1, strict=True)
    descripcion_dominio: str = Field(..., min_length=1, strict=True)
    fecha_registro: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def cargar_proyectos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_proyecto(proyecto: Proyecto):
    proyectos = cargar_proyectos()
    proyectos.append(proyecto.model_dump())
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(proyectos, f, ensure_ascii=False, indent=2)


st.set_page_config(
    page_title="SGR - Sistema de Generación de Requisitos basado en IEEE 830 y EARS",
    layout="centered",
)

st.title("SGR - Sistema de Generación de Requisitos")
st.markdown("Basado en **IEEE 830** y **EARS**")

with st.form("registro_proyecto"):
    nombre = st.text_input("Nombre del Proyecto")
    objetivo = st.text_area("Objetivo General")
    dominio = st.text_area("Descripción del Dominio")
    submitted = st.form_submit_button("Registrar Proyecto")

if submitted:
    try:
        proyecto = Proyecto(
            nombre_proyecto=nombre,
            objetivo_general=objetivo,
            descripcion_dominio=dominio,
        )
        guardar_proyecto(proyecto)
        st.success("Proyecto registrado exitosamente.")
        st.session_state["proyecto_guardado"] = True
    except ValidationError as e:
        for error in e.errors():
            campo = error["loc"][0]
            st.error(f"El campo '{campo}' no puede estar vacío.")

if st.session_state.get("proyecto_guardado"):
    st.rerun()

proyectos = cargar_proyectos()
if proyectos:
    st.subheader("Proyectos Registrados")
    st.dataframe(proyectos, use_container_width=True)

if st.button("Generar Requisitos con IA"):
    st.session_state["mostrar_requisitos"] = True

if st.session_state.get("mostrar_requisitos"):
    st.markdown("---")
    st.markdown("### 3.1 Requerimientos Funcionales")
    st.markdown("Clasificados según **EARS** (Easy Approach to Requirements Syntax)")

    for req in lista_requisitos_funcionales:
        with st.container():
            st.markdown(
                f"""
**Identificación del requerimiento:** {req['id']}

**Nombre del requerimiento:** {req['nombre']}

**Características:** {req['caracteristicas']}

**Descripción del requerimiento (Sintaxis EARS):**  
{req['descripcion_ears']}

**Prioridad del requerimiento:** {req['prioridad']}
"""
            )
            st.markdown("---")

    st.markdown("### 3.2 Requerimientos No Funcionales")
    df_nfr = pd.DataFrame(tabla_no_funcionales).rename(
        columns={"id": "ID", "requisito": "Requisito", "categoria": "Categoría"}
    )
    st.dataframe(df_nfr, use_container_width=True)

    st.markdown("### 3.3 Reglas de Negocio")
    for i, regla in enumerate(reglas_negocio, start=1):
        st.markdown(f"{i}. **{regla['nombre']}:** {regla['descripcion']}")
