## 1. Prompt Template and Sanitization

- [x] 1.1 Add `LLM_PROMPT_TEMPLATE` constant with system prompt requesting sections 2.1–2.4 and Mermaid syntax
- [x] 1.2 Add `sanitize_output(text: str) -> str` function that strips conflicting backtick/quote sequences

## 2. Example Data for Formal Sections

- [x] 2.1 Add example data for section 2.1 Spech & Tech Specifications (architecture, APIs, schemas)
- [x] 2.2 Add example data for section 2.2 Historias de Usuario (3 stories with Gherkin criteria)
- [x] 2.3 Add example Mermaid `graph TD` string for section 2.3 Use Case Diagram
- [x] 2.4 Add example Mermaid `sequenceDiagram` string for section 2.4 Sequence Diagram

## 3. Rendering Blocks

- [x] 3.1 Add rendering block for 2.1 Spech & Tech Specifications below business rules
- [x] 3.2 Add rendering block for 2.2 Historias de Usuario
- [x] 3.3 Add rendering block for 2.3 Mermaid Use Case Diagram
- [x] 3.4 Add rendering block for 2.4 Mermaid Sequence Diagram
