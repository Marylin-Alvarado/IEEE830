## Context

The current `requisitos.md` (1007 lines) follows IEEE 830-1998 structure with three main sections: Introducción (1.1-1.5), Descripción General (2.1-2.5), and Requisitos Específicos (3.1-3.4). It contains comprehensive technical specification content — AI pipeline architecture, EARS grammar rules, non-functional requirements, and external interfaces. However, as a thesis deliverable, it lacks the academic framing sections that establish the research problem, justify the chosen technological approach, and state the thesis objectives. These sections must be inserted at the beginning of Section 1, before the existing technical content, with subsequent renumbering of existing subsections.

## Goals / Non-Goals

**Goals:**
- Insert "1.1 Problemática" detailing ambiguity in traditional requirements elicitation, information loss in stakeholder meetings, and lack of formal structure in software requirements
- Insert "1.2 Justificación" establishing LLMs and Whisper transcription as a scientifically grounded solution to the identified problems
- Insert "1.3 Objetivos" with one general objective and 4-6 specific objectives oriented to the SGR system
- Renumber existing subsections: 1.1→1.4, 1.2→1.5, 1.3→1.6, 1.4→1.7, 1.5→1.8
- Update the "Visión general del documento" (new 1.8) cross-references to reflect new numbering
- Preserve all existing Section 2 and Section 3 content verbatim

**Non-Goals:**
- Modifying any technical content in Sections 2 or 3
- Changing app.py or any code file
- Adding new functional or non-functional requirements
- Modifying existing definitions or references

## Decisions

1. **Insertion approach over append-only** — New sections are inserted at the top of Section 1 rather than appended at the end. Rationale: Problemática, Justificación, and Objetivos establish the academic foundation and should precede the technical specification, following standard thesis structure.

2. **Renumbering over restructuring** — Existing subsection IDs (1.1 through 1.5) shift by +3 to accommodate the new sections, rather than placing new sections at the end of Section 1. Rationale: preserves logical flow from problem statement through technical content without breaking the IEEE 830 section hierarchy.

3. **Single-file edit** — All changes target `requisitos.md` only. Rationale: the thesis methodology sections are part of the SRS document itself, not a separate artifact.

4. **Cross-reference audit** — After insertion, verify all internal cross-references (especially in "Visión general del documento") point to correct section numbers. Rationale: renumbering creates risk of stale references.

## Risks / Trade-offs

- **Section numbering mismatch** — External documents or references that cite section 1.1-1.5 of requisitos.md will be off by +3. Mitigation: this is a thesis submission version; external references are minimal.
- **Document length increase** — Three new subsections add approximately 100-150 lines. Mitigation: the academic value of complete thesis framing outweighs document size considerations.
