## 1. Helper Function for Parsing

- [x] 1.1 Create helper function `parse_descripcion_ears(raw: str) -> tuple[str, str]` that splits the field into (categoria, sintaxis) using `\n` separation and prefix stripping

## 2. Replace Rendering Loop

- [x] 2.1 Rewrite the `for req in lista_requisitos_funcionales:` loop to build a Markdown table string with columns | Campo | Detalle |
- [x] 2.2 Ensure Categoría and Sintaxis EARS are separate rows (parsed from `descripcion_ears`)
- [x] 2.3 Verify all 12 RF cards render correctly as tables separated by `---` dividers
