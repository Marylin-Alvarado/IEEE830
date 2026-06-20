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
    {"id": "RNF-01", "requisito": "Tiempo de respuesta del pipeline IA menor a 30 segundos con GPU disponible", "categoria": "Eficiencia"},
    {"id": "RNF-02", "requisito": "Uso de memoria RAM no superior a 8GB en operación normal", "categoria": "Eficiencia"},
    {"id": "RNF-03", "requisito": "Procesamiento de transcripción de audio en tiempo real sin bloqueo de la UI", "categoria": "Eficiencia"},
    {"id": "RNF-04", "requisito": "Validación de datos de entrada contra inyección de código malicioso en campos de texto", "categoria": "Seguridad"},
    {"id": "RNF-05", "requisito": "Ejecución local de todos los modelos de IA sin transmisión de datos a terceros", "categoria": "Seguridad"},
    {"id": "RNF-06", "requisito": "Aislamiento de datos entre proyectos registrados en el mismo archivo JSON", "categoria": "Seguridad"},
    {"id": "RNF-07", "requisito": "Capacidad de exportar el SRS generado a formato PDF compatible con IEEE 830", "categoria": "Portabilidad"},
    {"id": "RNF-08", "requisito": "Funcionamiento en sistemas Windows y Linux sin modificaciones en el código fuente", "categoria": "Portabilidad"},
    {"id": "RNF-09", "requisito": "Soporte para backends de inferencia Ollama y LlamaCpp intercambiables mediante variable de entorno", "categoria": "Portabilidad"},
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


def parse_descripcion_ears(raw: str) -> tuple[str, str]:
    parts = raw.split("\n")
    categoria = ""
    sintaxis = ""
    for part in parts:
        part = part.strip()
        if part.startswith("**Categoría:**"):
            categoria = part.replace("**Categoría:** ", "")
        elif part.startswith("**Sintaxis:**"):
            sintaxis = part.replace("**Sintaxis:** ", "")
    return categoria, sintaxis


LLM_PROMPT_TEMPLATE = """Eres un analista de sistemas experto en IEEE 830 y EARS. Dado un proyecto de software con su objetivo general y descripción del dominio, genera una especificación de requisitos completa. Debes incluir OBLIGATORIAMENTE los siguientes bloques con la sintaxis exacta indicada:

## 2.1 Spech & Tech Specifications
Describe la arquitectura del backend, las APIs involucradas y los esquemas de datos.

## 2.2 Historias de Usuario (User Stories)
Escribe al menos 3 historias de usuario siguiendo el formato:
Como [rol], quiero [acción], para [beneficio]
Cada historia debe incluir criterios de aceptación en formato Gherkin:
- Dado [contexto inicial]
- Cuando [acción ejecutada]
- Entonces [resultado esperado]

## 2.3 Diagrama de Casos de Uso (UML)
Utiliza sintaxis Mermaid graph TD para representar actores y casos de uso.

## 2.4 Diagrama de Secuencia (UML)
Utiliza sintaxis Mermaid sequenceDiagram para representar el flujo desde la UI hasta la persistencia.

Los diagramas Mermaid deben ir dentro de bloques de código ```mermaid ... ```."""


def sanitize_output(text: str) -> str:
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        if line.strip().startswith("```") and "mermaid" not in line and line.strip() != "```":
            line = line.replace("`", "")
        cleaned.append(line)
    return "\n".join(cleaned)


example_spech_tech = {
    "arquitectura": "Backend monolítico en Python con Streamlit como capa de presentación y Pydantic para validación de datos en la capa de dominio.",
    "api": "API interna basada en funciones Python (cargar_proyectos, guardar_proyecto) sin framework HTTP. La comunicación entre componentes es síncrona y en memoria.",
    "esquemas": "Proyecto: {nombre_proyecto: str, objetivo_general: str, descripcion_dominio: str, fecha_registro: str}. Persistencia en JSON local con codificación UTF-8.",
}

example_user_stories = [
    {
        "rol": "Analista de requisitos",
        "accion": "transcribir entrevistas grabadas mediante Whisper",
        "beneficio": "obtener un texto fiable sin depender de notas manuales",
        "aceptacion": "Dado que tengo un archivo de audio de una entrevista\nCuando ejecuto la transcripción con Whisper\nEntonces obtengo el texto completo con una precisión mayor al 90%",
    },
    {
        "rol": "Revisor de especificaciones",
        "accion": "visualizar los requisitos generados clasificados por categoría EARS",
        "beneficio": "verificar que cada requisito cumple la sintaxis formal antes de aprobarlo",
        "aceptacion": "Dado que los requisitos han sido generados por el LLM\nCuando los visualizo en la interfaz\nEntonces cada requisito muestra su categoría EARS y su sintaxis formal",
    },
    {
        "rol": "Desarrollador",
        "accion": "consultar el diagrama de secuencia del pipeline",
        "beneficio": "entender el flujo completo desde la UI hasta la persistencia",
        "aceptacion": "Dado que el sistema ha generado la especificación formal\nCuando reviso el diagrama de secuencia\nEntonces encuentro representados la UI, Pydantic, el LLM y el archivo JSON",
    },
]

example_diagrama_casos_uso = """```mermaid
graph TD
    A[Analista] -->|Transcribe entrevista| SGR(SGR)
    A -->|Revisa requisitos EARS| SGR
    R[Revisor] -->|Valida especificación| SGR
    R -->|Aprueba o solicita cambios| SGR
    SGR -->|Genera SRS| D[Documento IEEE 830]
    SGR -->|Persiste| J[(proyectos_sgr.json)]
    SGR -->|Consulta| L[LLM Local]
    SGR -->|Transcribe| W[Whisper Local]
"""

example_diagrama_secuencia = """```mermaid
sequenceDiagram
    participant UI as Streamlit UI
    participant PV as Pydantic Validation
    participant LLM as LLM (Ollama)
    participant FS as proyectos_sgr.json

    UI->>PV: Envía datos del formulario
    PV-->>UI: Validación exitosa / Error
    UI->>LLM: Solicita generación de requisitos
    LLM-->>UI: Requisitos + Especificaciones formales
    UI->>FS: Guarda proyecto registrado
    FS-->>UI: Confirmación de persistencia
    UI->>UI: Renderiza diagramas Mermaid
"""

example_diagrama_clases = """```mermaid
classDiagram
    class Proyecto {
        +nombre_proyecto: str
        +objetivo_general: str
        +descripcion_dominio: str
        +fecha_registro: str
        +model_dump() dict
    }
    class GestorArchivos {
        +cargar_proyectos() list
        +guardar_proyecto(proyecto) None
    }
    class ValidadorEARS {
        +parse_descripcion_ears(raw) tuple
        +sanitize_output(text) str
    }
    class InterfazUI {
        +renderizar_formulario() None
        +mostrar_requisitos() None
    }
    Proyecto --> GestorArchivos : persiste
    InterfazUI --> Proyecto : valida
    InterfazUI --> ValidadorEARS : formatea
"""

example_diagrama_despliegue = """```mermaid
graph TB
    subgraph "Usuario Local"
        ST[Streamlit Browser]
    end
    subgraph "Backend Python"
        AP[app.py]
        PD[Pydantic Models]
    end
    subgraph "Persistencia"
        JSON[(proyectos_sgr.json)]
    end
    subgraph "Infraestructura IA"
        OL[Ollama / LlamaCpp]
        WH[Whisper Local]
    end
    ST <--> AP
    AP <--> PD
    AP <--> JSON
    AP <--> OL
    AP <--> WH
"""

matriz_trazabilidad = [
    {"requerimiento": "RF-01 Registro de proyectos", "componente": "st.text_input / Proyecto() / guardar_proyecto()", "estado": "Sincronizado"},
    {"requerimiento": "RF-02 Validación de datos", "componente": "Pydantic StrictStr / ValidationError", "estado": "Sincronizado"},
    {"requerimiento": "RF-03 Persistencia local JSON", "componente": "cargar_proyectos() / guardar_proyecto()", "estado": "Sincronizado"},
    {"requerimiento": "RF-04 Visualización de proyectos", "componente": "st.dataframe(proyectos)", "estado": "Sincronizado"},
    {"requerimiento": "RF-05 Retroalimentación al usuario", "componente": "st.success() / st.error() / session_state", "estado": "Sincronizado"},
    {"requerimiento": "RF-06 a RF-10 Clasificación EARS", "componente": "parse_descripcion_ears() / tabla RF", "estado": "Sincronizado"},
    {"requerimiento": "RF-11 Validación gramatical EARS", "componente": "parse_descripcion_ears() con 5 categorías", "estado": "Sincronizado"},
    {"requerimiento": "RF-12 Orquestación pipeline IA", "componente": "LLM_PROMPT_TEMPLATE / sanitize_output()", "estado": "Sincronizado"},
]

introduccion = {
    "problematica": (
        "La ingeniería de requisitos constituye una de las fases más críticas y propensas a errores en el ciclo de vida "
        "del desarrollo de software. Estudios ampliamente reconocidos en la literatura (Standish Group, 1994-2020; CHAOS Report) "
        "indican que los requisitos incorrectos, incompletos o ambiguos son la causa principal del fracaso de proyectos de software, "
        "representando entre el 40% y el 60% de los defectos descubiertos en etapas tardías del desarrollo.\n\n"
        "El levantamiento tradicional de requisitos enfrenta tres problemáticas fundamentales:\n"
        "- **Ambigüedad en la comunicación oral.** Las entrevistas con partes interesadas adolecen de ambigüedad inherente "
        "al lenguaje natural, generando requisitos que pueden ser interpretados de múltiples formas.\n"
        "- **Pérdida de información en reuniones.** La dependencia de la memoria humana y notas manuales introduce un sesgo "
        "de selección significativo, omitiendo detalles contextuales y matices.\n"
        "- **Falta de estructura formal en la documentación.** La redacción en lenguaje natural sin restricciones formales "
        "produce especificaciones inconsistentes con distintos niveles de abstracción."
    ),
    "justificacion": (
        "La selección de LLM y Whisper como base tecnológica del SGR se fundamenta en:\n\n"
        "- **Transcripción automatizada con Whisper.** Modelo ASR con arquitectura encoder-decoder basada en transformers, "
        "WER inferior al 10% en español con modelo small, ejecución local sin dependencia cloud.\n\n"
        "- **Generación de requisitos mediante LLM.** Los modelos de lenguaje pueden generar requisitos funcionales y no "
        "funcionales con estructura cercana a la producción humana mediante prompt engineering con restricciones EARS.\n\n"
        "- **Validación gramatical EARS.** La sintaxis EARS (Mavin et al., 2009) define cinco categorías sintácticas "
        "(Ubiquitous, Event-Driven, State-Driven, Optional, Desired) que eliminan ambigüedad.\n\n"
        "- **Ejecución local y soberanía de datos.** Todos los componentes se ejecutan localmente mediante Ollama o LlamaCpp, "
        "eliminando costos recurrentes de API y garantizando privacidad.\n\n"
        "- **Contribución al estado del arte.** Integración sinérgica Whisper + LLM + EARS en un pipeline unificado y "
        "ejecutable localmente, no identificado previamente en la literatura."
    ),
    "objetivo_general": "Desarrollar e implementar un Sistema de Generación de Requisitos (SGR) asistido por inteligencia artificial que integre transcripción automatizada de audio mediante Whisper, generación de requisitos estructurados mediante modelos de lenguaje locales, y validación gramatical formal basada en la sintaxis EARS, produciendo documentos SRS conformes con IEEE 830-1998.",
    "objetivos_especificos": [
        "Registro y gestión de proyectos con validación formal Pydantic y persistencia JSON.",
        "Transcripción automatizada de entrevistas mediante Whisper con preprocesamiento de audio.",
        "Generación estructurada de requisitos mediante LLM con prompt engineering basado en IEEE 830.",
        "Validación gramatical EARS con clasificación en 5 categorías y sugerencias de corrección.",
        "Orquestación del pipeline IA con visibilidad de progreso y manejo de errores.",
        "Interfaz de usuario Streamlit con fichas técnicas, tabla NFR y lista de reglas de negocio.",
    ],
}


st.set_page_config(
    page_title="SGR - Sistema de Generación de Requisitos basado en IEEE 830 y EARS",
    layout="centered",
)

st.title("SGR - Sistema de Generación de Requisitos")
st.markdown("Basado en **IEEE 830** y **EARS**")

st.text_input("Nombre del Proyecto", key="input_nombre")
st.text_area("Objetivo General", key="input_objetivo")
st.text_area("Descripción del Dominio", key="input_dominio")

if st.button("Registrar Proyecto"):
    try:
        proyecto = Proyecto(
            nombre_proyecto=st.session_state["input_nombre"],
            objetivo_general=st.session_state["input_objetivo"],
            descripcion_dominio=st.session_state["input_dominio"],
        )
        guardar_proyecto(proyecto)
        st.success("Proyecto registrado exitosamente.")
        st.session_state["proyecto_guardado"] = True
        st.rerun()
    except ValidationError as e:
        for error in e.errors():
            campo = error["loc"][0]
            st.error(f"El campo '{campo}' no puede estar vacío.")

proyectos = cargar_proyectos()
if proyectos:
    st.subheader("Proyectos Registrados")
    st.dataframe(proyectos, use_container_width=True)

if st.session_state.get("proyecto_guardado"):
    if st.button("Generar Requisitos con IA"):
        st.session_state["mostrar_requisitos"] = True

if st.session_state.get("mostrar_requisitos"):
    st.markdown("# ESPECIFICACIÓN DE REQUISITOS SGR (IEEE 830)")

    st.markdown("## 1. Introducción Científica")

    st.markdown("### 1.1 Problemática")
    st.markdown(introduccion["problematica"])

    st.markdown("### 1.2 Justificación")
    st.markdown(introduccion["justificacion"])

    st.markdown("### 1.3 Objetivos Generales y Específicos")
    st.markdown(f"**Objetivo General:** {introduccion['objetivo_general']}")
    st.markdown("**Objetivos Específicos:**")
    for i, obj in enumerate(introduccion["objetivos_especificos"], start=1):
        st.markdown(f"{i}. {obj}")

    st.markdown("---")
    st.markdown("## 2. Resultados de Ingeniería de Software (Rúbrica APE)")

    st.markdown("### 2.1 Especificaciones Formales")

    st.markdown("#### Historias de Usuario (User Stories)")
    for us in example_user_stories:
        st.markdown(f"**Como** {us['rol']}, **quiero** {us['accion']}, **para** {us['beneficio']}.")
        st.markdown("**Criterios de Aceptación:**")
        for linea in us["aceptacion"].split("\n"):
            st.markdown(f"- {linea}")
        st.markdown("---")

    st.markdown("#### Diagrama de Casos de Uso (UML)")
    st.markdown(sanitize_output(example_diagrama_casos_uso))

    st.markdown("#### Diagrama de Secuencia (UML)")
    st.markdown(sanitize_output(example_diagrama_secuencia))

    st.markdown("### 2.2 Código Generado e Implementado")

    st.markdown("#### Diagrama de Clases UML")
    st.markdown(sanitize_output(example_diagrama_clases))

    st.markdown("#### Diagrama de Despliegue UML")
    st.markdown(sanitize_output(example_diagrama_despliegue))

    st.markdown("### 2.3 Validación, Coherencia y Análisis de Sincronización")
    st.markdown("**Matriz de Trazabilidad:**")
    df_matriz = pd.DataFrame(matriz_trazabilidad).rename(
        columns={"requerimiento": "Requerimiento", "componente": "Componente", "estado": "Estado"}
    )
    st.dataframe(df_matriz, use_container_width=True)

    st.markdown("---")
    st.markdown("## 3. Arquitectura y Requisitos Base")

    st.markdown("### 3.1 Requerimientos Funcionales (Sintaxis EARS)")
    st.markdown("Clasificados según **EARS** (Easy Approach to Requirements Syntax)")

    for req in lista_requisitos_funcionales:
        categoria, sintaxis = parse_descripcion_ears(req["descripcion_ears"])
        table = f"""| Campo | Detalle |
|---|---|
| **Identificación** | {req['id']} |
| **Nombre** | {req['nombre']} |
| **Características** | {req['caracteristicas']} |
| **Descripción EARS** | {sintaxis} |
| **Categoría EARS** | {categoria} |
| **Prioridad** | {req['prioridad']} |"""
        with st.container():
            st.markdown(table)
            st.markdown("---")

    st.markdown("### 3.2 Requerimientos No Funcionales")
    df_nfr = pd.DataFrame(tabla_no_funcionales).rename(
        columns={"id": "ID", "requisito": "Requisito", "categoria": "Categoría"}
    )
    st.dataframe(df_nfr, use_container_width=True)

    st.markdown("### 3.3 Reglas de Negocio")
    for i, regla in enumerate(reglas_negocio, start=1):
        st.markdown(f"{i}. **{regla['nombre']}:** {regla['descripcion']}")
