## 1. Esquema del Proyecto

- [x] 1.1 Crear el directorio `schemas/` en la raíz del proyecto
- [x] 1.2 Definir en `project_schema.json` el objeto raíz `project` con propiedades: `nombre_proyecto` (string, minLength 1), `objetivo_general` (string), `descripcion_dominio` (string), `fecha_registro` (string, pattern fecha ISO)
- [x] 1.3 Definir el arreglo `requisitos` en el esquema con objetos que contengan `codigo` (pattern `^RF-\d{2}$`), `descripcion` (string), `sintaxis_ears` (objeto anidado), `tipo_ieee830` (enum)

## 2. Validación EARS y Gobernanza

- [x] 2.1 Definir `sintaxis_ears` como objeto con `when` (boolean, const: true) y `the_system_shall` (boolean, const: true)
- [x] 2.2 Definir `tipo_ieee830` como enum con valores: `functional`, `non-functional`, `interface`, `business_rule`
- [x] 2.3 Establecer `additionalProperties: false` en todos los objetos para cumplir con la gobernanza estricta de datos
