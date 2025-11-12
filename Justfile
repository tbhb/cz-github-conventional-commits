set unstable

# List available recipes
default:
  @just --list

# Install all dependencies (Python + Node.js)
install:
  uv sync --frozen

# Build the Python package
build: install
  uv build

# Run tests
test: install
  uv run --frozen pytest

# Run tests with coverage report
test-coverage: install
  uv run --frozen pytest \
    --cov=cz_github_conventional_commits \
    --cov-report=term-missing:skip-covered \
    --cov-report=html \
    --cov-report=xml \
    --cov-branch \
    --junitxml=test-results.xml

# Format code
format: install
  uv run --frozen codespell -w
  uv run --frozen ruff format .
  uv run --frozen djlint docs/overrides --reformat

# Lint code
lint: install
  uv run --frozen codespell
  uv run --frozen yamllint --strict .
  uv run --frozen ruff check .
  uv run --frozen mypy

lint-python: install
  uv run --frozen codespell -w
  uv run --frozen ruff check .
  uv run --frozen ruff format --check .
  uv run --frozen mypy

lint-types: install
  uv run --frozen mypy

# Lint GitHub Actions workflows
lint-actions: install
  actionlint

# Lint documentation with Vale
lint-vale:
  vale sync
  vale --glob='!{.vale/**/*,.venv/**/*,**/.pytest_cache/**/*}' .

lint-yaml: install
  uv run --frozen yamllint --strict .

# Run pre-commit hooks
pre-commit: install
  uv run --frozen prek

# Clean build artifacts
clean:
  rm -rf dist/
  find . -type d -name __pycache__ -exec rm -rf {} +
  find . -type d -name .pytest_cache -exec rm -rf {} +
  find . -type d -name .ruff_cache -exec rm -rf {} +
