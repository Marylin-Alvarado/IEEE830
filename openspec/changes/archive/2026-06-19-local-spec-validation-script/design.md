## Context

There are 15 spec files under `openspec/specs/`. Each follows the same structure (## Purpose → ## Requirements → ### Requirement → #### Scenario). The CI workflow validates syntax but a local script gives faster feedback without pushing to GitHub. No pre-validation script currently exists.

## Goals / Non-Goals

**Goals:**
- Create `scripts/validate_specs.py` that scans all `.md` files under `openspec/specs/`
- Validate metadata header contains `status`, `version`, `authors` (any format — YAML front matter, inline, etc.)
- Validate critical sections `## Purpose` and `## Requirements` are present
- Print PASS/FAIL per file with summary and exit code 0/1

**Non-Goals:**
- No modifications to spec files themselves
- No EARS grammar or scenario validation (handled by CI)
- No recursive subdirectory scanning beyond `openspec/specs/`

## Decisions

- **Pure Python stdlib**: No external dependencies — uses `os`, `glob`, `re`, `sys`. Ensures the script works in any Python 3.11 environment without pip install.
- **Line-by-line scan**: Rather than YAML parsing (which would require `pyyaml`), search for `status:`, `version:`, `authors:` patterns via regex. Robust enough for this project's metadata conventions.
- **Section check by `##` heading**: Uses regex `^## (Purpose|Requirements)` to detect critical sections. Case-sensitive to match the project convention.
- **Output format**: Single-line PASS/FAIL per file with a ⚠️ prefix on failures, followed by a summary table.
- **Exit code**: 0 = all pass, 1 = any failure. Compatible with CI or pre-commit hooks.

## Risks / Trade-offs

- **False negative on metadata**: If a spec uses a non-standard metadata format, the regex might miss it. Mitigation: keep regex flexible with optional whitespace and colon variants.
- **Script not run automatically**: No git hook integration yet. Mitigation: document manual usage in script docstring.
