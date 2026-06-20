## Why

The current "Generar Requisitos con IA" output only renders IEEE 830 requirement sections (3.1-3.3). It lacks formal specifications (architecture, user stories, UML diagrams) that a complete SRS document should include. Adding sections 2.1-2.4 with Mermaid diagrams makes the output a self-contained technical specification ready for review.

## What Changes

- Add `LLM_PROMPT_TEMPLATE` constant in `app.py` that instructs the model to emit 4 formal sections
- Add `sanitize_output()` function to strip conflicting backtick/quote sequences before `st.markdown()` rendering
- Add example/placeholder data for the 4 new sections (Spech & Tech, User Stories, Use Case Diagram, Sequence Diagram)
- Add rendering blocks below 3.3 Reglas de Negocio to display the new sections when activated

## Capabilities

### New Capabilities
- `llm-prompt-template`: Define the system prompt that the LLM receives to produce formal specifications sections

### Modified Capabilities
- `requirements-ui`: Add rendering for sections 2.1–2.4 (Spech & Tech, User Stories, Mermaid UML diagrams)

## Impact

- `app.py`: Add prompt template constant (~40 lines), sanitize function (~15 lines), 4 example data structures (~80 lines), 4 rendering blocks (~50 lines)
