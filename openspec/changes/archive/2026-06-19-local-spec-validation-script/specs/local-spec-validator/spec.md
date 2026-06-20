## ADDED Requirements

### Requirement: Spec file metadata validation
The script SHALL read each `.md` file under `openspec/specs/` and verify the presence of `status`, `version`, and `authors` in its metadata header.

#### Scenario: Metadata present
- **WHEN** a spec file contains all three metadata fields
- **THEN** the script SHALL report it as PASS

#### Scenario: Metadata missing
- **WHEN** a spec file is missing `status`, `version`, or `authors`
- **THEN** the script SHALL report the missing field(s) as FAIL

### Requirement: Critical section validation
The script SHALL check each spec file for the presence of critical sections: `Purpose` and `Requirements`.

#### Scenario: All sections present
- **WHEN** a spec file contains both `## Purpose` and `## Requirements`
- **THEN** the script SHALL report it as PASS

#### Scenario: Missing section
- **WHEN** a spec file is missing `## Purpose` or `## Requirements`
- **THEN** the script SHALL report the missing section(s) as FAIL

### Requirement: Summary report
The script SHALL print a summary with total files checked, passed, and failed, and list all failures.

#### Scenario: Summary printed
- **WHEN** the script finishes checking all spec files
- **THEN** it SHALL print `N/M archivos validados — X passed, Y failed` with details of each failure

### Requirement: Exit code
The script SHALL exit with code 0 if all checks pass, and code 1 if any check fails.

#### Scenario: All pass
- **WHEN** every spec file passes all checks
- **THEN** the script SHALL exit with code 0

#### Scenario: Any failure
- **WHEN** at least one check fails
- **THEN** the script SHALL exit with code 1
