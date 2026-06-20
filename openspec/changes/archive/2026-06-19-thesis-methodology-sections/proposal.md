## Why

The current `requisitos.md` is structured as a technical IEEE 830 SRS document but lacks the academic thesis framing required for the deliverable. It jumps directly into technical specification without establishing the research problem, justification for using LLMs and Whisper as a scientific solution, or the thesis objectives. Adding Problemática, Justificación, and Objetivos sections transforms the document into a complete academic-technical artifact suitable for thesis submission while preserving all existing IEEE 830 and EARS content.

## What Changes

- Insert new Section 1.1 (Problemática) before the existing 1.1 Propósito, detailing ambiguity in traditional requirements elicitation, information loss in meetings, and lack of formal structure in software specification
- Insert new Section 1.2 (Justificación) establishing LLMs and Whisper transcription as the scientific solution to the identified problems
- Insert new Section 1.3 (Objetivos) with general and specific objectives oriented to the SGR system
- Renumber existing sections 1.1-1.5 to 1.4-1.8 accordingly (Propósito, Ámbito del producto, Definiciones y siglas, Referencias, Visión general del documento)
- Preserve all existing Section 2 (Descripción General) and Section 3 (Requisitos Específicos) content unchanged

## Capabilities

### New Capabilities
- `thesis-methodology`: Thesis methodology framing — Problemática, Justificación, and Objetivos sections for the academic deliverable

### Modified Capabilities
- `ieee830-srs`: The SRS document structure requirements change — the Introduction section (Section 1) gains three new required subsections (Problemática, Justificación, Objetivos) and existing subsection numbering shifts

## Impact

- **Modified file**: `requisitos.md` — three new subsections inserted into Section 1, existing subsections renumbered (1.1→1.4, 1.2→1.5, 1.3→1.6, 1.4→1.7, 1.5→1.8)
- **No code changes**: Documentation-only — app.py is not affected
- **No external dependencies change**
