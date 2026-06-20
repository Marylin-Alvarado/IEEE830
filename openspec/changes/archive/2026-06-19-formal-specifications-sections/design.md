## Context

The app currently renders 3 static sections (3.1 RF, 3.2 NFR, 3.3 Business Rules) from hardcoded data. There is no LLM prompt defined, no Mermaid rendering, and no sanitization layer. The change adds 4 new formal-spec sections as both data and rendering infrastructure.

## Goals / Non-Goals

**Goals:**
- Define `LLM_PROMPT_TEMPLATE` as a multiline constant requesting 4 formal sections
- Implement `sanitize_output()` that removes backticks/commas/escapes which break `st.markdown()` Mermaid blocks
- Provide example data for all 4 sections so the UI renders without a real LLM
- Render sections 2.1–2.4 below existing requirement output

**Non-Goals:**
- No actual HTTP call to an LLM (the prompt template is prepared but not invoked)
- No changes to existing 3.1–3.3 sections
- No runtime streaming or async logic

## Decisions

- **`sanitize_output()` operates as a single pass**: Strips triple-backticks that are not part of a valid Mermaid code fence, normalizes quotes, and removes trailing commas that confuse `st.markdown()`. This is applied before `st.markdown()`.
- **Mermaid diagram strings stored as constants**: The use-case and sequence diagrams are stored as dedicated Python strings with the correct ```` ```mermaid ```` fence included, so they can be fed directly into `st.markdown()`.
- **Example user stories mirror real project roles**: 3 stories use the format "Como [rol], quiero [acción], para [beneficio]" with Gherkin acceptance criteria, matching the SGR's actual actors (Analista, Revisor, Desarrollador).

## Risks / Trade-offs

- [Mermaid syntax breakage] If Streamlit's Mermaid renderer changes, diagrams may fail silently. Mitigation: diagrams are plain strings so they degrade to raw code blocks.
- [Prompt unused until LLM integration] The prompt template exists but no code calls the LLM yet. Mitigation: the prompt is separated as a constant ready for the future `consultar_llm()` function.
