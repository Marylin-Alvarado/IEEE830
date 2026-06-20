## Context

The SGR application exists as `app.py` with Pydantic models, JSON persistence, and a Streamlit UI. The archived change `sgr-streamlit-app` and current specs at `openspec/specs/` document requirements at the capability level but not as a unified IEEE 830 SRS. The thesis requires a complete IEEE 830-1998 Software Requirements Specification document that presents the system in a standards-compliant format, with explicit traceability from each IEEE 830 section to the implemented code.

## Goals / Non-Goals

**Goals:**
- Produce `requisitos.md` following the IEEE 830-1998 standard structure (1. Introducción, 2. Descripción General, 3. Requisitos Específicos)
- Cover all functional requirements implemented in `app.py` (project registration, validation, persistence, listing)
- Include non-functional requirements appropriate for a Streamlit-based thesis tool
- Reference code files and spec files for traceability
- Write entirely in Spanish (as required by the thesis)

**Non-Goals:**
- Modify `app.py` or any existing code
- Generate new requirements not already implemented
- Create a multi-document SRS — single `requisitos.md` file
- IEEE 830 sections beyond the three main headings (1, 2, 3)

## Decisions

1. **IEEE 830-1998 structure** — The standard defines sections 1 (Introducción), 2 (Descripción General), and 3 (Requisitos Específicos). The document follows this exactly, with subsections adapted to the SGR scope.

2. **Single file `requisitos.md`** — A single Markdown file is sufficient for a thesis-grade SRS of this scope. It is easy to review, render, and include in the thesis document.

3. **Traceability via inline references** — Each requirement section references the corresponding code file (`app.py` lines, Pydantic model fields, Streamlit components) so the thesis evaluator can verify that each documented requirement has a concrete implementation.

4. **EARS taxonomy in section 3** — The specific requirements incorporate EARS (Easy Approach to Requirements Syntax) classification (ubiquitous, state-driven, event-driven, optional, unwanted) alongside the IEEE 830 structure, as this is part of the SGR concept.

## Risks / Trade-offs

- **Static document** — `requisitos.md` must be manually updated if `app.py` changes. No automated synchronization. Acceptable for a thesis deliverable.
- **Scope limitation** — IEEE 830 covers many optional subsections (e.g., user characteristics, assumptions, dependencies). Some are marked as TBD or "not applicable" to keep the document honest.
