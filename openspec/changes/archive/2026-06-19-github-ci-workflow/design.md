## Context

The project currently has no CI pipeline. Every change proposal requires manual validation of OpenSpec syntax and dependency reproducibility. A GitHub Actions workflow on push will automate these checks and enforce quality before merging to `main`.

## Goals / Non-Goals

**Goals:**
- Create `.github/workflows/ci.yml` that runs on push and PR to `main`
- Validate OpenSpec spec syntax via `npx openspec validate`
- Verify `pip install -r requirements.txt` succeeds

**Non-Goals:**
- No deployment or release steps
- No test execution (no test suite exists yet)
- No code linting or formatting checks

## Decisions

- **Single job pipeline**: A single `validate` job with sequential steps (checkout → Python → install → validate). Simpler than multi-job for this scope.
- **`actions/checkout@v4`**: Standard GitHub checkout action with full history.
- **`actions/setup-python@v5`**: With `python-version: '3.11'` and caching for pip.
- **`npx openspec validate`**: Validate all specs in the repository. Requires Node.js (npx comes with npm, pre-installed on GitHub runners).
- **Fail-fast**: Any step failure stops the workflow and marks the check as failed.

## Risks / Trade-offs

- **Node.js not installed**: GitHub Actions Ubuntu runners include Node.js/npm by default. Mitigation: pin `runs-on: ubuntu-latest`.
- **`openspec` CLI not found**: `npx` will auto-download. Mitigation: ensure `package.json` is present in repo (`.opencode/package.json` exists with `@opencode-ai/plugin`).
