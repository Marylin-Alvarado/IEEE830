## Why

The project lacks automated validation on push — there is no CI pipeline to verify OpenSpec spec syntax, ensure dependency reproducibility (`pip install -r requirements.txt`), or catch regressions early. This risks pushing broken configurations and undermines the thesis reproducibility criteria.

## What Changes

- Create `.github/workflows/` directory structure at project root
- Create `ci.yml` workflow file that triggers on `push` and `pull_request` to `main`
- Workflow steps: checkout, setup Python 3.11, install dependencies, validate OpenSpec spec syntax, verify pip install

## Capabilities

### New Capabilities
- `ci-automation`: Continuous integration workflow for automated spec validation and environment reproducibility checks on push

### Modified Capabilities
- (none)

## Impact

- New directory: `.github/workflows/`
- New file: `.github/workflows/ci.yml`
- No changes to existing code or specs
