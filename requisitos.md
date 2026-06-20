---
status: proposed
version: 1.0
authors: Marylin Alvarado
date: 2026-06-19
---

# HISTORIAL DE REVISIONES
| Versión | Fecha | Autor | Descripción del Cambio |
| :--- | :--- | :--- | :--- |
| 1.0 | 19/06/2026 | Marylin Alvarado | Inicialización del SGR, Problemática, Justificación y validación de Sintaxis EARS |

# SGR - Sistema de Generación de Requisitos
## Especificación de Requisitos de Software según IEEE 830-1998

---

# 1. Introducción

## 1.1 Problemática

La ingeniería de requisitos constituye una de las fases más críticas y propensas a errores en el ciclo de vida del desarrollo de software. Estudios ampliamente reconocidos en la literatura (Standish Group, 1994-2020; CHAOS Report) indican que los requisitos incorrectos, incompletos o ambiguos son la causa principal del fracaso de proyectos de software, representando entre el 40% y el 60% de los defectos descubiertos en etapas tardías del desarrollo. El costo de corregir un error de requisitos aumenta de forma exponencial a medida que el proyecto avanza: un defecto detectado en la fase de operación puede llegar a ser hasta 100 veces más costoso de corregir que si se hubiera identificado durante la elicitación.

El levantamiento tradicional de requisitos enfrenta tres problemáticas fundamentales que impactan directamente la calidad de las especificaciones:

**Ambigüedad en la comunicación oral.** Las entrevistas con partes interesadas, si bien constituyen el método de elicitación más utilizado, adolecen de ambigüedad inherente al lenguaje natural. Las expresiones imprecisas, los supuestos no declarados y las interpretaciones divergentes entre elicitador y stakeholder generan requisitos que pueden ser entendidos de múltiples formas por diferentes actores del proyecto. Sin un mecanismo formal de estructuración y validación, esta ambigüedad se propaga a través de todo el ciclo de desarrollo.

**Pérdida de información en reuniones.** La dependencia de la memoria humana y de notas manuales durante las sesiones de elicitación introduce un sesgo de selección significativo. Los elicitadores tienden a registrar únicamente la información que consideran relevante en el momento, omitiendo detalles contextuales, matices en la comunicación y requisitos implícitos que emergen durante la conversación. Las grabaciones de audio completas rara vez se transcriben y analizan sistemáticamente debido al costo temporal que implica.

**Falta de estructura formal en la documentación.** Aun cuando los requisitos se documentan exitosamente, con frecuencia carecen de una estructura sintáctica estandarizada que facilite su verificación, validación y trazabilidad. La redacción en lenguaje natural sin restricciones formales produce especificaciones inconsistentes donde conviven distintos niveles de abstracción, prioridades no declaradas y relaciones no explicitadas entre requisitos.

El SGR aborda estas tres problemáticas mediante un pipeline integrado que combina transcripción automatizada (Whisper), generación estructurada de requisitos (LLM), y validación gramatical formal (EARS), estableciendo un flujo de trabajo que reduce la ambigüedad, elimina la pérdida de información y garantiza la consistencia estructural de la especificación.

## 1.2 Justificación

La selección de Modelos de Lenguaje de Gran Escala (LLM) y el sistema de reconocimiento automático del habla Whisper como base tecnológica del SGR se fundamenta en los siguientes ejes científicos y técnicos:

**Transcripción automatizada con Whisper.** Whisper (Radford et al., 2023) es un modelo de reconocimiento automático del habla (ASR) desarrollado por OpenAI, entrenado con 680.000 horas de datos multilingües supervisados. Su arquitectura encoder-decoder basada en transformers le confiere una precisión superior en la transcripción de audio en español, con una tasa de error de palabras (WER) inferior al 10% en condiciones acústicas favorables utilizando el modelo de tamaño small o superior. A diferencia de soluciones comerciales basadas en la nube, Whisper puede ejecutarse localmente, eliminando dependencias de conectividad y garantizando la privacidad de los datos de las entrevistas — un requisito fundamental en contextos académicos y de investigación donde la confidencialidad de la información es crítica.

**Generación de requisitos mediante LLM.** Los modelos de lenguaje de gran escala han demostrado capacidad para comprender y generar texto estructurado siguiendo patrones formales complejos (Brown et al., 2020; Wei et al., 2022). Investigaciones recientes en ingeniería de requisitos asistida por IA (Fischbach et al., 2023; Frattini et al., 2023) evidencian que los LLM pueden generar requisitos funcionales y no funcionales con una estructura cercana a la producida por ingenieros de requisitos humanos, especialmente cuando se emplean técnicas de prompt engineering que incorporan restricciones sintácticas y semánticas en la instrucción. El SGR explota esta capacidad mediante un prompt de sistema que integra la plantilla de secciones IEEE 830-1998 y las reglas de sintaxis EARS, guiando al modelo hacia una salida consistente con el estándar.

**Validación gramatical EARS.** La sintaxis EARS (Easy Approach to Requirements Syntax), propuesta por Mavin et al. (2009), define cinco categorías sintácticas para la redacción de requisitos: Ubiquitous, Event-Driven, State-Driven, Optional y Desired. Cada categoría impone una estructura gramatical estricta que elimina la ambigüedad y fuerza la precisión en la especificación. La adopción de EARS en la industria ha demostrado reducir significativamente los errores de interpretación y mejorar la trazabilidad entre requisitos y casos de prueba. El SGR implementa un motor de validación formal que clasifica automáticamente cada requisito en su categoría EARS correspondiente y verifica el cumplimiento de las reglas sintácticas, proporcionando retroalimentación correctiva cuando se detectan desviaciones.

**Ejecución local y soberanía de datos.** Todos los componentes del pipeline — Whisper para transcripción y el LLM para generación de requisitos — se ejecutan exclusivamente en la máquina del usuario mediante Ollama o LlamaCpp como backends de inferencia. Esta decisión arquitectónica elimina los costos recurrentes de API, garantiza la privacidad de los datos de las entrevistas, y permite la operación desconectada, factores esenciales para un entorno académico y de investigación.

**Contribución al estado del arte.** La integración sinérgica de estas tres tecnologías (Whisper, LLM, EARS) en un flujo de trabajo unificado y ejecutable localmente constituye la principal contribución científica de esta tesis. Mientras que existen trabajos que abordan cada tecnología de forma aislada, no se ha identificado en la literatura un sistema que las integre en un pipeline completo de elicitación, generación y validación de requisitos conforme a IEEE 830 y EARS, con ejecución local y código abierto.

## 1.3 Objetivos

### Objetivo General

Desarrollar e implementar un Sistema de Generación de Requisitos (SGR) asistido por inteligencia artificial que integre transcripción automatizada de audio mediante Whisper, generación de requisitos estructurados mediante modelos de lenguaje locales, y validación gramatical formal basada en la sintaxis EARS, produciendo documentos de especificación de requisitos de software conformes con el estándar IEEE 830-1998.

### Objetivos Específicos

1. **Registro y gestión de proyectos.** Implementar un módulo base de registro de proyectos de software con validación formal de datos mediante Pydantic, persistencia local en JSON, y visualización interactiva, que sirva como punto de entrada para la captura del contexto del proyecto.

2. **Transcripción automatizada de entrevistas.** Integrar el modelo Whisper de OpenAI para la transcripción local de grabaciones de audio de entrevistas con partes interesadas, incluyendo preprocesamiento automático (remuestreo a 16kHz, conversión a mono, normalización de volumen) y generación de transcripciones con marcas temporales por segmento para trazabilidad.

3. **Generación estructurada de requisitos mediante LLM.** Diseñar e implementar un sistema de prompt engineering que, a partir de la transcripción de la entrevista y el contexto del proyecto, genere requisitos funcionales y no funcionales organizados según la estructura IEEE 830, utilizando modelos de lenguaje locales ejecutados a través de Ollama o LlamaCpp.

4. **Validación gramatical EARS.** Implementar un motor de validación formal que clasifique cada requisito generado en una de las cinco categorías EARS (Ubiquitous, Event-Driven, State-Driven, Optional, Desired) y verifique el cumplimiento estricto de las reglas sintácticas de cada categoría, proporcionando mensajes de error detallados con sugerencias de corrección.

5. **Orquestación del pipeline de IA.** Desarrollar un orquestador que coordine la ejecución secuencial de las etapas del pipeline (audio → transcripción → generación LLM → validación EARS → ensamblado SRS), con visibilidad del progreso por etapa, manejo de errores con retroalimentación específica, y capacidades de configuración de parámetros (modelo LLM, tamaño de Whisper, idioma, tiempos de espera).

6. **Interfaz de usuario para visualización de requisitos.** Implementar una interfaz gráfica basada en Streamlit que presente los requisitos funcionales en fichas técnicas verticales con los campos estandarizados (Identificación, Nombre, Características, Descripción EARS, Prioridad), los requisitos no funcionales en tabla matricial interactiva, y las reglas de negocio en lista indexada formal, facilitando la revisión y validación por parte del usuario.

## 1.4 Propósito

El presente documento constituye la Especificación de Requisitos de Software (ERS) para el **SGR - Sistema de Generación de Requisitos**, un sistema asistido por Inteligencia Artificial que integra modelos de lenguaje de gran escala (LLM) locales, transcripción de audio mediante Whisper, y un motor de validación gramatical EARS para la elicitación, generación y validación formal de requisitos de software conforme a los estándares IEEE 830-1998 y EARS (Easy Approach to Requirements Syntax).

El SGR opera en dos modalidades complementarias: (1) un módulo base de registro y gestión de proyectos de software con validación Pydantic y persistencia JSON local, y (2) un pipeline de inteligencia artificial que transcribe entrevistas con partes interesadas mediante Whisper, genera requisitos estructurados mediante LLMs locales (Ollama/LlamaCpp), y valida la conformidad gramatical de cada requisito contra las cinco categorías de la sintaxis EARS. El objetivo de la tesis es demostrar que la integración de estas tecnologías en un flujo de trabajo unificado produce especificaciones de requisitos más completas, trazables y formalmente correctas.

Este documento está dirigido a los desarrolladores del sistema, evaluadores de tesis, investigadores en ingeniería de requisitos asistida por IA, y usuarios finales que participan en el proceso de elicitación. Constituye el artefacto central de especificación para el trabajo de tesis y establece la línea base contra la cual se verificará la implementación.

## 1.5 Ámbito del producto

El SGR es una herramienta independiente, de escritorio web, construida sobre Streamlit, que integra capacidades de inteligencia artificial para la ingeniería de requisitos. El sistema abarca los siguientes dominios funcionales:

**Módulo base (SGR v1):**
- Registro de proyectos de software mediante formularios con validación Pydantic (nombre, objetivo general, descripción del dominio).
- Persistencia local en archivo JSON (`proyectos_sgr.json`) con carga automática al inicio.
- Visualización de proyectos registrados en tabla interactiva con actualización en tiempo real.
- Retroalimentación al usuario mediante mensajes de confirmación y manejo de errores de validación.

**Pipeline de inteligencia artificial (SGR v2):**
- **Transcripción de audio**: Captura de entrevistas con partes interesadas mediante el modelo Whisper de OpenAI (ejecución local), con soporte para formatos WAV, MP3, M4A y FLAC, preprocesamiento automático (remuestreo a 16kHz, conversión a mono, normalización de volumen), y generación de transcripciones con marcas temporales por segmento.
- **Generación de requisitos**: Construcción de prompts estructurados que incorporan la descripción del proyecto y el contexto de dominio, envío a modelos LLM locales mediante Ollama REST API o servidor LlamaCpp, y parseo de la respuesta estructurada en secciones IEEE 830 (requisitos funcionales, no funcionales, interfaces).
- **Validación gramatical EARS**: Motor de validación formal que clasifica cada requisito en una de las cinco categorías EARS (Ubiquo, Disparado por Eventos, Estado, Opcional, Deseado), verifica la sintaxis estricta de cada categoría mediante analizadores gramaticales especializados, y produce mensajes de error detallados con sugerencias de corrección cuando un requisito no cumple la gramática.
- **Orquestación del pipeline**: Coordinador de flujo de trabajo que ejecuta las etapas en secuencia (audio → transcripción → generación LLM → validación EARS → ensamblado SRS), proporciona visibilidad del progreso por etapa, maneja errores con retroalimentación específica, y ensambla el documento SRS final en formato IEEE 830.

El sistema **no** incluye: edición o eliminación de proyectos registrados, autenticación de usuarios, soporte multiusuario, servicios LLM en la nube (operación exclusivamente local), entrenamiento o ajuste de modelos, ni generación de documentación en formatos adicionales (PDF, DOCX).

## 1.6 Definiciones y siglas

| Término | Definición |
|---------|------------|
| **ERS / SRS** | Especificación de Requisitos de Software / Software Requirements Specification |
| **IEEE 830** | Estándar del IEEE para la práctica de especificaciones de requisitos de software (IEEE 830-1998) |
| **EARS** | Easy Approach to Requirements Syntax — taxonomía para redacción de requisitos con cinco categorías sintácticas (Mavin et al., 2009) |
| **SGR** | Sistema de Generación de Requisitos |
| **LLM** | Large Language Model — modelo de lenguaje de gran escala ejecutado localmente para generación de texto estructurado |
| **Whisper** | Modelo de reconocimiento automático del habla (ASR) de OpenAI, ejecutable localmente, que transcribe audio a texto con marcas temporales |
| **Ollama** | Ejecutor de modelos LLM local que expone una API REST para inferencia |
| **LlamaCpp** | Implementación en C/C++ de inferencia de modelos LLM con servidor API integrado |
| **Prompt engineering** | Ingeniería de instrucciones — diseño sistemático de prompts para guiar la salida de modelos LLM hacia formatos estructurados |
| **Pipeline** | Tubería de procesamiento — secuencia orquestada de etapas de transformación de datos |
| **ASR** | Automatic Speech Recognition — reconocimiento automático del habla |
| **WER** | Word Error Rate — tasa de error de palabras, métrica de precisión de transcripción |
| **Inference endpoint** | Punto de conexión API para realizar inferencia sobre un modelo LLM |
| **Streamlit** | Framework de Python para construir aplicaciones web interactivas de datos |
| **Pydantic** | Biblioteca de Python para validación de datos mediante modelos tipados |
| **StrictStr** | Tipo de Pydantic que rechaza cadenas vacías y no fuerza coerción de tipos |
| **Prompt template** | Plantilla de instrucción que combina contexto fijo (reglas IEEE 830, sintaxis EARS) con contexto variable (descripción del proyecto) |
| **Grammar validator** | Componente que analiza sintácticamente un requisito y determina su conformidad con una categoría EARS específica |
| **Pipeline orchestrator** | Componente que gestiona la ejecución secuencial de las etapas del pipeline, incluyendo manejo de errores, reintentos y notificación de progreso |
| **VRAM** | Video Random Access Memory — memoria de video utilizada por GPUs para inferencia de modelos |
| **Context window** | Ventana de contexto — número máximo de tokens que un modelo LLM puede procesar en una sola inferencia |

## 1.7 Referencias

- IEEE Std 830-1998, *IEEE Recommended Practice for Software Requirements Specifications*
- EARS (Easy Approach to Requirements Syntax), Mavin, A., Wilkinson, P., Harwood, A., & Novak, M. (2009). *Easy Approach to Requirements Syntax (EARS)*. 17th IEEE International Requirements Engineering Conference
- Radford, A., Kim, J. W., Xu, T., Brockman, G., McLeavey, C., & Sutskever, I. (2023). *Robust Speech Recognition via Large-Scale Weak Supervision*. OpenAI. https://cdn.openai.com/papers/whisper.pdf
- Brown, T. B., Mann, B., Ryder, N., et al. (2020). *Language Models are Few-Shot Learners*. Advances in Neural Information Processing Systems, 33, 1877-1901.
- Wei, J., Wang, X., Schuurmans, D., et al. (2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. Advances in Neural Information Processing Systems, 35.
- Fischbach, J., Frattini, J., Vogelsang, A., et al. (2023). *Automatic Requirement Generation from Natural Language: A Systematic Literature Review*. Requirements Engineering Journal.
- Frattini, J., Montgomery, L., Fischbach, J., & Mendez, D. (2023). *A Live Extractive Summarization of User Requirements: A Controlled Experiment*. Proceedings of the 31st IEEE International Requirements Engineering Conference.
- Standish Group (1994-2020). *CHAOS Report Series*. The Standish Group International.
- Ollama Documentation: https://github.com/ollama/ollama
- LlamaCpp Documentation: https://github.com/ggerganov/llama.cpp
- Streamlit Documentation: https://docs.streamlit.io
- Pydantic Documentation: https://docs.pydantic.dev
- Código fuente del sistema: `app.py`
- Artefactos de especificación: `openspec/specs/ieee830-srs/spec.md`
- Especificaciones del pipeline IA: `openspec/changes/expansion-srs-ia-pipeline/specs/`

## 1.8 Visión general del documento

La **Sección 1** (presente) establece el marco académico y técnico del SGR: la Problemática (1.1) que motiva la investigación, la Justificación (1.2) que fundamenta las decisiones tecnológicas, los Objetivos (1.3) que guían el desarrollo, el Propósito (1.4) y el Ámbito del producto (1.5) que delimitan el sistema, las Definiciones y siglas (1.6) que estandarizan la terminología, las Referencias (1.7) que respaldan el marco teórico, y esta Visión general (1.8) que orienta la lectura del documento.

La **Sección 2** describe el sistema en su contexto general, incluyendo la arquitectura de capas del módulo base y la arquitectura del pipeline de IA con sus cuatro etapas fundamentales: transcripción Whisper, generación LLM, validación EARS y orquestación. Se detallan las funciones del producto, los perfiles de usuario, las restricciones tecnológicas y las suposiciones operativas tanto para el módulo base como para el pipeline de IA.

La **Sección 3** constituye el cuerpo técnico del documento. En 3.1 se especifican los requisitos funcionales organizados por subsistemas: registro de proyectos (base), persistencia, visualización, retroalimentación, y las cinco categorías de la sintaxis EARS con reglas formales detalladas, la transcripción de audio, la generación mediante LLM, la validación gramatical y la orquestación del pipeline. La sección 3.2 cubre los requisitos no funcionales con métricas de rendimiento, precisión y hardware. La sección 3.3 documenta las interfaces externas para los componentes de IA (Ollama, LlamaCpp, Whisper) y los formatos de datos del pipeline. La sección 3.4 presenta el mapeo completo de requisitos a código y artefactos de especificación.

---

# 2. Descripción General

## 2.1 Perspectiva del producto

El SGR es un sistema independiente (no es un componente de un sistema mayor) que integra dos subsistemas arquitectónicos: un módulo base de registro de proyectos y un pipeline de inteligencia artificial para la generación y validación de requisitos.

### 2.1.1 Arquitectura del módulo base (SGR v1)

El módulo base sigue un modelo de tres capas lógicas que operan dentro de una sola aplicación Streamlit:

```
┌──────────────────────────────────┐
│   Capa de Presentación           │
│   (Streamlit UI - app.py)        │
│   st.form, st.dataframe,         │
│   st.text_input, st.text_area    │
├──────────────────────────────────┤
│   Capa de Validación             │
│   (Pydantic Proyecto)            │
│   StrictStr, min_length=1,       │
│   ValidationError handling       │
├──────────────────────────────────┤
│   Capa de Persistencia           │
│   (JSON - proyectos_sgr.json)    │
│   json.dump, json.load,          │
│   os.path.exists                 │
└──────────────────────────────────┘
```

- **Capa de Presentación**: Formularios y tabla de datos usando componentes nativos de Streamlit (`st.form`, `st.dataframe`, `st.text_input`, `st.text_area`). Incluye manejo de estado de sesión para retroalimentación visual.
- **Capa de Validación**: Modelo `Proyecto` de Pydantic con campos `StrictStr` y `min_length=1`. Captura y reporta errores de validación con mensajes descriptivos en español.
- **Capa de Persistencia**: Funciones `cargar_proyectos()` y `guardar_proyecto()` que operan sobre `proyectos_sgr.json` con codificación UTF-8 y manejo de archivo ausente.

### 2.1.2 Arquitectura del pipeline de IA (SGR v2)

El pipeline de inteligencia artificial extiende la arquitectura base con cuatro etapas de procesamiento secuencial:

```
┌──────────┐    ┌────────────┐    ┌──────────────┐    ┌──────────────┐    ┌─────────────┐
│  Audio   │───▶│  Whisper   │───▶│     LLM      │───▶│    EARS      │───▶│    SRS      │
│  Input   │    │    ASR     │    │  Generation  │    │  Validator   │    │   Output    │
│(WAV/MP3/ │    │Transcripción│   │   Prompts    │    │Clasificación │    │  Ensamblado │
│ M4A/FLAC)│    │+ timestamps│   │  + parseo    │    │  + sintaxis  │    │  IEEE 830   │
└──────────┘    └────────────┘    └──────────────┘    └──────────────┘    └─────────────┘
       │               │                  │                    │                 │
       ▼               ▼                  ▼                    ▼                 ▼
  Preprocesamiento  Texto con        Requisitos           Requisitos         Documento
  16kHz/mono/      segmentos y      estructurados        validados          SRS final
  normalización    timestamps       IEEE 830             EARS
```

**Etapa 1 — Transcripción de audio (Whisper ASR):**
- **Entrada**: Archivo de audio en formato WAV, MP3, M4A o FLAC.
- **Preprocesamiento**: Remuestreo a 16kHz, conversión de canales a mono, normalización de amplitud.
- **Procesamiento**: Inferencia local del modelo Whisper (variante configurable: tiny, base, small, medium, large).
- **Salida**: Texto transcrito con segmentos y marcas temporales (inicio, fin por segmento).
- **Interfaz**: API de Whisper Python (`whisper.load_model()`, `model.transcribe()`).

**Etapa 2 — Generación de requisitos mediante LLM:**
- **Entrada**: Texto transcrito de la entrevista + descripción del proyecto registrado (nombre, objetivo, dominio).
- **Construcción de prompt**: Plantilla de sistema que incluye instrucciones IEEE 830, reglas de sintaxis EARS, y el contexto del proyecto.
- **Procesamiento**: Solicitud de inferencia al LLM local mediante Ollama REST API o servidor LlamaCpp.
- **Salida**: Respuesta estructurada parseada en secciones IEEE 830 (RF, RNF, interfaces).
- **Interfaz**: Ollama: `POST /api/generate` con `model`, `prompt`, `stream: false`. LlamaCpp: `POST /completion` con `prompt`, `n_predict`, `temperature`.

**Etapa 3 — Validación gramatical EARS:**
- **Entrada**: Requisitos generados por el LLM en formato estructurado.
- **Procesamiento**: Clasificación de cada requisito en una categoría EARS, validación de sintaxis estricta contra las reglas de la categoría, generación de errores con sugerencias.
- **Salida**: Requisitos validados con clasificación EARS y estado de validación (aprobado/rechazado + mensaje de error).
- **Interfaz**: API interna del motor de validación con funciones por categoría.

**Etapa 4 — Orquestación y ensamblado SRS:**
- **Entrada**: Resultados de las etapas anteriores (transcripción, requisitos generados, validaciones).
- **Procesamiento**: Coordinación del flujo secuencial, visibilidad de progreso, manejo de errores por etapa.
- **Salida**: Documento SRS completo en formato IEEE 830 con todos los requisitos validados y clasificados.
- **Interfaz**: Orquestador central con callbacks de progreso y manejo de estado.

### 2.1.3 Flujo de datos del pipeline

Los datos fluyen a través del pipeline en formatos específicos que garantizan la trazabilidad entre etapas:

```
Audio Input (binario, formato orig)
    │
    ▼
PreprocessedAudio {
  waveform: float32[channels][samples],
  sample_rate: 16000,
  original_format: str
}
    │
    ▼
TranscriptionResult {
  text: str,
  segments: [{start: float, end: float, text: str}],
  language: str,
  duration_seconds: float
}
    │
    ▼
LLMInput {
  transcription_text: str,
  project_context: {nombre, objetivo, dominio},
  system_prompt: str,
  model_params: {model, temperature, max_tokens}
}
    │
    ▼
LLMOutput {
  raw_response: str,
  parsed_requirements: [
    {id, category, text, classification}
  ],
  sections: {funcionales, no_funcionales, interfaces}
}
    │
    ▼
ValidationResult {
  requirement_id: str,
  ears_category: str,
  syntax_valid: bool,
  errors: [{rule, message, suggestion}],
  corrected_example: str
}
    │
    ▼
SRSDocument {
  metadata: {project, date, version},
  sections: {
    introduccion: {...},
    descripcion_general: {...},
    requisitos_especificos: {
      funcionales: [ValidatedRequirement],
      no_funcionales: [ValidatedRequirement],
      interfaces: [ValidatedRequirement]
    }
  }
}
```

## 2.2 Funciones del producto

### Funciones del módulo base:

1. **Registro de proyectos**: El usuario completa un formulario con Nombre del Proyecto, Objetivo General y Descripción del Dominio, y lo envía para su registro.
2. **Validación de datos**: El sistema valida que ningún campo esté vacío usando Pydantic, mostrando mensajes de error específicos en español.
3. **Persistencia local**: Los proyectos registrados se guardan en `proyectos_sgr.json` y se cargan automáticamente al iniciar la aplicación.
4. **Visualización de proyectos**: Todos los proyectos registrados se muestran en una tabla interactiva que se actualiza tras cada registro exitoso.
5. **Retroalimentación al usuario**: Mensajes de confirmación visual y manejo de estado de sesión para mantener la retroalimentación entre recargas de la interfaz.

### Funciones del pipeline de IA:

6. **Transcripción de audio**: El sistema procesa archivos de audio de entrevistas mediante Whisper, generando texto transcrito con marcas temporales por segmento y soporte multilingüe (español como idioma principal).
7. **Generación de requisitos mediante LLM**: El sistema construye prompts estructurados con contexto del proyecto y reglas IEEE 830/EARS, envía solicitudes a modelos LLM locales, y parsea las respuestas en requisitos organizados por secciones.
8. **Validación gramatical EARS**: El sistema clasifica cada requisito generado en una de las cinco categorías EARS y valida su sintaxis contra reglas formales estrictas, proporcionando correcciones sugeridas cuando la validación falla.
9. **Orquestación del pipeline**: El sistema coordina la ejecución secuencial de todas las etapas del pipeline, muestra el progreso en tiempo real, maneja errores con retroalimentación específica por etapa, y permite la configuración de parámetros del pipeline (modelo LLM, tamaño de Whisper, idioma, tiempos de espera).
10. **Ensamblado de documento SRS**: El sistema combina los requisitos validados en un documento estructurado conforme al formato IEEE 830, listo para su revisión y exportación.

## 2.3 Características de los usuarios

| Tipo de usuario | Características |
|-----------------|-----------------|
| **Usuario final (elicitor)** | Estudiante o investigador que utiliza el SGR para registrar proyectos y gestionar requisitos. Participa en entrevistas de elicitación cuyas grabaciones son insumos del pipeline. No requiere conocimientos técnicos avanzados de IA ni de sintaxis EARS. |
| **Ingeniero de requisitos** | Usuario avanzado que configura los parámetros del pipeline de IA (selección de modelos, ajuste de prompts, umbrales de validación) y revisa los resultados de la validación gramatical para refinar los requisitos generados. |
| **Evaluador de tesis** | Revisor que examina la correspondencia entre los requisitos documentados y la implementación, así como la correctitud de la integración del pipeline de IA con el estándar IEEE 830. |
| **Desarrollador del sistema** | Programador que implementa y mantiene los componentes del pipeline (integración Whisper, cliente LLM, motor de validación EARS, orquestador). Requiere comprensión detallada de las APIs y formatos de datos. |

## 2.4 Restricciones

### Restricciones del módulo base:

- **Lenguaje de implementación**: Python 3.11+
- **Framework UI**: Streamlit (no se permite HTML/JS/CSS personalizado)
- **Validación**: Pydantic v2 con `StrictStr`
- **Persistencia**: Archivo JSON local (sin base de datos)
- **Idioma de la interfaz**: Español

### Restricciones del pipeline de IA:

- **Ejecución de modelos**: Todos los modelos (LLM y Whisper) se ejecutan localmente en la máquina del usuario. No se permiten servicios en la nube.
- **Memoria RAM mínima**: 8 GB para operación básica (Whisper small + LLM 3B); 16 GB recomendados para Whisper large + LLM 7B.
- **Memoria VRAM**: Se recomienda GPU con al menos 4 GB VRAM para Whisper medium/large y LLM 7B. Sin GPU, los modelos pequeños (Whisper tiny/base, LLM 3B) pueden ejecutarse en CPU con latencia incrementada.
- **Tamaños de modelo Whisper**: Variantes disponibles: tiny (39M params), base (74M), small (244M), medium (769M), large (1550M). La selección impacta directamente la precisión de transcripción y el tiempo de procesamiento.
- **Modelos LLM compatibles**: Cualquier modelo compatible con Ollama o LlamaCpp (formato GGUF). Se recomiendan modelos de 3B a 7B parámetros para balance entre calidad y rendimiento en hardware local.
- **Latencia de inferencia LLM**: Se espera que la generación de requisitos complete en menos de 30 segundos para modelos de hasta 7B en GPU, y menos de 120 segundos en CPU.
- **Formato de audio**: Los archivos de audio deben estar en formatos WAV, MP3, M4A o FLAC. El sistema preprocesa automáticamente a 16kHz mono.
- **Ventana de contexto LLM**: El prompt del sistema más la transcripción no deben exceder la ventana de contexto del modelo seleccionado (típicamente 2048-8192 tokens dependiendo del modelo).

## 2.5 Suposiciones y dependencias

### Suposiciones operativas:

- El sistema funciona en un entorno monousuario.
- Python 3.11 o superior está instalado con las bibliotecas `streamlit`, `pydantic`, `openai-whisper`, y `requests`.
- Ollama o LlamaCpp están instalados y configurados con al menos un modelo LLM descargado.
- El archivo `proyectos_sgr.json` se encuentra en el mismo directorio que `app.py`.
- No se requiere conexión a internet para la operación del sistema (todos los modelos son locales).
- Los archivos de audio de entrada son proporcionados por el usuario y cumplen con los formatos soportados.
- La GPU es opcional; sin ella, el sistema opera con modelos reducidos y latencia mayor.
- El usuario tiene espacio en disco suficiente para los modelos (Whisper large: ~3GB, LLM 7B: ~4-8GB dependiendo de la cuantización).

### Dependencias de software:

- **Módulo base**: `streamlit`, `pydantic`, `json` (stdlib), `os` (stdlib), `datetime` (stdlib).
- **Pipeline de IA**: `openai-whisper` (transcripción), `requests` (API LLM), `numpy` (procesamiento de audio).
- **Opcional**: `torch` (aceleración GPU para Whisper), `ffmpeg` (procesamiento de formatos de audio).

---

# 3. Requisitos Específicos

## 3.1 Requisitos Funcionales

### 3.1.1 Registro de Proyectos

**Clasificación EARS**: Ubiquitous

| ID | Requisito | Implementación |
|----|-----------|----------------|
| RF-01 | El sistema SHALL proporcionar un formulario con tres campos de texto: *Nombre del Proyecto*, *Objetivo General* y *Descripción del Dominio* | `app.py:40-44` — `st.form` con `st.text_input` y `st.text_area` |
| RF-02 | El sistema SHALL incluir un botón *Registrar Proyecto* para enviar el formulario | `app.py:44` — `st.form_submit_button("Registrar Proyecto")` |
| RF-03 | El sistema SHALL validar mediante Pydantic que ningún campo esté vacío antes de guardar | `app.py:11-15` — Modelo `Proyecto` con `Field(..., min_length=1, strict=True)` |

**Escenarios**:

#### Escenario: Registro exitoso
- **CUANDO** el usuario completa los tres campos con texto válido y presiona *Registrar Proyecto*
- **ENTONCES** el sistema valida los datos, guarda el proyecto y muestra el mensaje *"Proyecto registrado exitosamente."*

#### Escenario: Campo vacío
- **CUANDO** el usuario presiona *Registrar Proyecto* con uno o más campos vacíos
- **ENTONCES** el sistema captura `ValidationError` y muestra mensajes de error indicando qué campos están vacíos

#### Escenario: Visualización de errores
- **CUANDO** ocurre un error de validación
- **ENTONCES** el sistema itera sobre `e.errors()` y muestra `st.error(f"El campo '{campo}' no puede estar vacío.")` por cada campo inválido

### Workflow de Validación EARS

| ID | Palabras Clave | Estado |
|----|----------------|--------|
| RF-01 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-02 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-03 | WHEN, THE SYSTEM SHALL | ✅ Cumple |

**Estado general**: `approved`

### 3.1.2 Persistencia de Datos

**Clasificación EARS**: Ubiquitous

| ID | Requisito | Implementación |
|----|-----------|----------------|
| RF-04 | El sistema SHALL guardar los proyectos en un archivo local `proyectos_sgr.json` | `app.py:25-30` — `guardar_proyecto()` escribe JSON con `json.dump` |
| RF-05 | El sistema SHALL cargar los proyectos existentes al iniciar la aplicación | `app.py:18-22` — `cargar_proyectos()` lee `proyectos_sgr.json` |
| RF-06 | El sistema SHALL almacenar cada proyecto con los campos: `nombre_proyecto`, `objetivo_general`, `descripcion_dominio`, `fecha_registro` | `app.py:11-15` — Modelo `Proyecto` incluye `fecha_registro` con timestamp automático |
| RF-07 | El sistema SHALL manejar la ausencia del archivo `proyectos_sgr.json` en el primer uso | `app.py:19` — `if not os.path.exists(DATA_FILE): return []` |

**Escenarios**:

#### Escenario: Guardar proyecto
- **CUANDO** un proyecto supera la validación
- **ENTONCES** el sistema lo agrega a la lista existente y escribe el archivo JSON completo con codificación UTF-8

#### Escenario: Cargar al inicio
- **CUANDO** la aplicación se inicia
- **ENTONCES** el sistema lee `proyectos_sgr.json` y carga todos los proyectos en memoria para mostrarlos

#### Escenario: Primer uso sin datos
- **CUANDO** `proyectos_sgr.json` no existe
- **ENTONCES** el sistema retorna una lista vacía sin generar errores

### Workflow de Validación EARS

| ID | Palabras Clave | Estado |
|----|----------------|--------|
| RF-04 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-05 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-06 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-07 | WHEN, THE SYSTEM SHALL | ✅ Cumple |

**Estado general**: `approved`

### 3.1.3 Visualización de Proyectos

**Clasificación EARS**: Ubiquitous

| ID | Requisito | Implementación |
|----|-----------|----------------|
| RF-08 | El sistema SHALL mostrar todos los proyectos registrados en una tabla interactiva | `app.py:66-67` — `st.dataframe(proyectos, use_container_width=True)` |
| RF-09 | El sistema SHALL actualizar la tabla inmediatamente después de un registro exitoso | `app.py:61-62` — `st.rerun()` tras guardar |

**Escenarios**:

#### Escenario: Visualizar proyectos
- **CUANDO** la aplicación carga o un proyecto es guardado exitosamente
- **ENTONCES** el sistema renderiza un `st.dataframe` con todos los proyectos registrados

#### Escenario: Actualización post-registro
- **CUANDO** un proyecto se guarda exitosamente
- **ENTONCES** el sistema forza un re-ejecución (`st.rerun()`) para actualizar la tabla con el nuevo proyecto

### Workflow de Validación EARS

| ID | Palabras Clave | Estado |
|----|----------------|--------|
| RF-08 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-09 | WHEN, THE SYSTEM SHALL | ✅ Cumple |

**Estado general**: `approved`

### 3.1.4 Retroalimentación al Usuario

**Clasificación EARS**: Event-Driven

| ID | Requisito | Implementación |
|----|-----------|----------------|
| RF-10 | El sistema SHALL mostrar un mensaje de confirmación después de guardar un proyecto | `app.py:54` — `st.success("Proyecto registrado exitosamente.")` |
| RF-11 | El sistema SHALL usar `session_state` para evitar que el mensaje de confirmación desaparezca antes del re-ejecución | `app.py:55` — `st.session_state["proyecto_guardado"] = True` |

**Escenarios**:

#### Escenario: Confirmación visible
- **CUANDO** el registro es exitoso
- **ENTONCES** el sistema muestra `st.success` y establece `session_state["proyecto_guardado"] = True`

### Workflow de Validación EARS

| ID | Palabras Clave | Estado |
|----|----------------|--------|
| RF-10 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-11 | WHEN, THE SYSTEM SHALL | ✅ Cumple |

**Estado general**: `approved`

### 3.1.5 EARS — Requisitos Ubicuos (Ubiquitous)

**Clasificación EARS**: Ubiquitous

Los requisitos Ubicuos expresan comportamientos que el sistema SHALL exhibir siempre, sin condiciones previas ni desencadenantes. Representan funcionalidades permanentes del sistema.

**Sintaxis formal**:
```
<entidad> SHALL <acción>
<entidad> SHALL <acción> <objeto>
<entidad> SHALL <acción> <objeto> <complemento>
```

**Reglas de validación estrictas**:
1. La entidad debe ser un sustantivo o frase nominal que identifique al sistema o un componente.
2. El verbo modal SHALL es obligatorio y debe aparecer exactamente una vez.
3. No se permiten cláusulas condicionales (WHEN, WHILE, WHERE, IF).
4. La acción debe ser un verbo en infinitivo que describa una funcionalidad.
5. El requisito completo debe ser una oración declarativa simple.

**Algoritmo de clasificación**:
1. Verificar presencia del token SHALL.
2. Verificar ausencia de tokens condicionales (WHEN, WHILE, WHERE, IF, SI, CUANDO, MIENTRAS, DONDE).
3. Verificar estructura sintáctica: [sujeto] SHALL [verbo] [complemento].
4. Si todas las verificaciones pasan, clasificar como Ubicuo.

| ID | Requisito | Implementación/Especificación |
|----|-----------|-------------------------------|
| RF-12 | El sistema SHALL clasificar un requisito como Ubicuo cuando contenga SHALL sin cláusulas condicionales | `ears-grammar-validation/spec.md` — Escenario: Ubiquitous requirement detected |
| RF-13 | El sistema SHALL validar que los requisitos Ubicuos sigan el patrón `<entidad> SHALL <acción>` sin cláusulas condicionales | `ears-grammar-validation/spec.md` — Strict syntax validation rules for Ubiquitous |

**Ejemplos**:

```
Válido:   "El sistema SHALL proporcionar un formulario de registro"
Válido:   "El sistema SHALL almacenar los proyectos en un archivo JSON"
Inválido: "El sistema SHALL validar los datos CUANDO el usuario envía el formulario"
          → Error: Presencia de cláusula condicional (CUANDO). Sugerir clasificación Event-Driven.
Inválido: "El sistema SHALL procesar audio SI el archivo es WAV"
           → Error: Presencia de condicional (SI). Sugerir clasificación Optional.
```

### Workflow de Validación EARS

| ID | Palabras Clave | Estado |
|----|----------------|--------|
| RF-12 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-13 | WHEN, THE SYSTEM SHALL | ✅ Cumple |

**Estado general**: `approved`

### 3.1.6 EARS — Requisitos Disparados por Eventos (Event-Driven)

**Clasificación EARS**: Event-Driven

Los requisitos Event-Driven describen comportamientos que se activan en respuesta a un evento específico. Siguen un patrón causa-efecto donde un disparador produce una respuesta del sistema.

**Sintaxis formal**:
```
WHEN <evento> THEN <entidad> SHALL <respuesta>
WHEN <evento> <entidad> SHALL <respuesta>
CUANDO <evento> ENTONCES <entidad> SHALL <respuesta>
CUANDO <evento> <entidad> SHALL <respuesta>
```

**Reglas de validación estrictas**:
1. La cláusula WHEN/CUANDO es obligatoria y debe iniciar el requisito.
2. El evento debe describir una acción o condición que ocurre externamente.
3. Debe existir una cláusula THEN/ENTONCES explícita o implícita (seguida de SHALL).
4. El verbo modal SHALL es obligatorio en la cláusula de respuesta.
5. No se permiten múltiples disparadores en un mismo requisito.

**Algoritmo de clasificación**:
1. Verificar presencia del token WHEN o CUANDO al inicio del requisito.
2. Verificar presencia del token SHALL en la cláusula de respuesta.
3. Verificar presencia de THEN o ENTONCES entre el evento y la respuesta, o que SHALL siga inmediatamente al evento.
4. Verificar que no existan tokens de estado continuo (WHILE).
5. Si todas las verificaciones pasan, clasificar como Event-Driven.

| ID | Requisito | Implementación/Especificación |
|----|-----------|-------------------------------|
| RF-14 | El sistema SHALL clasificar un requisito como Event-Driven cuando contenga WHEN/CUANDO seguido de THEN/SHALL | `ears-grammar-validation/spec.md` — Escenario: Event-Driven requirement detected |
| RF-15 | El sistema SHALL validar que los requisitos Event-Driven sigan el patrón `WHEN <trigger> THEN <entity> SHALL <response>` | `ears-grammar-validation/spec.md` — Strict syntax validation rules for Event-Driven |

**Ejemplos**:

```
Válido:   "WHEN el usuario envía el formulario THEN el sistema SHALL validar los datos"
Válido:   "CUANDO el archivo de audio se carga el sistema SHALL iniciar la transcripción"
Inválido: "WHEN el usuario hace clic"
          → Error: Falta cláusula THEN/SHALL de respuesta. El requisito no especifica qué ocurre.
Inválido: "WHEN el sistema inicia MIENTRAS hay datos pendientes el sistema SHALL procesarlos"
           → Error: Conflicto entre Event-Driven (WHEN) y State-Driven (MIENTRAS). Clasificación ambigua.
```

### Workflow de Validación EARS

| ID | Palabras Clave | Estado |
|----|----------------|--------|
| RF-14 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-15 | WHEN, THE SYSTEM SHALL | ✅ Cumple |

**Estado general**: `approved`

### 3.1.7 EARS — Requisitos de Estado (State-Driven)

**Clasificación EARS**: State-Driven

Los requisitos State-Driven describen comportamientos que el sistema SHALL mantener continuamente mientras el sistema se encuentra en un estado particular. A diferencia de los Event-Driven, la condición es un estado continuo, no un evento puntual.

**Sintaxis formal**:
```
WHILE <estado> <entidad> SHALL <acción>
WHILE <estado> <entidad> SHALL <acción> <objeto>
MIENTRAS <estado> <entidad> SHALL <acción>
```

**Reglas de validación estrictas**:
1. La cláusula WHILE/MIENTRAS es obligatoria y debe iniciar el requisito.
2. El estado debe describir una condición continua o modo operativo.
3. La acción especificada SHALL mantenerse activa mientras el estado persista.
4. El verbo modal SHALL es obligatorio.
5. No se permiten eventos puntuales (WHEN/CUANDO) combinados con estados continuos.

**Algoritmo de clasificación**:
1. Verificar presencia del token WHILE o MIENTRAS al inicio del requisito.
2. Verificar que la condición describa un estado continuo (no un evento puntual).
3. Verificar presencia de SHALL en la cláusula de acción.
4. Verificar que no existan tokens de evento (WHEN/CUANDO).
5. Si todas las verificaciones pasan, clasificar como State-Driven.

| ID | Requisito | Implementación/Especificación |
|----|-----------|-------------------------------|
| RF-16 | El sistema SHALL clasificar un requisito como State-Driven cuando contenga WHILE/MIENTRAS describiendo un estado continuo | `ears-grammar-validation/spec.md` — Escenario: State-Driven requirement detected |
| RF-17 | El sistema SHALL validar que los requisitos State-Driven sigan el patrón `WHILE <state> <entity> SHALL <action>` | `ears-grammar-validation/spec.md` — Strict syntax validation rules for State-Driven |

**Ejemplos**:

```
Válido:   "WHILE el archivo está abierto el sistema SHALL bloquear escrituras concurrentes"
Válido:   "MIENTRAS el pipeline está en ejecución el sistema SHALL mostrar el progreso por etapa"
Inválido: "MIENTRAS se completa la transcripción el sistema SHALL notificar al usuario"
           → Error: "se completa" es un evento puntual, no un estado continuo. Sugerir clasificación Event-Driven.
```

### Workflow de Validación EARS

| ID | Palabras Clave | Estado |
|----|----------------|--------|
| RF-16 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-17 | WHEN, THE SYSTEM SHALL | ✅ Cumple |

**Estado general**: `approved`

### 3.1.8 EARS — Requisitos Opcionales (Optional)

**Clasificación EARS**: Optional

Los requisitos Opcionales describen funcionalidades que el sistema SHALL proporcionar solo si una característica o condición específica está presente en la configuración del sistema.

**Sintaxis formal**:
```
WHERE <característica> <entidad> SHALL <acción>
WHERE <característica> <entidad> SHALL <acción> <objeto>
DONDE <característica> <entidad> SHALL <acción>
```

**Reglas de validación estrictas**:
1. La cláusula WHERE/DONDE es obligatoria y debe iniciar el requisito.
2. La característica debe ser un componente o funcionalidad opcional del sistema.
3. Si la característica no está presente en la configuración, el requisito no aplica.
4. El verbo modal SHALL es obligatorio.
5. La característica debe ser un sustantivo que denote un componente opcional.

**Algoritmo de clasificación**:
1. Verificar presencia del token WHERE o DONDE al inicio del requisito.
2. Verificar que la característica referenciada sea un componente opcional configurable.
3. Verificar presencia de SHALL en la cláusula de acción.
4. Verificar que no existan tokens de evento (WHEN) o estado (WHILE).
5. Si todas las verificaciones pasan, clasificar como Optional.

| ID | Requisito | Implementación/Especificación |
|----|-----------|-------------------------------|
| RF-18 | El sistema SHALL clasificar un requisito como Optional cuando contenga WHERE/DONDE describiendo una característica condicional | `ears-grammar-validation/spec.md` — Escenario: Optional requirement detected |
| RF-19 | El sistema SHALL validar que los requisitos Optional sigan el patrón `WHERE <feature> <entity> SHALL <action>` | `ears-grammar-validation/spec.md` — Strict syntax validation rules for Optional |

**Ejemplos**:

```
Válido:   "WHERE la transcripción está habilitada el sistema SHALL mostrar el texto transcrito"
Válido:   "DONDE el modelo GPU está disponible el sistema SHALL acelerar la inferencia con CUDA"
Inválido: "DONDE el usuario lo solicita el sistema SHALL generar el documento"
           → Error: "el usuario lo solicita" es un evento, no una característica opcional. Sugerir Event-Driven.
```

### Workflow de Validación EARS

| ID | Palabras Clave | Estado |
|----|----------------|--------|
| RF-18 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-19 | WHEN, THE SYSTEM SHALL | ✅ Cumple |

**Estado general**: `approved`

### 3.1.9 EARS — Requisitos Deseados (Desired)

**Clasificación EARS**: Desired

Los requisitos Deseados expresan funcionalidades que el sistema SHOULD (debería) implementar, pero que no son obligatorias. Utilizan SHOULD o WANT en lugar de SHALL para indicar prioridad reducida.

**Sintaxis formal**:
```
<entidad> SHOULD <acción>
<entidad> SHOULD <acción> <objeto>
<entidad> WANT <acción>
<entidad> DEBERÍA <acción>
```

**Reglas de validación estrictas**:
1. El verbo modal SHOULD o WANT (o DEBERÍA en español) reemplaza a SHALL.
2. La estructura es idéntica a Ubicuo pero con un modal de menor prioridad.
3. El sistema SHALL marcar estos requisitos como no obligatorios en el documento SRS.
4. Pueden combinarse con cláusulas condicionales (WHEN, WHERE) para mayor precisión.

**Algoritmo de clasificación**:
1. Verificar presencia de tokens SHOULD, WANT o DEBERÍA.
2. Verificar ausencia de SHALL (si SHALL está presente, no es Desired).
3. Clasificar como Desired y asignar prioridad baja.
4. Incluir nota en el documento SRS indicando que es un requisito deseado no obligatorio.

| ID | Requisito | Implementación/Especificación |
|----|-----------|-------------------------------|
| RF-20 | El sistema SHALL clasificar un requisito como Desired cuando contenga SHOULD/WANT en lugar de SHALL | `ears-grammar-validation/spec.md` — Escenario: Desired requirement detected |
| RF-21 | El sistema SHALL validar que los requisitos Desired sigan el patrón `<entity> SHOULD <action>` y marcar como no obligatorios | `ears-grammar-validation/spec.md` — Strict syntax validation rules for Desired |

**Ejemplos**:

```
Válido:   "El sistema SHOULD soportar formatos adicionales de audio"
Válido:   "El sistema WANT proporcionar exportación a PDF"
Válido:   "WHEN hay GPU disponible el sistema SHOULD usar el modelo Whisper large"
          → Nota: Desired con condición Event-Driven. Prioridad baja.
Inválido: "El sistema SHALL soportar múltiples idiomas SHOULD ser prioridad"
           → Error: Mezcla de SHALL (obligatorio) y SHOULD (deseado). Ambiguo.
```

### Workflow de Validación EARS

| ID | Palabras Clave | Estado |
|----|----------------|--------|
| RF-20 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-21 | WHEN, THE SYSTEM SHALL | ✅ Cumple |

**Estado general**: `approved`

### 3.1.10 Transcripción de Audio

**Clasificación EARS**: Event-Driven / Ubiquitous

| ID | Requisito | Especificación |
|----|-----------|----------------|
| RF-22 | El sistema SHALL usar OpenAI Whisper (modelo local) para transcribir grabaciones de audio de entrevistas a texto | `audio-transcription/spec.md` — Requirement: Audio-to-text transcription |
| RF-23 | El sistema SHALL aceptar archivos de audio en formatos WAV, MP3, M4A y FLAC | `audio-transcription/spec.md` — Escenario: Upload and transcribe audio |
| RF-24 | El sistema SHALL preprocesar los archivos de audio: remuestreo a 16kHz, conversión a mono, normalización de volumen | `audio-transcription/spec.md` — Requirement: Audio preprocessing |
| RF-25 | El sistema SHALL incluir marcas temporales por segmento en la transcripción para trazabilidad | `audio-transcription/spec.md` — Escenario: Transcription with timestamps |
| RF-26 | El sistema SHALL soportar transcripción en español con opción de configurar el idioma de origen | `audio-transcription/spec.md` — Requirement: Multilingual transcription |

**Escenarios**:

#### Escenario: Transcripción exitosa
- **CUANDO** el usuario sube un archivo de audio válido y selecciona *Transcribir*
- **ENTONCES** el sistema procesa el audio mediante Whisper y retorna el texto transcrito con segmentos y marcas temporales

#### Escenario: Preprocesamiento automático
- **CUANDO** un archivo de audio es subido
- **ENTONCES** el sistema lo remuestrea a 16kHz, convierte a mono y normaliza el volumen antes de la transcripción

#### Escenario: Configuración de idioma
- **CUANDO** el idioma se configura como español
- **ENTONCES** el sistema pasa el parámetro `language="es"` a Whisper para mejorar la precisión

### Workflow de Validación EARS

| ID | Palabras Clave | Estado |
|----|----------------|--------|
| RF-22 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-23 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-24 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-25 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-26 | WHEN, THE SYSTEM SHALL | ✅ Cumple |

**Estado general**: `approved`

### 3.1.11 Generación de Requisitos mediante LLM

**Clasificación EARS**: Event-Driven

| ID | Requisito | Especificación |
|----|-----------|----------------|
| RF-27 | El sistema SHALL usar un modelo de lenguaje local para generar requisitos IEEE 830 estructurados a partir de la transcripción y el contexto del proyecto | `ai-requirement-generation/spec.md` — Requirement: LLM-based requirement generation |
| RF-28 | El sistema SHALL construir un prompt estructurado que incluya: reglas IEEE 830, sintaxis EARS, descripción del proyecto y texto transcrito | `ai-requirement-generation/spec.md` — Requirement: Prompt engineering for IEEE 830 |
| RF-29 | El sistema SHALL soportar inferencia local mediante Ollama REST API | `ai-requirement-generation/spec.md` — Escenario: Inference via Ollama |
| RF-30 | El sistema SHALL soportar inferencia local mediante servidor LlamaCpp | `ai-requirement-generation/spec.md` — Escenario: Inference via LlamaCpp |
| RF-31 | El sistema SHALL parsear la respuesta del LLM en secciones IEEE 830 (requisitos funcionales, no funcionales, interfaces) | `ai-requirement-generation/spec.md` — Escenario: Receive structured output |

**Escenarios**:

#### Escenario: Generación desde transcripción
- **CUANDO** el usuario inicia la generación de requisitos con una transcripción completada
- **ENTONCES** el sistema construye el prompt con el contexto del proyecto y la transcripción, lo envía al LLM local, y parsea la respuesta estructurada

#### Escenario: Prompt con reglas del estándar
- **CUANDO** se construye el prompt para generación de requisitos
- **ENTONCES** el sistema incluye la plantilla de secciones IEEE 830 y las reglas de sintaxis EARS en el prompt del sistema

#### Escenario: Inferencia via Ollama
- **CUANDO** el sistema envía una solicitud de generación a Ollama
- **ENTONCES** usa la API REST de Ollama (`POST /api/generate`) con el modelo configurado y `stream: false`

#### Escenario: Inferencia via LlamaCpp
- **CUANDO** el sistema envía una solicitud de generación a LlamaCpp
- **ENTONCES** usa la API del servidor LlamaCpp (`POST /completion`) con el modelo y ventana de contexto configurados

### Workflow de Validación EARS

| ID | Palabras Clave | Estado |
|----|----------------|--------|
| RF-27 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-28 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-29 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-30 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-31 | WHEN, THE SYSTEM SHALL | ✅ Cumple |

**Estado general**: `approved`

### 3.1.12 Validación Gramatical EARS

**Clasificación EARS**: Ubiquitous

| ID | Requisito | Especificación |
|----|-----------|----------------|
| RF-32 | El sistema SHALL validar que cada requisito generado conforme a una de las cinco categorías EARS | `ears-grammar-validation/spec.md` — Requirement: EARS grammar validation engine |
| RF-33 | El sistema SHALL clasificar automáticamente cada requisito en la categoría EARS correspondiente | `ears-grammar-validation/spec.md` — Escenarios de clasificación |
| RF-34 | El sistema SHALL aplicar reglas de validación estrictas para cada categoría EARS | `ears-grammar-validation/spec.md` — Strict syntax validation rules |
| RF-35 | El sistema SHALL proporcionar mensajes de error específicos cuando un requisito falle la validación, indicando la regla violada y una sugerencia de corrección | `ears-grammar-validation/spec.md` — Requirement: Validation error reporting |

**Escenarios**:

#### Escenario: Validación exitosa
- **CUANDO** un requisito cumple con todas las reglas sintácticas de su categoría EARS
- **ENTONCES** el sistema lo marca como válido y lo incluye en el documento SRS con su clasificación

#### Escenario: Error de sintaxis con sugerencia
- **CUANDO** un requisito no cumple la sintaxis de su categoría
- **ENTONCES** el sistema retorna la categoría EARS intentada, la regla violada, y un ejemplo corregido

#### Escenario: Clasificación ambigua
- **CUANDO** un requisito contiene tokens de múltiples categorías EARS (ej. WHEN y WHILE simultáneamente)
- **ENTONCES** el sistema reporta la ambigüedad y sugiere dividir el requisito en requisitos más específicos

### Workflow de Validación EARS

| ID | Palabras Clave | Estado |
|----|----------------|--------|
| RF-32 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-33 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-34 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-35 | WHEN, THE SYSTEM SHALL | ✅ Cumple |

**Estado general**: `approved`

### 3.1.13 Orquestación del Pipeline

**Clasificación EARS**: Event-Driven

| ID | Requisito | Especificación |
|----|-----------|----------------|
| RF-36 | El sistema SHALL coordinar las etapas del pipeline IA en secuencia: transcripción → generación LLM → validación EARS → ensamblado SRS | `ai-pipeline-orchestration/spec.md` — Requirement: Pipeline orchestration |
| RF-37 | El sistema SHALL mostrar el progreso de cada etapa del pipeline en tiempo real | `ai-pipeline-orchestration/spec.md` — Escenario: Stage-by-stage visibility |
| RF-38 | El sistema SHALL manejar errores en cualquier etapa del pipeline, reportando la etapa y el error específico | `ai-pipeline-orchestration/spec.md` — Requirement: Pipeline error handling |
| RF-39 | El sistema SHALL reintentar una vez cuando el LLM local no responda dentro del tiempo de espera configurado | `ai-pipeline-orchestration/spec.md` — Escenario: LLM timeout |
| RF-40 | El sistema SHALL detener el pipeline si la transcripción falla y reportar el error sin proceder a generación LLM | `ai-pipeline-orchestration/spec.md` — Escenario: Transcription failure |
| RF-41 | El sistema SHALL permitir al usuario configurar: modelo LLM, tamaño de Whisper, idioma y tiempos de espera | `ai-pipeline-orchestration/spec.md` — Requirement: Configuration management |
| RF-42 | El sistema SHALL ensamblar los requisitos validados en un documento SRS estructurado en formato IEEE 830 | `ai-pipeline-orchestration/spec.md` — Requirement: SRS output assembly |

**Escenarios**:

#### Escenario: Ejecución completa del pipeline
- **CUANDO** el usuario inicia el flujo de trabajo asistido por IA con un archivo de audio
- **ENTONCES** el sistema ejecuta todas las etapas en secuencia: transcribir audio, generar requisitos via LLM, validar con EARS, y presentar el SRS validado

#### Escenario: Fallo en transcripción
- **CUANDO** la transcripción con Whisper falla debido a audio corrupto
- **ENTONCES** el sistema detiene el pipeline y reporta el error sin proceder a la generación LLM

#### Escenario: Timeout del LLM
- **CUANDO** el LLM local no responde dentro del tiempo de espera configurado
- **ENTONCES** el sistema reintenta una vez y luego aborta con un mensaje de error de timeout

#### Escenario: Configuración del pipeline
- **CUANDO** el usuario abre el panel de configuración
- **ENTONCES** el sistema muestra campos editables para selección de modelo, idioma y parámetros de timeout

### Workflow de Validación EARS

| ID | Palabras Clave | Estado |
|----|----------------|--------|
| RF-36 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-37 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-38 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-39 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-40 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-41 | WHEN, THE SYSTEM SHALL | ✅ Cumple |
| RF-42 | WHEN, THE SYSTEM SHALL | ✅ Cumple |

**Estado general**: `approved`

## 3.2 Requisitos No Funcionales

### 3.2.1 Usabilidad

| ID | Requisito |
|----|-----------|
| RNF-01 | La interfaz SHALL ser intuitiva y requerir cero capacitación para su uso |
| RNF-02 | Los mensajes de error SHALL estar en español y ser descriptivos |
| RNF-03 | La tabla de proyectos SHALL utilizar el ancho completo del contenedor para mejor legibilidad |
| RNF-04 | El pipeline SHALL mostrar el estado y progreso de cada etapa de forma visible durante la ejecución |
| RNF-05 | El sistema SHALL proporcionar un panel de configuración accesible para los parámetros del pipeline |
| RNF-06 | El sistema SHALL mostrar una vista previa de la transcripción antes de proceder a la generación de requisitos |
| RNF-07 | El sistema SHALL presentar un informe de validación EARS que muestre qué requisitos pasaron y cuáles fallaron, con detalles de cada error |

### 3.2.2 Rendimiento

| ID | Requisito |
|----|-----------|
| RNF-08 | El sistema SHALL responder a las acciones del usuario del módulo base en menos de 2 segundos |
| RNF-09 | La tabla SHALL soportar al menos 100 proyectos sin degradación visible del rendimiento |
| RNF-10 | El pipeline SHALL completar la inferencia LLM en menos de 30 segundos para modelos ≤7B con GPU disponible |
| RNF-11 | El pipeline SHALL completar la inferencia LLM en menos de 120 segundos para modelos ≤3B en CPU |
| RNF-12 | El tiempo de transcripción SHALL ser menor a 3 veces la duración del audio para Whisper small en GPU |
| RNF-13 | El tiempo de transcripción SHALL ser menor a 10 veces la duración del audio para Whisper small en CPU |
| RNF-14 | El motor de validación EARS SHALL procesar al menos 100 requisitos por segundo en cualquier hardware |

### 3.2.3 Confiabilidad

| ID | Requisito |
|----|-----------|
| RNF-15 | El sistema SHALL manejar la ausencia del archivo de datos sin lanzar excepciones |
| RNF-16 | El sistema SHALL preservar los datos entre reinicios de la aplicación |
| RNF-17 | El sistema SHALL reintentar una vez la conexión al LLM antes de reportar fallo |
| RNF-18 | El sistema SHALL verificar la disponibilidad del endpoint Ollama/LlamaCpp antes de iniciar la generación |
| RNF-19 | El sistema SHALL verificar que el modelo Whisper seleccionado esté descargado antes de iniciar la transcripción |
| RNF-20 | El pipeline SHALL registrar en un log interno cada etapa completada para permitir reinicio desde puntos de control |

### 3.2.4 Precisión

| ID | Requisito |
|----|-----------|
| RNF-21 | El sistema SHALL mantener una tasa de error de palabras (WER) menor al 10% en la transcripción Whisper con modelo small o superior en audio limpio |
| RNF-22 | El sistema SHALL mantener una precisión de clasificación EARS mayor al 95% en requisitos bien formados |
| RNF-23 | El sistema SHALL lograr que al menos el 85% de los requisitos generados por el LLM cumplan la estructura IEEE 830 sin correcciones mayores |

### 3.2.5 Mantenibilidad

| ID | Requisito |
|----|-----------|
| RNF-24 | El código SHALL estar documentado con referencias a los requisitos IEEE 830 |
| RNF-25 | El modelo de datos SHALL estar definido con Pydantic para validación explícita y autodocumentada |
| RNF-26 | Cada categoría EARS SHALL estar implementada como un validador independiente y testeable |
| RNF-27 | La integración con Ollama y LlamaCpp SHALL estar encapsulada en clases abstractas de cliente LLM para permitir la adición de nuevos backends |

### 3.2.6 Requisitos de Hardware

| ID | Requisito |
|----|-----------|
| RNF-28 | El sistema SHALL funcionar con un mínimo de 8 GB de RAM para operación básica (Whisper small + LLM 3B) |
| RNF-29 | El sistema SHALL recomendar 16 GB de RAM para operación completa (Whisper large + LLM 7B) |
| RNF-30 | El sistema SHALL funcionar sin GPU dedicada utilizando modelos pequeños en CPU |
| RNF-31 | El sistema SHALL requerir al menos 10 GB de espacio libre en disco para los modelos descargados |
| RNF-32 | El sistema SHALL recomendar GPU con 4 GB+ VRAM para Whisper medium/large y LLM 7B |

## 3.3 Interfaces Externas

### 3.3.1 Interfaz de Usuario

- **Framework**: Streamlit
- La interfaz consta de dos modos principales:
  - **Modo base**: Título y subtítulo del sistema, formulario de registro centrado, tabla de proyectos registrados (aparece solo cuando hay datos)
  - **Modo pipeline**: Subida de audio con selector de archivos, visor de transcripción con marcas temporales, panel de configuración del pipeline (modelo LLM, tamaño Whisper, idioma, timeout), visualizador de requisitos generados, panel de validación EARS con resultados por requisito, documento SRS ensamblado

### 3.3.2 Interfaz de Archivos

- Archivo de datos base: `proyectos_sgr.json`
- Formato: JSON con codificación UTF-8
- Ubicación: Mismo directorio que `app.py`
- Archivos de audio: Almacenamiento temporal durante el procesamiento del pipeline

### 3.3.3 Interfaz de Software (Módulo Base)

- Python 3.11+
- `streamlit` — framework de aplicación web
- `pydantic` — validación de datos
- `json` — serialización (biblioteca estándar)
- `os` — operaciones de sistema de archivos (biblioteca estándar)
- `datetime` — marcas de tiempo (biblioteca estándar)

### 3.3.4 Interfaz Ollama REST API

- **Endpoint**: `POST /api/generate`
- **Propósito**: Solicitar generación de texto al modelo LLM local ejecutado por Ollama
- **Formato de solicitud** (JSON):
  ```json
  {
    "model": "llama3:8b",
    "prompt": "[prompt del sistema + contexto + transcripción]",
    "stream": false,
    "options": {
      "temperature": 0.3,
      "top_p": 0.9,
      "max_tokens": 4096
    }
  }
  ```
- **Formato de respuesta** (JSON):
  ```json
  {
    "model": "llama3:8b",
    "response": "texto generado...",
    "done": true,
    "total_duration": 12345678900,
    "eval_count": 1024
  }
  ```
- **Parámetros configurables**: `model` (nombre del modelo), `temperature` (0.0-1.0), `max_tokens` (límite de generación)
- **Manejo de errores**: Timeout configurable (por defecto 60s), reintento automático una vez ante fallo de conexión

### 3.3.5 Interfaz LlamaCpp Server

- **Endpoint**: `POST /completion`
- **Propósito**: Solicitar generación de texto al modelo LLM local ejecutado por LlamaCpp
- **Formato de solicitud** (JSON):
  ```json
  {
    "prompt": "[prompt del sistema + contexto + transcripción]",
    "n_predict": 4096,
    "temperature": 0.3,
    "top_p": 0.9,
    "stop": ["\n##", "\n\n\n"],
    "cache_prompt": true
  }
  ```
- **Formato de respuesta** (JSON):
  ```json
  {
    "content": "texto generado...",
    "stop": true,
    "tokens_predicted": 1024,
    "tokens_evaluated": 2048
  }
  ```
- **Parámetros configurables**: `n_predict` (máximo de tokens a generar), `temperature`, `stop` (secuencias de parada)
- **Ventana de contexto**: Determinada por la configuración del servidor LlamaCpp (típicamente 2048-8192 tokens)
- **Manejo de errores**: Timeout configurable (por defecto 60s), verificación de disponibilidad del servidor antes de cada solicitud

### 3.3.6 Interfaz Whisper Model

- **Integración**: Biblioteca Python `openai-whisper`
- **Modelos disponibles**:
  | Variante | Parámetros | RAM requerida | Velocidad relativa | Precisión relativa |
  |----------|------------|---------------|-------------------|-------------------|
  | tiny     | 39M        | ~1 GB         | 10x               | Baja              |
  | base     | 74M        | ~1 GB         | 7x                | Media-baja        |
  | small    | 244M       | ~2 GB         | 4x                | Media             |
  | medium   | 769M       | ~5 GB         | 2x                | Media-alta        |
  | large    | 1550M      | ~10 GB        | 1x                | Alta              |

- **Formato de entrada**: Audio preprocesado a 16kHz, mono, float32
- **Formato de salida**:
  ```python
  {
    "text": "texto completo transcrito...",
    "segments": [
      {
        "start": 0.0,
        "end": 5.2,
        "text": "texto del segmento..."
      },
      ...
    ],
    "language": "es"
  }
  ```
- **Parámetros de transcripción**: `model` (variante), `language` (código ISO), `task` ("transcribe" o "translate"), `beam_size` (tamaño del haz de búsqueda)
- **Preprocesamiento interno**: Remuestreo a 16kHz, conversión a mono, normalización de amplitud

### 3.3.7 Formato de Datos del Pipeline

Los datos intermedios del pipeline se transmiten entre etapas en estructuras de datos bien definidas:

**TranscriptChunk** (salida de Whisper → entrada a LLM):
```python
{
  "project_id": "uuid",
  "transcription": {
    "full_text": "texto completo...",
    "segments": [{"start": 0.0, "end": 5.2, "text": "..."}],
    "language": "es",
    "duration_seconds": 120.5,
    "model_used": "whisper-small"
  },
  "project_context": {
    "nombre": "Sistema de Gestión",
    "objetivo": "Automatizar...",
    "dominio": "Gestión empresarial"
  }
}
```

**StructuredRequirements** (salida de LLM → entrada a validador EARS):
```python
{
  "requirements": [
    {
      "id": "REQ-001",
      "text": "El sistema SHALL proporcionar un formulario de registro",
      "section": "funcional",
      "raw_text": "..."
    },
    ...
  ],
  "metadata": {
    "model": "llama3:8b",
    "prompt_tokens": 2048,
    "generation_time_ms": 15000
  }
}
```

**ValidationResult** (salida del validador EARS → entrada al ensamblador SRS):
```python
{
  "requirement_id": "REQ-001",
  "original_text": "...",
  "ears_classification": {
    "category": "ubiquitous",
    "confidence": 0.98,
    "matched_rules": ["has_shall", "no_conditional_clauses"]
  },
  "validation": {
    "is_valid": true,
    "errors": [],
    "warnings": []
  }
}
```

## 3.4 Mapeo Completo: Requisitos ↔ Código / Especificación

### Mapeo de requisitos del módulo base:

| ID | Requisito | Archivo | Líneas / Especificación |
|----|-----------|---------|------------------------|
| RF-01 | Formulario de registro | `app.py` | 40-44 |
| RF-02 | Botón Registrar | `app.py` | 44 |
| RF-03 | Validación Pydantic | `app.py` | 11-15, 46-59 |
| RF-04 | Guardar en JSON | `app.py` | 25-30 |
| RF-05 | Cargar desde JSON | `app.py` | 18-22 |
| RF-06 | Estructura de datos | `app.py` | 11-15 |
| RF-07 | Manejo de archivo ausente | `app.py` | 19 |
| RF-08 | Tabla de proyectos | `app.py` | 66-67 |
| RF-09 | Actualización de tabla | `app.py` | 61-62 |
| RF-10 | Mensaje de éxito | `app.py` | 54 |
| RF-11 | session_state | `app.py` | 55, 61-62 |

### Mapeo de requisitos del pipeline IA:

| ID | Requisito | Especificación |
|----|-----------|----------------|
| RF-12 | Clasificación Ubicuo EARS | `openspec/specs/ears-grammar-validation/spec.md` |
| RF-13 | Validación sintaxis Ubicuo | `openspec/specs/ears-grammar-validation/spec.md` |
| RF-14 | Clasificación Event-Driven EARS | `openspec/specs/ears-grammar-validation/spec.md` |
| RF-15 | Validación sintaxis Event-Driven | `openspec/specs/ears-grammar-validation/spec.md` |
| RF-16 | Clasificación State-Driven EARS | `openspec/specs/ears-grammar-validation/spec.md` |
| RF-17 | Validación sintaxis State-Driven | `openspec/specs/ears-grammar-validation/spec.md` |
| RF-18 | Clasificación Optional EARS | `openspec/specs/ears-grammar-validation/spec.md` |
| RF-19 | Validación sintaxis Optional | `openspec/specs/ears-grammar-validation/spec.md` |
| RF-20 | Clasificación Desired EARS | `openspec/specs/ears-grammar-validation/spec.md` |
| RF-21 | Validación sintaxis Desired | `openspec/specs/ears-grammar-validation/spec.md` |
| RF-22 | Transcripción Whisper | `openspec/specs/audio-transcription/spec.md` |
| RF-23 | Formatos de audio aceptados | `openspec/specs/audio-transcription/spec.md` |
| RF-24 | Preprocesamiento de audio | `openspec/specs/audio-transcription/spec.md` |
| RF-25 | Marcas temporales en transcripción | `openspec/specs/audio-transcription/spec.md` |
| RF-26 | Transcripción multilingüe | `openspec/specs/audio-transcription/spec.md` |
| RF-27 | Generación LLM de requisitos | `openspec/specs/ai-requirement-generation/spec.md` |
| RF-28 | Prompt engineering IEEE 830 | `openspec/specs/ai-requirement-generation/spec.md` |
| RF-29 | Integración Ollama | `openspec/specs/ai-requirement-generation/spec.md` |
| RF-30 | Integración LlamaCpp | `openspec/specs/ai-requirement-generation/spec.md` |
| RF-31 | Parseo de respuesta LLM | `openspec/specs/ai-requirement-generation/spec.md` |
| RF-32 | Motor de validación EARS | `openspec/specs/ears-grammar-validation/spec.md` |
| RF-33 | Clasificación automática EARS | `openspec/specs/ears-grammar-validation/spec.md` |
| RF-34 | Validación estricta por categoría | `openspec/specs/ears-grammar-validation/spec.md` |
| RF-35 | Mensajes de error con sugerencias | `openspec/specs/ears-grammar-validation/spec.md` |
| RF-36 | Orquestación del pipeline | `openspec/specs/ai-pipeline-orchestration/spec.md` |
| RF-37 | Visibilidad de progreso | `openspec/specs/ai-pipeline-orchestration/spec.md` |
| RF-38 | Manejo de errores del pipeline | `openspec/specs/ai-pipeline-orchestration/spec.md` |
| RF-39 | Reintento LLM por timeout | `openspec/specs/ai-pipeline-orchestration/spec.md` |
| RF-40 | Detención por fallo de transcripción | `openspec/specs/ai-pipeline-orchestration/spec.md` |
| RF-41 | Configuración del pipeline | `openspec/specs/ai-pipeline-orchestration/spec.md` |
| RF-42 | Ensamblado SRS | `openspec/specs/ai-pipeline-orchestration/spec.md` |

### Mapeo de requisitos no funcionales:

| ID | Requisito | Especificación |
|----|-----------|----------------|
| RNF-01 a RNF-07 | Usabilidad | Este documento, sección 3.2.1-3.2.6 |
| RNF-08 a RNF-14 | Rendimiento | Este documento, sección 3.2.2 |
| RNF-15 a RNF-20 | Confiabilidad | Este documento, sección 3.2.3 |
| RNF-21 a RNF-23 | Precisión | Este documento, sección 3.2.4 |
| RNF-24 a RNF-27 | Mantenibilidad | Este documento, sección 3.2.5 |
| RNF-28 a RNF-32 | Hardware | Este documento, sección 3.2.6 |

---

*Documento generado como parte del artefacto de especificación del cambio `expansion-srs-ia-pipeline`.*
*Basado en IEEE Std 830-1998 y EARS (Mavin et al., 2009).*
