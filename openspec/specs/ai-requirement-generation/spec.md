# AI Requirement Generation

## Purpose

Define the capabilities for generating structured IEEE 830 software requirements using a local Large Language Model (LLM) from project descriptions and domain context.

## Requirements

### Requirement: LLM-based requirement generation
The system SHALL use a local Large Language Model to generate structured IEEE 830 requirements from a project description and domain context.

#### Scenario: Generate requirements from project data
- **WHEN** the user provides a project description (nombre, objetivo, dominio) and triggers requirement generation
- **THEN** the system SHALL construct a structured prompt and send it to the local LLM inference endpoint

#### Scenario: Receive structured output
- **WHEN** the LLM returns a completion
- **THEN** the system SHALL parse the response into structured IEEE 830 sections (functional requirements, non-functional requirements, interfaces)

### Requirement: Prompt engineering for IEEE 830
The system SHALL use a carefully designed system prompt that instructs the LLM to output requirements following the IEEE 830-1998 structure and EARS syntax.

#### Scenario: Prompt includes standard rules
- **WHEN** constructing the prompt for requirement generation
- **THEN** the system SHALL include the IEEE 830 section template and EARS syntax rules in the system prompt

### Requirement: Local model inference
The system SHALL support local LLM inference through Ollama API or LlamaCpp server endpoints.

#### Scenario: Inference via Ollama
- **WHEN** the system sends a generation request to Ollama
- **THEN** it SHALL use the Ollama REST API at the configured endpoint with the specified model

#### Scenario: Inference via LlamaCpp
- **WHEN** the system sends a generation request to LlamaCpp
- **THEN** it SHALL use the LlamaCpp server API with the configured model and context window
