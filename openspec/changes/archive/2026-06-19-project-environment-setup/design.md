## Context

The SGR system relies on multiple local AI models (Ollama, LlamaCpp, Whisper) that require specific environment configuration. Currently there is no `environment.md` or `requirements.txt`, making it impossible to reproduce the development environment from scratch. The thesis guide requires explicit reproducibility documentation.

## Goals / Non-Goals

**Goals:**
- Create `environment.md` with Python 3.11, env vars for Ollama/LlamaCpp/Whisper, and folder structure
- Create `requirements.txt` with pinned versions of streamlit, pydantic, openai, requests

**Non-Goals:**
- No changes to `app.py` or `requisitos.md`
- No automation scripts (e.g., setup.sh/setup.ps1) — just reference documentation

## Decisions

- **environment.md format**: Plain Markdown with sections (Python Runtime, Environment Variables, Folder Structure), reflecting the repo's actual layout
- **requirements.txt version pinning**: Use `==` exact version pinning based on currently compatible versions, not `>=` ranges, to ensure deterministic installs
- **openai package**: Used for Ollama-compatible API calls (`openai` library with custom base_url pointing to `http://localhost:11434/v1`)
- **requests package**: Used for direct LlamaCpp HTTP calls (`POST /completion`)
- **No virtual environment documentation**: Left to the developer's preferred tool (venv, conda, pipenv)

## Risks / Trade-offs

- **Version drift**: Pinned versions may become outdated. Mitigation: document a periodic review cadence in `environment.md`.
- **Cross-platform paths**: Folder structure and env vars differ on Windows vs Linux. Mitigation: document both conventions in `environment.md`.
