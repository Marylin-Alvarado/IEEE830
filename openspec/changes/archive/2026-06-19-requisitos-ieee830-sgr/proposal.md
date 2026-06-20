## Why

The SGR application has been built (project registration with IEEE 830/EARS concepts), but it lacks formal IEEE 830-compliant documentation that describes the system's requirements, architecture, and design rationale. For the thesis, it is essential to produce a complete Software Requirements Specification following the IEEE 830-1998 standard, linking each section to the actual implemented code. This change creates that documentation artifact.

## What Changes

- Create `requisitos.md` at project root with the full IEEE 830 SRS structure (Introducción, Descripción General, Requisitos Específicos)
- Map each IEEE 830 section to the existing `app.py` implementation, existing specs, and Pydantic model
- Link existing capabilities (project-registration, data-persistence, project-listing) into the IEEE 830 document structure
- Document the architecture, interfaces, and constraints as required by the thesis guide

## Capabilities

### New Capabilities
- `ieee830-srs`: IEEE 830-compliant Software Requirements Specification document covering introduction, general description, and specific requirements for the SGR system

### Modified Capabilities
*(No existing capabilities are modified — this is a documentation-only addition)*

## Impact

- **New file**: `requisitos.md` — IEEE 830 SRS document at project root
- **No code changes**: All existing functionality in `app.py`, `openspec/specs/`, and archived change artifacts remains unchanged
- **Reference**: Links to `app.py`, existing specs, and the Pydantic `Proyecto` model
