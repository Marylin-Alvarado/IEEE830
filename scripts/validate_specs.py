#!/usr/bin/env python3
"""
validate_specs.py — Pre-validación local de especificaciones OpenSpec

Lee todos los archivos .md en openspec/specs/ y verifica:
  1. Metadatos: presencia de status, version, authors
  2. Secciones críticas: ## Purpose, ## Requirements

Uso:
    python scripts/validate_specs.py

Exit code: 0 si todo pasa, 1 si hay fallos.
"""

import glob
import os
import re
import sys

SPECS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "openspec", "specs")

METADATA_FIELDS = ["status", "version", "authors"]
CRITICAL_SECTIONS = ["Purpose", "Requirements"]


def check_metadata(filepath):
    missing = []
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    for field in METADATA_FIELDS:
        pattern = re.compile(rf"^{re.escape(field)}\s*:", re.MULTILINE)
        if not pattern.search(content):
            missing.append(field)
    return missing


def check_sections(filepath):
    missing = []
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    for section in CRITICAL_SECTIONS:
        pattern = re.compile(rf"^##\s+{re.escape(section)}\s*$", re.MULTILINE)
        if not pattern.search(content):
            missing.append(section)
    return missing


def main():
    pattern = os.path.join(SPECS_DIR, "**", "*.md")
    files = sorted(glob.glob(pattern, recursive=True))

    if not files:
        print(f"No se encontraron archivos .md en {SPECS_DIR}")
        sys.exit(1)

    passed = 0
    failed = 0
    results = []

    for filepath in files:
        relpath = os.path.relpath(filepath, SPECS_DIR)
        meta_missing = check_metadata(filepath)
        sec_missing = check_sections(filepath)

        if not meta_missing and not sec_missing:
            passed += 1
            results.append((relpath, "PASS", []))
        else:
            failed += 1
            errors = []
            for field in meta_missing:
                errors.append(f"Metadato faltante: '{field}'")
            for sec in sec_missing:
                errors.append(f"Sección faltante: '## {sec}'")
            results.append((relpath, "FAIL", errors))

    print(f"\n{'=' * 60}")
    print("  Validacion de Especificaciones OpenSpec")
    print(f"{'=' * 60}\n")

    for relpath, status, errors in results:
        if status == "PASS":
            print(f"  [PASS] {relpath}")
        else:
            print(f"  [FAIL] {relpath}")
            for err in errors:
                    print(f"      -> {err}")

    print(f"\n{'-' * 60}")
    print(f"  {len(files)} archivos validados - {passed} passed, {failed} failed")
    print(f"{'=' * 60}\n")

    sys.exit(1 if failed > 0 else 0)


if __name__ == "__main__":
    main()
