## 1. Environment Documentation

- [x] 1.1 Crear `environment.md` con sección "Python Runtime" especificando Python 3.11 y gestor de paquetes pip
- [x] 1.2 Agregar sección "Environment Variables" en `environment.md` con variables para Ollama (`OLLAMA_HOST`), LlamaCpp (`LLAMACPP_HOST`, `LLAMACPP_MODEL`), Whisper (`WHISPER_MODEL_SIZE`, `WHISPER_DEVICE`)
- [x] 1.3 Agregar sección "Project Structure" en `environment.md` con el árbol de carpetas del proyecto y descripciones

## 2. Dependency Manifest

- [x] 2.1 Crear `requirements.txt` con streamlit versión 1.28.1+ y pydantic versión 2.5.0+
- [x] 2.2 Agregar openai>=1.6.0 y requests>=2.31.0 a `requirements.txt` para comunicaciones con modelos IA locales
- [x] 2.3 Verificar que `pip install -r requirements.txt` se ejecuta sin errores
