# EARS Grammar Validation

## Purpose

Define the capabilities for validating that generated requirements conform to the EARS (Easy Approach to Requirements Syntax) grammar, ensuring structured, unambiguous requirement statements.

## Requirements

### Requirement: EARS grammar validation engine
The system SHALL validate that each requirement conforms to one of the five EARS syntax categories: Ubiquitous, Event-Driven, State-Driven, Optional, or Desired.

#### Scenario: Ubiquitous requirement detected
- **WHEN** a requirement uses the keyword SHALL with an active verb and no triggering condition
- **THEN** the system SHALL classify it as Ubiquitous and validate its structure

#### Scenario: Event-Driven requirement detected
- **WHEN** a requirement contains a WHEN clause followed by THEN or SHALL
- **THEN** the system SHALL classify it as Event-Driven and validate the trigger-response structure

#### Scenario: State-Driven requirement detected
- **WHEN** a requirement contains a WHILE clause describing a continuous state
- **THEN** the system SHALL classify it as State-Driven and validate the state-condition structure

#### Scenario: Optional requirement detected
- **WHEN** a requirement contains WHERE clause describing a conditional feature
- **THEN** the system SHALL classify it as Optional and validate the condition

#### Scenario: Desired requirement detected
- **WHEN** a requirement uses the keyword SHOULD or WANT instead of SHALL
- **THEN** the system SHALL classify it as Desired and flag it as non-mandatory

### Requirement: Strict syntax validation rules for Ubiquitous
Ubiquitous requirements SHALL follow the pattern: `<entity> SHALL <action>` with no conditional clauses.

#### Scenario: Valid Ubiquitous syntax
- **WHEN** the requirement is "El sistema SHALL proporcionar un formulario de registro"
- **THEN** the validator SHALL accept it as valid Ubiquitous

#### Scenario: Invalid Ubiquitous syntax
- **WHEN** the requirement includes WHEN inside a Ubiquitous pattern
- **THEN** the validator SHALL reject it and suggest Event-Driven classification

### Requirement: Strict syntax validation rules for Event-Driven
Event-Driven requirements SHALL follow the pattern: `WHEN <trigger> THEN <entity> SHALL <response>` or `WHEN <trigger> <entity> SHALL <response>`.

#### Scenario: Valid Event-Driven syntax
- **WHEN** the requirement is "WHEN el usuario envía el formulario ENTONCES el sistema SHALL validar los datos"
- **THEN** the validator SHALL accept it as valid Event-Driven

#### Scenario: Missing THEN clause
- **WHEN** the requirement has WHEN but no THEN or SHALL response
- **THEN** the validator SHALL reject it with an error indicating the missing response clause

### Requirement: Strict syntax validation rules for State-Driven
State-Driven requirements SHALL follow the pattern: `WHILE <state> <entity> SHALL <action>`.

#### Scenario: Valid State-Driven syntax
- **WHEN** the requirement is "WHILE el archivo está abierto el sistema SHALL bloquear escrituras concurrentes"
- **THEN** the validator SHALL accept it as valid State-Driven

### Requirement: Strict syntax validation rules for Optional
Optional requirements SHALL follow the pattern: `WHERE <feature> <entity> SHALL <action>`.

#### Scenario: Valid Optional syntax
- **WHEN** the requirement is "WHERE la transcripción está habilitada el sistema SHALL mostrar el texto transcrito"
- **THEN** the validator SHALL accept it as valid Optional

### Requirement: Strict syntax validation rules for Desired
Desired requirements SHALL follow the pattern: `<entity> SHOULD <action>` or `<entity> WANT <action>`.

#### Scenario: Valid Desired syntax
- **WHEN** the requirement is "El sistema SHOULD soportar formatos adicionales de audio"
- **THEN** the validator SHALL accept it as valid Desired but flag it as non-mandatory

### Requirement: Validation error reporting
When a requirement fails EARS syntax validation, the system SHALL provide specific error messages indicating the rule violated and suggested correction.

#### Scenario: Detailed validation error
- **WHEN** a requirement fails validation
- **THEN** the system SHALL return the EARS category attempted, the specific rule violated, and a corrected example
