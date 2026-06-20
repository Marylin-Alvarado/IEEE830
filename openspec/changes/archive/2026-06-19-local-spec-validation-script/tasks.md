## 1. Estructura del Script

- [x] 1.1 Crear el directorio `scripts/` en la raíz del proyecto
- [x] 1.2 Crear `scripts/validate_specs.py` con shebang y docstring de uso

## 2. Validación de Metadatos

- [x] 2.1 Implementar función `check_metadata(filepath)` que busque las líneas `status:`, `version:` y `authors:` mediante regex
- [x] 2.2 Implementar función `check_sections(filepath)` que verifique presencia de `## Purpose` y `## Requirements`

## 3. Reporte y Salida

- [x] 3.1 Implementar bucle principal que itere sobre todos los `.md` en `openspec/specs/` y acumule resultados PASS/FAIL
- [x] 3.2 Implementar resumen final con contadores y exit code 0 si todo pasa, 1 si hay fallos
