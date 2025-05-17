# Contributing

Thank you for taking the time to contribute!

## Installing dependencies

Set up a virtual environment and install the development packages with `uv`:

```bash
uv venv .venv
source .venv/bin/activate
uv sync --group dev
```

## Running tests and lint checks

Run the test suite with `pytest`:

```bash
.venv/bin/pytest -q
```

The repository uses **Black**, **isort** and **Ruff** via `pre-commit`. Run all
lint checks with:

```bash
.venv/bin/pre-commit run --all-files
```

## Opening issues and pull requests

Use the templates under `.github/ISSUE_TEMPLATE` when creating a new issue. For
code changes, open a pull request against the `main` branch and describe your
changes using the provided PR template.
