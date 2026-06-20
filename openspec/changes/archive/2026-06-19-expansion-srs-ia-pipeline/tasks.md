## 1. Expand Section 1 (Introducción) — AI-Assisted Elicitation Scope

- [x] 1.1 Update 1.1 Propósito to include AI-assisted requirements engineering scope and thesis research objectives
- [x] 1.2 Expand 1.2 Ámbito del producto with the full AI pipeline: audio transcription (Whisper), LLM-based requirement generation, EARS grammar validation
- [x] 1.3 Add new definitions to 1.3 Definiciones y siglas: Whisper, LLM, EARS grammar validator, prompt engineering, pipeline orchestration, inference endpoint
- [x] 1.4 Add references to 1.4 Referencias: Whisper paper (Radford et al.), Ollama/LlamaCpp documentation, EARS taxonomy (Mavin et al. 2009), prompt engineering literature
- [x] 1.5 Update 1.5 Visión general del documento to describe how the new sections cover the AI pipeline

## 2. Expand Section 2 (Descripción General) — Pipeline Architecture

- [x] 2.1 Rewrite 2.1 Perspectiva del producto with multi-layer architecture diagram: Audio Input → Whisper ASR → Text Chunks → LLM Prompt → Structured Requirements → EARS Validator → Validated SRS Output
- [x] 2.2 Describe each pipeline layer with data formats, interfaces, and data flow contracts
- [x] 2.3 Expand 2.2 Funciones del producto with three new functions: transcription, LLM generation, EARS validation
- [x] 2.4 Update 2.3 Características de los usuarios to include AI pipeline user roles and interaction modes
- [x] 2.5 Add AI-specific 2.4 Restricciones: local model constraints (RAM, VRAM), model size limits, Whisper model variants (tiny, base, small, medium, large), inference latency expectations
- [x] 2.6 Update 2.5 Suposiciones y dependencias with Ollama/LlamaCpp runtime, Whisper Python package, GPU availability assumptions

## 3. Expand Section 3 (Requisitos Específicos) — EARS Grammar & AI Pipeline Requirements

- [x] 3.1 Add 3.1.x subsection for EARS Ubiquitous requirements: formal syntax (`<entity> SHALL <action>`), classification algorithm, valid/invalid examples, validation logic
- [x] 3.2 Add 3.1.x subsection for EARS Event-Driven requirements: formal syntax (`WHEN <trigger> THEN <entity> SHALL <response>`), trigger-response pattern matching, valid/invalid examples
- [x] 3.3 Add 3.1.x subsection for EARS State-Driven requirements: formal syntax (`WHILE <state> <entity> SHALL <action>`), continuous state detection, valid/invalid examples
- [x] 3.4 Add 3.1.x subsection for EARS Optional requirements: formal syntax (`WHERE <feature> <entity> SHALL <action>`), conditional feature detection, valid/invalid examples
- [x] 3.5 Add 3.1.x subsection for EARS Desired requirements: formal syntax (`<entity> SHOULD <action>`), non-mandatory flagging, SHOULD vs SHALL distinction, valid/invalid examples
- [x] 3.6 Add 3.1.x subsection for Audio Transcription requirements: file format support, Whisper model configuration, preprocessing pipeline, multilingual support, timestamp generation
- [x] 3.7 Add 3.1.x subsection for LLM Requirement Generation requirements: prompt construction, IEEE 830 system prompt, Ollama/LlamaCpp integration, structured output parsing
- [x] 3.8 Add 3.1.x subsection for EARS Grammar Validation requirements: multi-category classification, strict syntax rules per category, rejection with error messages, correction suggestions
- [x] 3.9 Add 3.1.x subsection for Pipeline Orchestration requirements: stage sequencing, progress visibility, error handling per stage, retry logic, configuration management

## 4. Add Non-Functional Requirements for AI Pipeline

- [x] 4.1 Add usability requirements: pipeline status visibility, configuration UI, transcript preview, validation reports
- [x] 4.2 Add performance requirements: LLM inference latency (<30s per generation), transcription time vs audio length ratio, grammar validation throughput
- [x] 4.3 Add reliability requirements: Whisper model fallback, LLM connection retry, pipeline checkpoint/restart
- [x] 4.4 Add accuracy requirements: transcription WER target (<10%), EARS classification accuracy target (>95%), LLM requirement structure compliance
- [x] 4.5 Add hardware requirements: minimum RAM (8GB), GPU recommendation, disk space for models

## 5. Add External Interfaces for AI Components

- [x] 5.1 Document 3.3.x Ollama REST API interface: endpoint URL, request/response format, model configuration parameters
- [x] 5.2 Document 3.3.x LlamaCpp server interface: endpoint URL, completion parameters, context window configuration
- [x] 5.3 Document 3.3.x Whisper model interface: supported model sizes, input audio format requirements, output format (text with segments/timestamps)
- [x] 5.4 Document 3.3.x Pipeline data format: intermediate data structures between stages (transcript chunks, structured requirements, validation results)

## 6. Final Review & Verification

- [x] 6.1 Verify all EARS categories have formal syntax definitions with valid/invalid examples
- [x] 6.2 Verify all AI pipeline components have corresponding non-functional requirements
- [x] 6.3 Verify all new requirements trace to capability specs in `openspec/specs/`
- [x] 6.4 Verify document consistency: terminology, cross-references, section numbering
- [x] 6.5 Final proofread of expanded `requisitos.md` for technical accuracy and completeness
