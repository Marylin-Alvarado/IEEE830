## ADDED Requirements

### Requirement: Environment documentation
The project SHALL include an `environment.md` file documenting the complete runtime environment for the SGR system.

#### Scenario: Python version documented
- **WHEN** `environment.md` is reviewed
- **THEN** it SHALL specify Python 3.11 as the required runtime version

#### Scenario: Environment variables documented
- **WHEN** `environment.md` is reviewed
- **THEN** it SHALL list all required environment variables for local AI models (Ollama host URL, LlamaCpp host URL, Whisper model path/config) with descriptions and examples

#### Scenario: Folder structure documented
- **WHEN** `environment.md` is reviewed
- **THEN** it SHALL include the complete project folder tree with descriptions of each directory's purpose

### Requirement: Pinned dependency manifest
The project SHALL include a `requirements.txt` file at the root with all Python dependencies pinned to exact versions.

#### Scenario: Core framework dependencies
- **WHEN** `requirements.txt` is inspected
- **THEN** it SHALL include streamlit and pydantic with pinned versions

#### Scenario: AI model dependencies
- **WHEN** `requirements.txt` is inspected
- **THEN** it SHALL include openai (for Ollama-compatible API calls) and requests (for LlamaCpp HTTP calls)

#### Scenario: Reproducible installation
- **WHEN** a new developer runs `pip install -r requirements.txt`
- **THEN** all dependencies SHALL install at the exact pinned versions specified in the file
