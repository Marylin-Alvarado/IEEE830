## Purpose

This capability allows users to register software projects through a Streamlit form. It collects the project name, general objective, and domain description, applying Pydantic strict validation to ensure no fields are empty.

## Requirements

### Requirement: Project registration form
The system SHALL provide a form with three text fields: *Nombre del Proyecto*, *Objetivo General*, and *Descripción del Dominio*.

#### Scenario: User fills all fields correctly
- **WHEN** the user enters valid text in all three fields and clicks the save button
- **THEN** the system SHALL validate the input and save the project

#### Scenario: User leaves a field empty
- **WHEN** the user clicks save with one or more fields empty
- **THEN** the system SHALL display a validation error for each empty field

### Requirement: Pydantic strict validation
The system SHALL use Pydantic to validate that none of the three fields are empty strings.

#### Scenario: Empty string submitted
- **WHEN** any field contains only whitespace or is empty
- **THEN** the validation SHALL reject the submission with an error message

### Requirement: Save confirmation
The system SHALL display a success confirmation message after a project is saved.

#### Scenario: Successful save
- **WHEN** the project passes validation and is saved to the file
- **THEN** the system SHALL show a success message indicating the project was saved
