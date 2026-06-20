## Why

There is no local pre-validation tool to check that OpenSpec spec files maintain their metadata header (status, version, authors) and contain all critical sections before committing. The CI workflow validates syntax remotely, but a local script enables faster feedback during thesis development.

## What Changes

- Create `scripts/` directory at project root
- Create `scripts/validate_specs.py` with automated logic to:
  - Read all `.md` spec files under `openspec/specs/`
  - Verify YAML/metadata header contains `status`, `version`, `authors`
  - Check for presence of critical sections (Purpose, Requirements)
  - Alert if any metadata field or critical section is missing

## Capabilities

### New Capabilities
- `local-spec-validator`: Python script for local pre-validation of OpenSpec spec file metadata and section completeness

### Modified Capabilities
- (none)

## Impact

- New directory: `scripts/`
- New file: `scripts/validate_specs.py`
- No changes to existing code or spec files
