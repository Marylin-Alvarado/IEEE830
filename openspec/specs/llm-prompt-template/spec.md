# LLM Prompt Template

## Purpose

Define the system prompt template that instructs the LLM to generate formal specifications sections (2.1–2.4) as part of the SRS output.

## Requirements

### Requirement: Prompt requests 4 formal sections
The system SHALL provide a prompt template that instructs the LLM to output exactly four sections: Spech & Tech Specifications, User Stories, Use Case Diagram (Mermaid), and Sequence Diagram (Mermaid).

#### Scenario: Sections enumerated in prompt
- **WHEN** the prompt template is read
- **THEN** it SHALL enumerate "## 2.1 Spech & Tech Specifications", "## 2.2 Historias de Usuario", "## 2.3 Diagrama de Casos de Uso (UML)", and "## 2.4 Diagrama de Secuencia (UML)"

### Requirement: Prompt specifies Mermaid syntax
The system SHALL instruct the LLM to output Mermaid diagrams inside fenced code blocks with the `mermaid` language tag.

#### Scenario: Mermaid fence required
- **WHEN** the prompt template instructs diagram output
- **THEN** it SHALL specify that diagrams use ` ```mermaid ` fences with `graph TD` for use cases and `sequenceDiagram` for sequence diagrams
