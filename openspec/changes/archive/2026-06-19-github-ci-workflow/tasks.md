## 1. Estructura del Workflow

- [x] 1.1 Crear el directorio `.github/workflows/` en la raíz del proyecto
- [x] 1.2 Crear el archivo `.github/workflows/ci.yml` con configuración básica: nombre, trigger on push y pull_request a main

## 2. Jobs y Pasos Automatizados

- [x] 2.1 Agregar job `validate` con `runs-on: ubuntu-latest`
- [x] 2.2 Agregar paso de checkout con `actions/checkout@v4`
- [x] 2.3 Agregar paso de setup Python 3.11 con `actions/setup-python@v5` y caché de pip
- [x] 2.4 Agregar paso de instalación de dependencias: `pip install -r requirements.txt`
- [x] 2.5 Agregar paso de validación OpenSpec: `npx openspec validate openspec/specs/`
