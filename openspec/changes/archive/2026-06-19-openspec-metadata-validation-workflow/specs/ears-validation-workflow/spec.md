## ADDED Requirements

### Requirement: EARS validation checklist per functional requirement subsection
Each functional requirement subsection (3.1.1 through 3.1.13) SHALL end with a "Workflow de Validación EARS" checklist that verifies keyword presence and advances the status to `approved`.

#### Scenario: Checklist structure
- **WHEN** a functional requirement subsection is reviewed
- **THEN** it SHALL contain a section titled "### Workflow de Validación EARS" with at least the following checklist items: keyword check for "WHEN", keyword check for "THE SYSTEM SHALL", and a status advancement indicator

### Requirement: Keyword verification rules
The checklist SHALL verify that every requirement in the subsection contains the EARS keywords "WHEN" (trigger condition) and "THE SYSTEM SHALL" (expected behavior) to be considered valid.

#### Scenario: Valid requirement passes
- **WHEN** a requirement contains both "WHEN" and "THE SYSTEM SHALL" in its scenarios
- **THEN** the checklist SHALL mark that requirement as ✅ Passed

#### Scenario: Missing keyword fails
- **WHEN** a requirement is missing "WHEN" or "THE SYSTEM SHALL"
- **THEN** the checklist SHALL mark that requirement as ❌ Failed and list the missing keywords

### Requirement: Status advancement
When all requirements in a subsection pass the EARS validation checklist, the subsection's status SHALL advance from `proposed` to `approved`.

#### Scenario: All passed
- **WHEN** every requirement in the subsection has ✅ Passed
- **THEN** the checklist footer SHALL state: "Estado: approved"

#### Scenario: Some failed
- **WHEN** any requirement has ❌ Failed
- **THEN** the checklist footer SHALL state: "Estado: proposed (pendiente de corrección)"
