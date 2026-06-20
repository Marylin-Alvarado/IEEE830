# Entorno de Ejecución del SGR

## Python Runtime

- **Versión**: Python 3.11 o superior
- **Gestor de paquetes**: pip (incluido con Python)
- **Entorno virtual recomendado**: `python -m venv .venv`
- **Sistema operativo compatible**: Windows 10/11, Linux (Ubuntu 22.04+), macOS

### Instalación rápida

```powershell
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

```bash
# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Environment Variables

### Ollama (modelo LLM local)

| Variable | Valor por defecto | Descripción |
|----------|-------------------|-------------|
| `OLLAMA_HOST` | `http://localhost:11434` | URL base de la API REST de Ollama |
| `OLLAMA_MODEL` | `llama3.2:3b` | Nombre del modelo desplegado en Ollama |

**Ejemplo**: `$env:OLLAMA_HOST="http://localhost:11434"`

### LlamaCpp (modelo LLM local alternativo)

| Variable | Valor por defecto | Descripción |
|----------|-------------------|-------------|
| `LLAMACPP_HOST` | `http://localhost:8080` | URL base del servidor LlamaCpp |
| `LLAMACPP_MODEL` | `models/mistral-7b-instruct.gguf` | Ruta o alias del modelo GGU |

**Ejemplo**: `$env:LLAMACPP_HOST="http://localhost:8080"`

### Whisper (transcripción de audio)

| Variable | Valor por defecto | Descripción |
|----------|-------------------|-------------|
| `WHISPER_MODEL_SIZE` | `base` | Tamaño del modelo Whisper (tiny, base, small, medium, large) |
| `WHISPER_DEVICE` | `cpu` | Dispositivo de inferencia (`cpu` o `cuda` para GPU NVIDIA) |

**Ejemplo**: `$env:WHISPER_MODEL_SIZE="base"` / `$env:WHISPER_DEVICE="cpu"`

> **Nota:** Si no se definen, el sistema usará los valores por defecto indicados.

## Project Structure

```
IEEE830/
├── app.py                          # Aplicación Streamlit principal
├── requisitos.md                   # Documento ERS IEEE 830-1998 (1062 líneas)
├── requirements.txt                # Dependencias Python versionadas
├── environment.md                  # Este archivo — documentación del entorno
├── proyectos_sgr.json              # Persistencia de proyectos registrados
│
├── openspec/                       # Especificaciones y cambios OpenSpec
│   ├── config.yaml                 # Configuración del esquema spec-driven
│   ├── specs/                      # Capacidades activas (12 especificaciones)
│   │   ├── ai-pipeline-orchestration/
│   │   ├── ai-requirement-generation/
│   │   ├── audio-transcription/
│   │   ├── data-persistence/
│   │   ├── document-metadata/
│   │   ├── ears-grammar-validation/
│   │   ├── ears-validation-workflow/
│   │   ├── ieee830-srs/
│   │   ├── project-listing/
│   │   ├── project-registration/
│   │   ├── requirements-ui/
│   │   └── thesis-methodology/
│   │
│   └── changes/                    # Historial de cambios
│       ├── archive/                # Cambios archivados (6)
│       └── project-environment-setup/  # Cambio activo actual
│
├── .opencode/                      # Configuración del agente opencode
│
├── .claude/                        # Comandos y skills para Claude
├── .continue/                      # Comandos y skills para Continue
├── .cursor/                        # Comandos y skills para Cursor
├── .gemini/                        # Comandos y skills para Gemini
├── .github/                        # Prompts y skills para GitHub Copilot
├── .kilocode/                      # Skills y workflows para Kilocode
├── .kiro/                          # Prompts y skills para Kiro
└── .windsurf/                      # Skills y workflows for Windsurf
```
