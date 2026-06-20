## Why

The current SRS document (`requisitos.md`) documents the SGR project registration system but does not cover the AI-assisted requirements engineering pipeline — local LLM models for requirement generation, Whisper for audio-to-text transcription of stakeholder interviews, and a formal EARS grammar validation engine. For the thesis, the SRS must be expanded to specify these advanced capabilities in full IEEE 830 detail, establishing the technical foundation for an AI-augmented requirements workflow.

## What Changes

- Expand `requisitos.md` with a complete IEEE 830 Section 1 (Introducción) covering AI-assisted requirements elicitation scope
- Expand Section 2 (Descripción General) with the full pipeline architecture: local LLM orchestration, Whisper transcription layer, and EARS validation engine
- Expand Section 3 (Requisitos Específicos) with detailed functional requirements for EARS syntax rules (Ubiquitous, Event-driven, State-driven, Optional, Desired) and strict grammar validation
- Add new non-functional requirements for model latency, transcription accuracy, and grammar validation coverage
- Document external interfaces for LLM inference APIs (LlamaCpp, Ollama) and Whisper model integration

## Capabilities

### New Capabilities
- `ai-requirement-generation`: Local LLM-based generation of IEEE 830 requirements from project descriptions
- `audio-transcription`: Whisper-based transcription of audio interviews to text for requirement elicitation
- `ears-grammar-validation`: Formal validation engine for EARS syntax rules (ubiquitous, event-driven, state-driven, optional, desired)
- `ai-pipeline-orchestration`: Pipeline orchestrator that coordinates LLM, Whisper, and EARS validation into a unified workflow

### Modified Capabilities
- `ieee830-srs`: Expanded to cover AI-assisted elicitation, EARS grammar rules, and LLM/Whisper pipeline architecture in all three IEEE 830 sections

## Impact

- **Expanded file**: `requisitos.md` — all three IEEE 830 sections will be rewritten with deep technical content
- **New spec files**: `openspec/specs/` — four new capability specs for AI/Whisper/EARS/pipeline
- **No code changes**: This change is documentation-only; implementation will follow in a separate change
