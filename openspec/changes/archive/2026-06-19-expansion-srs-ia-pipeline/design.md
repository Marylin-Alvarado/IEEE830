## Context

The current `requisitos.md` documents the SGR v1 (project registration with Pydantic validation and JSON persistence). The thesis requires expanding this SRS to specify an AI-assisted pipeline where: (1) stakeholder interviews are transcribed via Whisper, (2) transcribed text feeds into local LLMs for structured requirement generation following IEEE 830, and (3) generated requirements are validated against EARS grammar rules. This is a documentation-only change that produces a comprehensive IEEE 830 SRS covering the entire AI pipeline architecture.

## Goals / Non-Goals

**Goals:**
- Expand Section 1 (Introducción) to include AI-assisted elicitation scope, updated definitions (LLM, Whisper, EARS grammar, prompt engineering), and references
- Expand Section 2 (Descripción General) with pipeline architecture diagram, LLM orchestration layer, Whisper integration, and EARS validation engine
- Expand Section 3 (Requisitos Específicos) with detailed EARS syntax rules for each category, strict grammar validation requirements, and AI pipeline functional requirements
- Add pipeline-specific non-functional requirements (inference latency, transcription WER, grammar coverage)
- Add external interfaces for local LLM APIs (Ollama, LlamaCpp), Whisper model bindings, and pipeline data flow

**Non-Goals:**
- Code implementation of the AI pipeline (separate change)
- Model training or fine-tuning
- Cloud/hosted LLM services (local-only scope)

## Decisions

1. **IEEE 830-1998 as the document backbone** — The existing `requisitos.md` follows IEEE 830. The expansion preserves this structure and adds depth within each section rather than restructuring.

2. **EARS formal grammar definitions in Section 3** — Each EARS category (ubiquitous, event-driven, state-driven, optional, desired) gets its own subsection with formal syntax rules, valid/invalid examples, and validation logic specifications. This is the most technically demanding section and must be exhaustive.

3. **Pipeline architecture in Section 2** — A multi-layer diagram shows: Audio Input → Whisper ASR → Text Chunks → LLM Prompt → Structured Requirements → EARS Validator → Validated SRS Output. Each layer is described with data formats and interfaces.

4. **Local-first design** — All AI components (LLM, Whisper) run locally on the user's machine. This avoids API costs, keeps data private, and aligns with the thesis scope. Ollama and LlamaCpp are referenced as compatible inference backends.

## Risks / Trade-offs

- **Document size growth** — The expanded SRS may exceed 100 pages. Acceptable for a thesis deliverable where completeness is valued over conciseness.
- **Technology dependency** — Referencing specific tools (Ollama, Whisper) may date the document. Mitigated by specifying capabilities abstractly and listing tools as examples.
- **No implementation validation** — Requirements are written before code exists. Some may be refined during implementation. The document notes this as expected per IEEE 830 iterative nature.
