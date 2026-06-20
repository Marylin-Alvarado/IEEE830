# GUIÓN TÉCNICO: SGR - Sistema de Generación de Requisitos
## Cómo funciona "por debajo" y "por encima" - Arquitectura Completa

---

## 📋 TABLA DE CONTENIDOS

1. [Visión General](#visión-general)
2. [Arquitectura de Alto Nivel](#arquitectura-de-alto-nivel)
3. [Flujo Completo del Sistema](#flujo-completo-del-sistema)
4. [Por Debajo: Componentes Técnicos](#por-debajo-componentes-técnicos)
5. [Por Encima: Interfaz de Usuario](#por-encima-interfaz-de-usuario)
6. [Integración de Componentes](#integración-de-componentes)
7. [Pipeline de IA Detallado](#pipeline-de-ia-detallado)
8. [Flujos de Datos](#flujos-de-datos)

---

## 📊 CRITERIOS DE EVALUACIÓN - RÚBRICA APE

### 1. [Estructura del Informe](#1-estructura-del-informe) (1.0 puntos)
### 2. [Especificaciones Formales](#2-especificaciones-formales) (2.0 puntos)
### 3. [Código e Implementación](#3-código-e-implementación) (2.0 puntos)
### 4. [Validación y Coherencia](#4-validación-y-coherencia) (2.0 puntos)
### 5. [Demostración del Sistema](#5-demostración-del-sistema) (2.0 puntos)
### 6. [Conclusiones y Reflexión Ética](#6-conclusiones-y-reflexión-ética) (1.0 puntos)

---

## 🎯 VISIÓN GENERAL

El **SGR (Sistema de Generación de Requisitos)** es una herramienta de escritorio que **automatiza la captura, generación y validación de requisitos de software** mediante inteligencia artificial. 

### Problema que Resuelve
Las entrevistas con clientes/usuarios generan:
- ❌ Información dispersa y ambigua
- ❌ Requisitos incompletos o contradictorios  
- ❌ Documentación poco estructurada
- ❌ Pérdida de información

### Solución del SGR
✅ **Entrevista → Audio → Transcripción → LLM → Requisitos Estructurados → Validación EARS → Documento IEEE 830**

El sistema trabaja en **dos capas**:
- **🎨 Por Encima (UI)**: Streamlit - interfaz amigable para usuarios
- **⚙️ Por Debajo (Motor)**: Whisper + LLM + EARS - máquinas que procesan datos

---

## 🏗️ ARQUITECTURA DE ALTO NIVEL

```
┌─────────────────────────────────────────────────────────────┐
│                    SGR - SISTEMA COMPLETO                   │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │    CAPA DE PRESENTACIÓN (POR ENCIMA)                │   │
│  │    ────────────────────────────────────────────      │   │
│  │  Streamlit Web App                                   │   │
│  │  ├─ Registro de Proyectos                           │   │
│  │  ├─ Visualización de Requisitos                     │   │
│  │  ├─ Interfaz del Pipeline                           │   │
│  │  └─ Feedback del Usuario                            │   │
│  └──────────────────────────────────────────────────────┘   │
│                          ↓↑                                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │    CAPA DE LÓGICA DE NEGOCIO (EN MEDIO)             │   │
│  │    ────────────────────────────────────────────      │   │
│  │  Orquestador de Pipeline                            │   │
│  │  ├─ Gestor de Proyectos (Pydantic)                  │   │
│  │  ├─ Coordinador de Etapas                           │   │
│  │  └─ Manejo de Errores                               │   │
│  └──────────────────────────────────────────────────────┘   │
│                          ↓↑                                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │    CAPA DE PROCESAMIENTO (POR DEBAJO)               │   │
│  │    ────────────────────────────────────────────      │   │
│  │  Motor de Inteligencia Artificial                    │   │
│  │  ├─ 🎙️  Whisper (Transcripción Audio)              │   │
│  │  ├─ 🧠 LLM Local (Generación de Requisitos)        │   │
│  │  ├─ ✓ EARS Validator (Validación Gramatical)       │   │
│  │  └─ 💾 Persistencia JSON (Datos)                    │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 FLUJO COMPLETO DEL SISTEMA

### Escenario Típico de Uso

```
USUARIO                    SISTEMA SGR
───────────────────────────────────────────────────────────────

1. Inicia la app      →    Streamlit carga la UI
                            ├─ Lee proyectos_sgr.json
                            └─ Muestra tabla de proyectos

2. Registra proyecto  →    Valida con Pydantic
                            ├─ Verifica campos requeridos
                            ├─ Guarda en JSON
                            └─ Actualiza tabla dinámicamente

3. Sube archivo audio →    Streamlit recibe archivo
                            │
                      ↓ ENTRA AL PIPELINE
                            │
4. Inicia pipeline    →    Orquestador coordina:
                            ├─ ETAPA 1: Whisper transcribe
                            ├─ ETAPA 2: LLM genera requisitos
                            ├─ ETAPA 3: EARS valida c/requisito
                            └─ ETAPA 4: Ensambla documento SRS
                            │
5. Ve resultados      ←    Streamlit muestra:
                            ├─ Requisitos funcionales (fichas)
                            ├─ Requisitos no funcionales (tabla)
                            └─ Validaciones EARS (estado ✓/✗)

6. Descarga SRS       ←    Documento IEEE 830 generado
```

---

## ⚙️ POR DEBAJO: COMPONENTES TÉCNICOS

### 1️⃣ COMPONENTE: PERSISTENCIA DE DATOS

**Ubicación**: `proyectos_sgr.json` (archivo local)

**Tecnología**: JSON + Pydantic

**¿Qué hace?**
- Guarda información de proyectos registrados
- Se carga automáticamente al iniciar
- Formatos validados por Pydantic

**Estructura de Datos**:
```json
{
  "proyectos": [
    {
      "id": "uuid-xxx",
      "nombre": "Sistema de Ventas",
      "objetivo": "Automatizar proceso de ventas",
      "dominio": "E-commerce",
      "fecha_registro": "2026-06-19T14:30:00",
      "requisitos": {
        "funcionales": [...],
        "no_funcionales": [...]
      }
    }
  ]
}
```

**Validación Pydantic**:
```python
class Proyecto(BaseModel):
    nombre: StrictStr = Field(..., min_length=1)
    objetivo: StrictStr = Field(..., min_length=1)
    dominio: StrictStr = Field(..., min_length=1)
    # Fuerza campos obligatorios con longitud mínima
```

---

### 2️⃣ COMPONENTE: TRANSCRIPCIÓN DE AUDIO (WHISPER)

**Ubicación**: Integración con modelo Whisper local

**Tecnología**: OpenAI Whisper (modelo local)

**¿Qué hace?**
- Convierte archivos de audio → texto
- Soporta múltiples formatos: WAV, MP3, M4A, FLAC
- Genera transcripciones en español
- Incluye timestamps para cada segmento

**Proceso Internamente**:

```
Archivo de Audio
    ↓
[Preprocesamiento]
    ├─ Resamplear a 16kHz (estándar Whisper)
    ├─ Convertir a mono (elimina canales adicionales)
    └─ Normalizar volumen
    ↓
[Modelo Whisper]
    ├─ Divide audio en segmentos de 30 segundos
    ├─ Procesa cada segmento (encoder-decoder)
    ├─ Genera token predicciones
    └─ Decodifica a texto español
    ↓
[Salida Transcripción]
{
  "text": "El sistema debe validar los datos...",
  "segments": [
    {
      "id": 0,
      "start": 0.0,
      "end": 5.2,
      "text": "El sistema debe..."
    },
    ...
  ]
}
```

**¿Por qué local?**
- 🔒 Privacidad: no sube datos a servidores
- 💰 Gratis: sin costos de API
- ⚡ Rápido: ejecución en máquina local
- 🌐 Sin conexión: funciona desconectado

---

### 3️⃣ COMPONENTE: GENERACIÓN DE REQUISITOS (LLM)

**Ubicación**: Conexión a Ollama o LlamaCpp local

**Tecnología**: Modelos LLM locales (Mistral, Llama, etc.)

**¿Qué hace?**
- Recibe transcripción + contexto del proyecto
- Genera requisitos estructurados automáticamente
- Sigue plantilla IEEE 830
- Produce requisitos funcionales y no funcionales

**Proceso Internamente**:

```
[ENTRADA]
Contexto del Proyecto + Transcripción
    ├─ Nombre proyecto: "Sistema de Ventas"
    ├─ Objetivo: "Automatizar ventas"
    ├─ Dominio: "E-commerce"
    └─ Transcripción: "...el cliente necesita poder ver el carrito..."

    ↓
[PROMPT ENGINEERING - Sistema Prompt]

    Eres un ingeniero de requisitos experto. Tu tarea es:
    1. Analizar la transcripción de la entrevista
    2. Generar requisitos IEEE 830-1998 válidos
    3. Cada requisito DEBE seguir sintaxis EARS
    
    Plantilla IEEE 830:
    - Requisitos Funcionales: [RF-XX] Nombre - SHALL...
    - Requisitos No Funcionales: [RNF-XX] Requisito - Categoría
    
    Categorías EARS:
    - Ubicuo: "El sistema SHALL..."
    - Disparado: "WHEN... THEN el sistema SHALL..."
    - Estado: "WHILE... el sistema SHALL..."
    - Opcional: "WHERE... el sistema SHALL..."
    - Deseado: "El sistema SHOULD..."
    
    ↓
[LLAMADA AL LLM]

    POST http://localhost:11434/api/generate
    {
      "model": "mistral:latest",
      "prompt": "[PROMPT COMPLETO]",
      "stream": false
    }
    
    ↓
[LLM PROCESA]
    El modelo:
    1. Analiza transcripción
    2. Identifica conceptos clave
    3. Genera requisitos one-by-one
    4. Sigue estructura mandatoria
    5. Retorna texto estructurado

    ↓
[SALIDA LLM - Requisitos Brutos]

    ## Requisitos Funcionales
    
    ### RF-01 Visualizar Carrito
    **Categoría:** Ubicuo
    **Descripción EARS:** El sistema SHALL proporcionar una página 
    para visualizar los artículos en el carrito
    
    ### RF-02 Agregar Producto
    **Categoría:** Event-Driven
    **Descripción EARS:** WHEN el usuario hace clic en "Agregar al 
    carrito" THEN el sistema SHALL añadir el producto a la sesión
    
    ...
```

**Configuración Disponible**:
```
OLLAMA_HOST = http://localhost:11434
OLLAMA_MODEL = mistral:latest
TIMEOUT = 60 segundos
```

---

### 4️⃣ COMPONENTE: VALIDACIÓN EARS

**Ubicación**: Motor de validación gramatical

**Tecnología**: Parser y regex especializados

**¿Qué hace?**
- Valida que cada requisito sea sintácticamente correcto
- Clasifica en una de 5 categorías EARS
- Detecta errores gramaticales
- Proporciona mensajes de corrección

**Categorías EARS y Validación**:

#### 🟢 CATEGORÍA 1: UBICUO (Ubiquitous)
```
Patrón: <entidad> SHALL <acción>

Ejemplos VÁLIDOS:
✓ "El sistema SHALL validar los datos"
✓ "El usuario SHALL iniciar sesión"

Ejemplos INVÁLIDOS:
✗ "WHEN el usuario... SHALL" → Tiene disparador
✗ "El sistema SHOULD validar" → Es SHOULD, no SHALL
```

#### 🟠 CATEGORÍA 2: DISPARADO (Event-Driven)
```
Patrón: WHEN <disparador> THEN <entidad> SHALL <respuesta>

Ejemplos VÁLIDOS:
✓ "WHEN el usuario envía el formulario THEN el sistema SHALL validar"
✓ "WHEN se detecta error THEN el sistema SHALL mostrar mensaje"

Ejemplos INVÁLIDOS:
✗ "El usuario registra proyecto" → Falta WHEN
✗ "WHEN... el sistema no valida" → Usa negación
```

#### 🔵 CATEGORÍA 3: ESTADO (State-Driven)
```
Patrón: WHILE <condición> <entidad> SHALL <acción>

Ejemplos VÁLIDOS:
✓ "WHILE el archivo esté abierto el sistema SHALL bloquear escritura"
✓ "WHILE el usuario esté autenticado el sistema SHALL mostrar menú"

Ejemplos INVÁLIDOS:
✗ "UNTIL se completa el proceso" → Usa UNTIL en lugar de WHILE
```

#### 🟡 CATEGORÍA 4: OPCIONAL (Optional)
```
Patrón: WHERE <condición> <entidad> SHALL <acción>

Ejemplos VÁLIDOS:
✓ "WHERE la transcripción esté habilitada el sistema SHALL mostrar texto"
✓ "WHERE el usuario sea admin el sistema SHALL permitir editar"

Ejemplos INVÁLIDOS:
✗ "En caso de que... el sistema SHALL" → Usa "En caso de que"
```

#### ⚪ CATEGORÍA 5: DESEADO (Desired)
```
Patrón: <entidad> SHOULD <acción> (recomendación, no mandatorio)

Ejemplos VÁLIDOS:
✓ "El sistema SHOULD soportar múltiples idiomas"
✓ "El usuario WANT recibir notificaciones"

Ejemplos INVÁLIDOS:
✗ "El sistema SHOULD SHALL validar" → Mezcla SHOULD y SHALL
```

**Proceso de Validación**:

```
Requisito Ingresado
    "El sistema SHALL validar y guardar datos"
    
    ↓
[DETECCIÓN DE CATEGORÍA]
    ├─ ¿Contiene WHEN? No
    ├─ ¿Contiene WHILE? No
    ├─ ¿Contiene WHERE? No
    ├─ ¿Contiene SHALL? Sí
    ├─ ¿Contiene SHOULD? No
    └─ → CATEGORÍA: UBICUO
    
    ↓
[VALIDACIÓN ESTRICTA UBICUO]
    ├─ Estructura: <entidad> SHALL <acción>?
    │  ✓ "El sistema" (entidad) "SHALL validar y guardar" (acción)
    ├─ Sin cláusulas condicionales? ✓
    ├─ Verbo en infinitivo? ✓ (validar, guardar)
    └─ → RESULTADO: VÁLIDO ✓
    
    ↓
[SALIDA VALIDACIÓN]
    {
      "id": "RF-03",
      "categoria_ears": "Ubicuo",
      "estado": "válido",
      "errores": []
    }
```

---

### 5️⃣ COMPONENTE: ORQUESTADOR DEL PIPELINE

**Ubicación**: Coordinador central de ejecución

**Tecnología**: Coordinador secuencial con manejo de errores

**¿Qué hace?**
- Ejecuta las 4 etapas en orden
- Monitorea progreso
- Maneja errores con precisión
- Ensambla salida final IEEE 830

**Estado del Pipeline**:

```
Estados: NOT_STARTED → TRANSCRIBING → GENERATING → VALIDATING → COMPLETE/ERROR

┌─────────────────────────────────────────────────────────────┐
│                    EJECUCIÓN DEL PIPELINE                   │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  [████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 10%        │
│  🎙️  Etapa 1: Transcribiendo audio...                      │
│  └─ Esperando Whisper...                                    │
│                                                               │
│  Cuando completa ETAPA 1:                                   │
│                                                               │
│  [██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 40%        │
│  🧠 Etapa 2: Generando requisitos con LLM...              │
│  └─ Enviado prompt (450 tokens)...                         │
│  └─ Esperando respuesta del modelo...                      │
│                                                               │
│  Cuando completa ETAPA 2:                                   │
│                                                               │
│  [██████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 60%        │
│  ✓ Etapa 3: Validando EARS...                              │
│  ├─ RF-01: ✓ Válido (Ubicuo)                              │
│  ├─ RF-02: ✓ Válido (Event-Driven)                        │
│  ├─ RF-03: ⚠️  Advertencia (Sintaxis ambigua)             │
│  └─ RNF-01: ✓ Válido (Ubicuo)                             │
│                                                               │
│  [██████████████████░░░░░░░░░░░░░░░░░░░░░░░░░] 100%       │
│  📄 Etapa 4: Ensamblando documento SRS...                   │
│  └─ ✅ COMPLETADO EXITOSAMENTE                             │
│                                                               │
│  Documentos generados:                                       │
│  ├─ requisitos_funcionales.json                            │
│  ├─ requisitos_no_funcionales.json                         │
│  └─ srs_ieee830.md                                         │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**Manejo de Errores**:

```
ETAPA 1 - Transcripción
├─ Error: Archivo corrupto → Detiene pipeline
├─ Error: Formato no soportado → Detiene pipeline
└─ Error: Modelo Whisper no disponible → Detiene pipeline

ETAPA 2 - Generación LLM
├─ Error: Timeout (>60s) → Reintenta una vez
├─ Error: LLM no responde → Detiene pipeline
└─ Error: Prompt muy largo → Trunca transcripción

ETAPA 3 - Validación EARS
├─ Advertencia: Sintaxis ambigua → Continúa con flag
├─ Error: No cumple ninguna categoría → Requiere revisión
└─ Error: Estructura EARS rota → Marca para corrección manual

ETAPA 4 - Ensamblado
├─ Error: Campos faltantes → Valores por defecto
└─ Salida → Documento IEEE 830 con notas sobre errores
```

---

## 🎨 POR ENCIMA: INTERFAZ DE USUARIO

**Framework**: Streamlit (web framework Python)

**¿Qué es Streamlit?**
- Framework que convierte scripts Python en apps web interactivas
- No requiere HTML/CSS/JavaScript
- Recarga automática cuando cambia el código
- Interfaz responsive y moderna

### PÁGINA 1: Dashboard Principal

```
┌─────────────────────────────────────────────────────────┐
│  SGR - Sistema de Generación de Requisitos              │
└─────────────────────────────────────────────────────────┘

┌─ SECCIÓN: Registrar Nuevo Proyecto ──────────────────┐
│                                                        │
│  Nombre del Proyecto:     [________________]          │
│  Objetivo General:        [____________________]      │
│  Dominio/Contexto:        [____________________]      │
│                                                        │
│  [💾 Guardar Proyecto]  [❌ Limpiar]                 │
│                                                        │
│  ✅ Proyecto registrado exitosamente                  │
│                                                        │
└────────────────────────────────────────────────────────┘

┌─ SECCIÓN: Proyectos Registrados ─────────────────────┐
│                                                        │
│  Nombre              │ Objetivo        │ Dominio      │
│  ─────────────────────────────────────────────────── │
│  Sistema de Ventas   │ Automatizar... │ E-commerce   │
│  App Tareas          │ Gestionar...   │ Productivid. │
│  Plataforma Chat     │ Comunicar...   │ Redes Soc.   │
│                                                        │
└────────────────────────────────────────────────────────┘

┌─ SECCIÓN: Iniciar Pipeline de IA ──────────────────┐
│                                                     │
│  Seleccionar Proyecto: [Sistema de Ventas ▼]      │
│  Archivo de Audio:     [📁 Subir archivo]          │
│                                                     │
│  [🚀 Iniciar Pipeline]                            │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### PÁGINA 2: Ejecución del Pipeline (En Vivo)

```
┌─────────────────────────────────────────────────────────┐
│  🎯 PIPELINE EN EJECUCIÓN - Sistema de Ventas           │
└─────────────────────────────────────────────────────────┘

┌─ PROGRESO ───────────────────────────────────────────┐
│                                                       │
│  [████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 35%         │
│  Etapa actual: Transcribiendo audio...              │
│  Tiempo transcurrido: 2m 15s                        │
│  Tiempo estimado: 6m 30s                            │
│                                                       │
└───────────────────────────────────────────────────────┘

┌─ LOGS DE EJECUCIÓN ──────────────────────────────────┐
│                                                       │
│  14:30:02 [INICIO] Cargando proyecto...              │
│  14:30:03 [ETAPA-1] Iniciando Whisper               │
│  14:30:05 [ETAPA-1] Transcribiendo... 45% completo  │
│  14:30:12 [ETAPA-1] ✅ Transcripción completada     │
│  14:30:13 [ETAPA-2] Enviando a LLM...               │
│  14:30:18 [ETAPA-2] LLM procesando prompt...        │
│  [▼ Más logs]                                        │
│                                                       │
└───────────────────────────────────────────────────────┘

┌─ RESULTADOS PARCIALES ───────────────────────────────┐
│                                                       │
│  Transcripción (primeros 200 caracteres):            │
│  "El cliente necesita una interfaz para ver su       │
│   carrito de compras en tiempo real, con posibilidad │
│   de..."                                             │
│                                                       │
└───────────────────────────────────────────────────────┘

                    ⏳ Esperando...
```

### PÁGINA 3: Resultados Finales

```
┌─────────────────────────────────────────────────────────┐
│  ✅ PIPELINE COMPLETADO - Sistema de Ventas             │
│  Tiempo total: 6 minutos 45 segundos                   │
└─────────────────────────────────────────────────────────┘

┌─ RESUMEN RESULTADOS ──────────────────────────────────┐
│                                                        │
│  📊 Estadísticas:                                     │
│  ├─ Requisitos Funcionales generados: 12            │
│  ├─ Requisitos No Funcionales: 8                    │
│  ├─ Validaciones EARS: 20/20 ✓                      │
│  ├─ Advertencias: 2 ⚠️                              │
│  └─ Errores: 0                                       │
│                                                        │
│  [📥 Descargar SRS] [📋 Ver Resumen] [🔄 Nuevo]    │
│                                                        │
└────────────────────────────────────────────────────────┘

┌─ REQUISITOS FUNCIONALES ──────────────────────────────┐
│                                                        │
│  ┌─ RF-01: Visualizar Carrito ──────────────────┐   │
│  │                                                │   │
│  │  ID: RF-01                                    │   │
│  │  Prioridad: ⭐⭐⭐ Alta                      │   │
│  │  Categoría EARS: Ubicuo ✓                    │   │
│  │                                                │   │
│  │  Descripción EARS:                           │   │
│  │  El sistema SHALL proporcionar una página    │   │
│  │  para visualizar todos los artículos en el   │   │
│  │  carrito de compras activo.                  │   │
│  │                                                │   │
│  └────────────────────────────────────────────────┘   │
│                                                        │
│  ┌─ RF-02: Agregar Producto ────────────────────┐   │
│  │                                                │   │
│  │  ID: RF-02                                    │   │
│  │  Prioridad: ⭐⭐⭐ Alta                      │   │
│  │  Categoría EARS: Event-Driven ✓              │   │
│  │                                                │   │
│  │  Descripción EARS:                           │   │
│  │  WHEN el usuario hace clic en "Agregar al    │   │
│  │  carrito" THEN el sistema SHALL validar      │   │
│  │  disponibilidad y añadir el producto a la    │   │
│  │  sesión activa.                              │   │
│  │                                                │   │
│  └────────────────────────────────────────────────┘   │
│                                                        │
│  [Más fichas...]                                      │
│                                                        │
└────────────────────────────────────────────────────────┘

┌─ REQUISITOS NO FUNCIONALES ───────────────────────────┐
│                                                        │
│  ID    │ Requisito          │ Categoría  │ Prioridad │
│  ─────────────────────────────────────────────────── │
│  RNF-01│ Interfaz intuitiva │ Usabilidad │ Alta      │
│  RNF-02│ Mensajes español   │ Usabilidad │ Alta      │
│  RNF-03│ Tiempo carga <2s   │ Performance│ Media     │
│  RNF-04│ HTTPS              │ Seguridad  │ Alta      │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## 🔗 INTEGRACIÓN DE COMPONENTES

### Flujo de Datos Completo

```
[USUARIO]
   │
   ├─→ Registra Proyecto
   │        │
   │        ├─→ Validación Pydantic
   │        ├─→ Guardar en proyectos_sgr.json
   │        └─→ Streamlit actualiza tabla dinámicamente
   │
   └─→ Inicia Pipeline
            │
            ├─→ Sube Audio
            │        │
            │        ├─→ [WHISPER]
            │        │   ├─ Preprocesamiento
            │        │   ├─ Transcripción
            │        │   └─ Output: texto + timestamps
            │        │
            │        ├─→ [LLM GENERATION]
            │        │   ├─ Construcción prompt
            │        │   ├─ Envío a Ollama/LlamaCpp
            │        │   ├─ Parsing de respuesta
            │        │   └─ Output: requisitos brutos
            │        │
            │        ├─→ [EARS VALIDATION]
            │        │   ├─ Clasificación categórica
            │        │   ├─ Validación sintáctica
            │        │   └─ Output: requisitos validados + flags
            │        │
            │        └─→ [ENSAMBLADO SRS]
            │            ├─ Compilación IEEE 830
            │            ├─ Generación documento
            │            └─ Output: SRS en múltiples formatos
            │
            └─→ Streamlit muestra resultados
                 ├─ Fichas de RF
                 ├─ Tabla de RNF
                 ├─ Estados de validación
                 └─ Botón de descarga
```

### Diagrama de Dependencias

```
proyectos_sgr.json
        ↑
        │
   Pydantic Validation ←─── Proyecto
        │                        │
        └─→ Streamlit UI         │
                │                │
                └─→ [Pipeline Start]
                        │
                        ├─→ Audio File
                        │        │
                        │        ├─→ WHISPER
                        │        │    ├─ librosa (procesamiento)
                        │        │    └─ torch (inferencia)
                        │        │
                        │        ├─→ LLM (Ollama API)
                        │        │    └─ HTTP requests
                        │        │
                        │        ├─→ EARS Validator
                        │        │    ├─ regex patterns
                        │        │    └─ category classifier
                        │        │
                        └─→ Documento IEEE 830
                             └─→ Descarga JSON/Markdown
```

---

## 🧠 PIPELINE DE IA DETALLADO

### Fase 1: Entrada y Contexto

```
[PROYECTO]
{
  "nombre": "Sistema de Carrito de Compras",
  "objetivo": "Permitir a usuarios gestionar productos para comprar",
  "dominio": "E-commerce"
}

[AUDIO GRABADO]
- Transcripción preparada (5-20 minutos de entrevista)
- Español hablado naturalmente
- Incluye cambios de tema, interjecciones, pausas

Ej: "Eh, bueno, el cliente necesita poder ver... 
     ah sí, y también agregar productos, ¿verdad? 
     Y cuando finaliza la compra... debe haber confirmación"
```

### Fase 2: Procesamiento de Transcripción

```
ENTRADA CRUDA:
"Eh, bueno, el cliente necesita poder ver el carrito, 
 ah sí, y también agregar productos, ¿verdad? 
 Y cuando finaliza la compra debe haber confirmación"

↓ LIMPIEZA INTELIGENTE (LLM local realiza)

SALIDA PROCESADA:
"El cliente necesita poder ver el carrito de compras. 
 También debe poder agregar productos. 
 Cuando finaliza la compra debe haber confirmación."
```

### Fase 3: Construcción del Prompt del Sistema

```
PROMPT ENVIADO AL LLM:

═══════════════════════════════════════════════════════════════

Eres un ingeniero de requisitos de software experto especializado 
en la norma IEEE 830-1998 y la sintaxis EARS (Easy Approach to 
Requirements Syntax).

Tu tarea es analizar la siguiente información de proyecto y 
transcripción de entrevista, y generar un documento completo de 
Especificación de Requisitos de Software (ERS).

CONTEXTO DEL PROYECTO:
- Nombre: Sistema de Carrito de Compras
- Objetivo: Permitir a usuarios gestionar productos para comprar
- Dominio: E-commerce

TRANSCRIPCIÓN LIMPIA DE LA ENTREVISTA:
El cliente necesita poder ver el carrito de compras. 
También debe poder agregar productos. 
Cuando finaliza la compra debe haber confirmación.

INSTRUCCIONES:

1. REQUISITOS FUNCIONALES (RF)
   Formato: RF-XX: Nombre del Requisito
   Cada uno DEBE cumplir EXACTAMENTE una categoría EARS
   
   Categorías EARS:
   
   a) UBICUO - Patrón: <entidad> SHALL <acción>
      Ejemplo: "El sistema SHALL mostrar el carrito actualizado"
      Usa cuando: Es una capacidad base sin condiciones
   
   b) DISPARADO - Patrón: WHEN <trigger> THEN <entidad> SHALL <respuesta>
      Ejemplo: "WHEN el usuario hace clic THEN el sistema SHALL validar"
      Usa cuando: Una acción dispara un comportamiento
   
   c) ESTADO - Patrón: WHILE <condición> <entidad> SHALL <acción>
      Ejemplo: "WHILE la sesión activa el sistema SHALL mantener carrito"
      Usa cuando: Comportamiento mientras existe una condición
   
   d) OPCIONAL - Patrón: WHERE <característica> <entidad> SHALL <acción>
      Ejemplo: "WHERE el pago sea por tarjeta el sistema SHALL validar"
      Usa cuando: El requisito es condicional a una característica
   
   e) DESEADO - Patrón: <entidad> SHOULD <acción>
      Ejemplo: "El sistema SHOULD enviar notificación"
      Usa cuando: Es recomendado pero NO mandatorio

2. REQUISITOS NO FUNCIONALES (RNF)
   Formato: RNF-XX: [Categoría] Descripción
   Categorías: Usabilidad, Performance, Seguridad, 
               Confiabilidad, Mantenibilidad
   
   Ejemplos:
   - "RNF-01: [Usabilidad] Interfaz intuitiva sin capacitación"
   - "RNF-02: [Performance] Tiempo de carga <2 segundos"

3. SALIDA ESPERADA EN FORMATO JSON:

{
  "proyecto": "Sistema de Carrito de Compras",
  "fecha_generacion": "2026-06-19",
  "requisitos_funcionales": [
    {
      "id": "RF-01",
      "nombre": "Visualizar Carrito",
      "categoria_ears": "Ubicuo",
      "descripcion": "El sistema SHALL mostrar un listado...",
      "prioridad": "Alta"
    },
    ...
  ],
  "requisitos_no_funcionales": [
    {
      "id": "RNF-01",
      "categoria": "Usabilidad",
      "descripcion": "Interfaz intuitiva..."
    },
    ...
  ]
}

4. RESTRICCIONES:
   ✓ Cada requisito debe ser independiente y autoexplicativo
   ✓ NO usar pronombres ambiguos (eso, esto, aquello)
   ✓ Verbos en infinitivo activo (mostrar, validar, registrar)
   ✓ Sin negaciones dobles o confusas
   ✓ Mínimo 10 RF, máximo 20 RF
   ✓ Mínimo 5 RNF, máximo 15 RNF

GENERA LOS REQUISITOS AHORA:

═══════════════════════════════════════════════════════════════
```

### Fase 4: Respuesta del LLM

```
SALIDA DEL MODELO (respuesta generada):

{
  "proyecto": "Sistema de Carrito de Compras",
  "fecha_generacion": "2026-06-19",
  "requisitos_funcionales": [
    {
      "id": "RF-01",
      "nombre": "Visualizar Carrito",
      "categoria_ears": "Ubicuo",
      "descripcion": "El sistema SHALL mostrar en tiempo real todos 
                      los productos agregados al carrito con cantidad, 
                      precio unitario y subtotal.",
      "prioridad": "Alta"
    },
    {
      "id": "RF-02",
      "nombre": "Agregar Producto al Carrito",
      "categoria_ears": "Event-Driven",
      "descripcion": "WHEN el usuario hace clic en el botón 'Agregar 
                      al carrito' THEN el sistema SHALL validar 
                      disponibilidad de inventario y añadir el producto 
                      a la sesión activa del usuario.",
      "prioridad": "Alta"
    },
    {
      "id": "RF-03",
      "nombre": "Confirmar Compra",
      "categoria_ears": "Event-Driven",
      "descripcion": "WHEN el usuario hace clic en 'Finalizar compra' 
                      THEN el sistema SHALL mostrar un diálogo de 
                      confirmación con resumen de carrito, total a pagar, 
                      y opciones de pago.",
      "prioridad": "Alta"
    },
    ...
  ],
  "requisitos_no_funcionales": [
    {
      "id": "RNF-01",
      "categoria": "Usabilidad",
      "descripcion": "La interfaz SHALL ser intuitiva permitiendo 
                      agregar productos con máximo 2 clics"
    },
    {
      "id": "RNF-02",
      "categoria": "Performance",
      "descripcion": "El sistema SHALL cargar el carrito y mostrar 
                      todos los productos en menos de 2 segundos"
    },
    ...
  ]
}
```

### Fase 5: Validación EARS

```
VALIDADOR EARS PROCESA CADA REQUISITO:

RF-01: "El sistema SHALL mostrar en tiempo real..."
├─ Detecta: ¿WHEN? No | ¿WHILE? No | ¿WHERE? No | ¿SHOULD? No
├─ Categoría detectada: UBICUO ✓
├─ Verificación: Patrón <entidad> SHALL <acción>?
│  ├─ Entidad: "El sistema" ✓
│  ├─ Verbo auxiliar: "SHALL" ✓
│  └─ Acción: "mostrar" (infinitivo) ✓
├─ Validación: ✅ CORRECTO
└─ Salida: {"id": "RF-01", "estado": "válido", "categoría": "Ubicuo"}

RF-02: "WHEN el usuario hace clic... THEN el sistema SHALL..."
├─ Detecta: ¿WHEN? Sí | ¿THEN/SHALL? Sí
├─ Categoría detectada: EVENT-DRIVEN ✓
├─ Verificación: Patrón WHEN <trigger> THEN <entity> SHALL <respuesta>?
│  ├─ Trigger: "el usuario hace clic" ✓
│  ├─ Verbo auxiliar: "SHALL" ✓
│  └─ Respuesta: "validar disponibilidad y añadir" ✓
├─ Validación: ✅ CORRECTO
└─ Salida: {"id": "RF-02", "estado": "válido", "categoría": "Event-Driven"}

RF-03: "El sistema podría mostrar..." (PROBLEMA)
├─ Detecta: ¿CUANDO? No | ¿WHILE? No | ¿WHERE? No | ¿SHOULD? No
├─ Palabras clave: "podría" (modal condicional)
├─ Categoría candidata: ??? (NO ENCAJA EN NINGUNA EARS)
├─ Análisis: "podría" no es SHALL/SHOULD/WHEN/WHILE/WHERE
├─ Validación: ❌ INVÁLIDO
└─ Error: "La palabra 'podría' es ambigua. 
           Usa SHALL para mandatorio o SHOULD para recomendado.
           Ejemplo correcto: 'El sistema SHALL mostrar...'"

SALIDA VALIDACIÓN GLOBAL:
- RF-01: ✅ Válido
- RF-02: ✅ Válido
- RF-03: ❌ Inválido (CORRECCIÓN NECESARIA)
- RNF-01: ✅ Válido
- RNF-02: ✅ Válido

Requisitos aprobados: 4/5 (80%)
```

### Fase 6: Generación de Documento IEEE 830

```
ESTRUCTURA DEL DOCUMENTO ENSAMBLADO:

═══════════════════════════════════════════════════════════════
ESPECIFICACIÓN DE REQUISITOS DE SOFTWARE (ERS)
IEEE 830-1998
═══════════════════════════════════════════════════════════════

1. INTRODUCCIÓN
   1.1 Propósito
       Especificar los requisitos funcionales y no funcionales del
       Sistema de Carrito de Compras...
   
   1.2 Ámbito
       El presente documento especifica la funcionalidad de un
       módulo de carrito de compras...
   
   1.3 Definiciones y acrónimos
       - RF: Requisito Funcional
       - RNF: Requisito No Funcional
       - EARS: Easy Approach to Requirements Syntax

2. REQUISITOS GENERALES DEL SISTEMA
   2.1 Interfaces de usuario
       - Interfaz web responsive
       - Acceso desde navegadores modernos
   
   2.2 Interfaces de hardware
       - Conexión a internet
   
   2.3 Interfaces de software
       - Integración con API de inventario
       - Integración con sistema de pagos

3. REQUISITOS FUNCIONALES ESPECÍFICOS

   3.1 RF-01: Visualizar Carrito
   ID: RF-01
   Nombre: Visualizar Carrito
   Prioridad: Alta
   Estado de Validación EARS: ✅ Válido (Ubicuo)
   
   Descripción:
   El sistema SHALL mostrar en tiempo real todos los productos
   agregados al carrito con cantidad, precio unitario y subtotal.
   
   ───────────────────────────────────────────────────────────

   3.2 RF-02: Agregar Producto al Carrito
   ID: RF-02
   Nombre: Agregar Producto al Carrito
   Prioridad: Alta
   Estado de Validación EARS: ✅ Válido (Event-Driven)
   
   Descripción:
   WHEN el usuario hace clic en el botón 'Agregar al carrito'
   THEN el sistema SHALL validar disponibilidad de inventario
   y añadir el producto a la sesión activa del usuario.
   
   ───────────────────────────────────────────────────────────

4. REQUISITOS NO FUNCIONALES ESPECÍFICOS

   4.1 RNF-01: Usabilidad
   Descripción: La interfaz SHALL ser intuitiva permitiendo
   agregar productos con máximo 2 clics.
   
   4.2 RNF-02: Performance
   Descripción: El sistema SHALL cargar el carrito y mostrar
   todos los productos en menos de 2 segundos.

5. APÉNDICES
   A. Matriz de Trazabilidad
   B. Análisis de Validación EARS
   C. Diccionario de Datos

═══════════════════════════════════════════════════════════════
```

---

## 📊 FLUJOS DE DATOS

### Flujo 1: Persistencia y Recuperación de Proyectos

```
ESCRITURA (Guardar Proyecto):
┌────────────────┐
│ Usuario        │
│ Ingresa datos  │
└────────────────┘
        ↓
┌────────────────────────────┐
│ Pydantic valida            │
│ (min_length=1 en todos)    │
└────────────────────────────┘
        ↓ ✓ Válido
┌────────────────────────────┐
│ Python abre proyectos_sgr  │
│ .json en modo lectura      │
└────────────────────────────┘
        ↓
┌────────────────────────────┐
│ Lee JSON existente         │
│ (ó inicia array vacío)     │
└────────────────────────────┘
        ↓
┌────────────────────────────┐
│ Añade nuevo proyecto       │
│ con timestamp y UUID       │
└────────────────────────────┘
        ↓
┌────────────────────────────┐
│ Escribe archivo JSON con   │
│ codificación UTF-8         │
└────────────────────────────┘
        ↓
┌────────────────────────────┐
│ Streamlit recarga estado   │
│ y actualiza tabla UI       │
└────────────────────────────┘


LECTURA (Cargar Proyectos):
┌────────────────────────────┐
│ Streamlit inicia app       │
└────────────────────────────┘
        ↓
┌────────────────────────────┐
│ Busca proyectos_sgr.json   │
│ en directorio raíz         │
└────────────────────────────┘
        ↓
┌────────────────────────────┐
│ Lee y parsea JSON          │
│ (error si no existe)       │
└────────────────────────────┘
        ↓
┌────────────────────────────┐
│ Valida estructura con      │
│ Pydantic                   │
└────────────────────────────┘
        ↓ ✓ Válido
┌────────────────────────────┐
│ Guarda en session_state    │
│ de Streamlit               │
└────────────────────────────┘
        ↓
┌────────────────────────────┐
│ Renderiza tabla con datos  │
│ en UI                      │
└────────────────────────────┘
```

### Flujo 2: Transcripción de Audio

```
USUARIO CARGA AUDIO:
┌──────────────────────────────┐
│ Streamlit: archivo.wav       │
│ (bytes en memoria)           │
└──────────────────────────────┘
        ↓
┌──────────────────────────────┐
│ Librosa (librería Python)    │
│ Lee y carga audio en RAM     │
└──────────────────────────────┘
        ↓
┌──────────────────────────────┐
│ Preprocesamiento:            │
│ 1. Detecta sample_rate orig  │
│ 2. Resamplea a 16kHz         │
│ 3. Convierte a mono          │
│ 4. Normaliza volumen         │
└──────────────────────────────┘
        ↓
┌──────────────────────────────┐
│ WHISPER API Local            │
│ (ejecuta en GPU/CPU local)   │
│                              │
│ Encoder:                     │
│ - Audio dividido en frames   │
│ - Cada frame → embedding     │
│ - Contexto acumulado         │
│                              │
│ Decoder:                     │
│ - Genera tokens predichos    │
│ - Decodifica a español       │
└──────────────────────────────┘
        ↓
┌──────────────────────────────┐
│ Output JSON:                 │
│ {                            │
│  "text": "transcripción...", │
│  "segments": [               │
│    {                         │
│     "id": 0,                 │
│     "start": 0.0,            │
│     "end": 5.2,              │
│     "text": "..."            │
│    }                         │
│  ]                           │
│ }                            │
└──────────────────────────────┘
        ↓
┌──────────────────────────────┐
│ Streamlit muestra en UI:     │
│ "Transcripción completada"   │
│ + primeros 500 caracteres    │
└──────────────────────────────┘
```

### Flujo 3: Llamada al LLM

```
DATOS PREPARADOS:
┌────────────────────────────────────┐
│ Prompt construcción:               │
│ - System prompt (instrucciones)    │
│ - Contexto proyecto               │
│ - Transcripción limpia            │
└────────────────────────────────────┘
        ↓
┌────────────────────────────────────┐
│ HTTP Request Preparation:          │
│ POST http://localhost:11434/...    │
│                                    │
│ Body JSON:                         │
│ {                                  │
│   "model": "mistral:latest",       │
│   "prompt": "[PROMPT COMPLETO]",   │
│   "stream": false,                 │
│   "temperature": 0.7,              │
│   "top_p": 0.9,                    │
│   "timeout": 60000                 │
│ }                                  │
└────────────────────────────────────┘
        ↓
┌────────────────────────────────────┐
│ LLM Inferencia (30-120 segundos):  │
│                                    │
│ GPU/CPU procesa:                   │
│ 1. Tokeniza prompt (5000+ tokens)  │
│ 2. Forward pass por red neuronal   │
│ 3. Sampling de siguiente token     │
│ 4. Repeat hasta finalizar          │
│ 5. De-tokeniza a strings           │
└────────────────────────────────────┘
        ↓
┌────────────────────────────────────┐
│ Response JSON:                     │
│ {                                  │
│  "model": "mistral:latest",        │
│  "created_at": "...",              │
│  "response": "[requisitos JSON]",  │
│  "done": true,                     │
│  "context": [...]                  │
│ }                                  │
└────────────────────────────────────┘
        ↓
┌────────────────────────────────────┐
│ Parsing Response:                  │
│ - Extrae campo "response"          │
│ - Limpia markdown si existe        │
│ - Valida JSON                      │
│ - Convierte a Python dict          │
└────────────────────────────────────┘
        ↓
┌────────────────────────────────────┐
│ Estructura validada:               │
│ {                                  │
│   "requisitos_funcionales": [...], │
│   "requisitos_no_funcionales": []  │
│ }                                  │
└────────────────────────────────────┘
```

### Flujo 4: Validación EARS

```
ENTRADA: Requisito Sin Validar
┌─────────────────────────────────────────┐
│ "El sistema SHALL proporcionar un       │
│  formulario de registro de proyectos"   │
└─────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────┐
│ ANÁLISIS LÉXICO:                        │
│ - Búsqueda palabras clave               │
│ - ¿WHEN? → No encontrado                │
│ - ¿WHILE? → No encontrado               │
│ - ¿WHERE? → No encontrado               │
│ - ¿SHOULD? → No encontrado              │
│ - ¿SHALL? → ENCONTRADO                  │
└─────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────┐
│ CLASIFICACIÓN PRELIMINAR:               │
│ Candidato: UBICUO                       │
│ (contiene SHALL sin WHEN/WHILE/WHERE)   │
└─────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────┐
│ VALIDACIÓN PATRÓN UBICUO:               │
│ Patrón esperado: <entity> SHALL <action>│
│                                         │
│ Análisis del requisito:                 │
│ "El sistema" = <entity> ✓              │
│ "SHALL" = verbo auxiliar ✓              │
│ "proporcionar un formulario..." =       │
│   <action> ✓                            │
│                                         │
│ Verificaciones adicionales:             │
│ - ¿Sin condicionales? ✓                 │
│ - ¿Verbo principal infinitivo? ✓        │
│ - ¿Sujeto claro? ✓                      │
└─────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────┐
│ RESULTADO VALIDACIÓN:                   │
│ ✅ VÁLIDO                               │
│ Categoría: UBICUO                       │
│ Errores: ninguno                        │
│ Advertencias: ninguna                   │
│ Confianza: 100%                         │
└─────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────┐
│ SALIDA VALIDADOR:                       │
│ {                                       │
│   "id": "RF-01",                        │
│   "categoria_ears": "Ubicuo",           │
│   "estado": "válido",                   │
│   "errores": [],                        │
│   "confianza": 1.0                      │
│ }                                       │
└─────────────────────────────────────────┘
```

---

## 🎬 RESUMEN EJECUTIVO

El **SGR es un sistema de dos caras**:

### 👤 Vista del Usuario (Por Encima)
- Interfaz limpia en Streamlit
- Registro de proyectos con un formulario
- Sube audio de entrevista
- Presiona "Iniciar Pipeline"
- Ve requisitos generados automáticamente
- Descarga documento IEEE 830

### ⚙️ Vista Técnica (Por Debajo)
1. **Whisper** transcribe audio → texto
2. **LLM Local** genera requisitos a partir del contexto
3. **EARS Validator** verifica cada requisito es gramaticalmente correcto
4. **Orquestador** coordina todo y maneja errores
5. **Persistencia JSON** guarda el estado

### 🔄 El Flujo
```
Proyecto → Audio → Transcripción → LLM → Validación → SRS
  (UI)    (Audio) (Whisper)   (LLM)  (EARS)    (Documento)
```

Todo ocurre **localmente** - sin conexión a internet, sin costos de API, con privacidad garantizada.

---

**Documento generado**: 19/06/2026  
**Versión**: 1.0  
**Sistema**: SGR - Sistema de Generación de Requisitos
