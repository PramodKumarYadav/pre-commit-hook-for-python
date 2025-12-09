# Quick Start Guide

Get up and running with pre-commit hooks for Python in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- git

## Setup (5 minutes)

### Step 1: Install Dependencies

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install package in development mode
pip install -e .
```

Or use the Makefile:

```bash
make setup
```

### Step 2: Install Pre-commit Hooks

```bash
# Install the git hooks
pre-commit install
```

That's it! You're ready to go.

## Usage

### Automatic on Commit

Pre-commit hooks will now run automatically every time you commit:

```bash
git add .
git commit -m "Your commit message"
# Hooks run automatically and fix/check your code
```

### Manual Run

Run hooks manually on all files:

```bash
# Run all hooks
pre-commit run --all-files

# Or use make
make pre-commit-run
```

Run specific hooks:

```bash
pre-commit run black      # Format code
pre-commit run ruff       # Lint code
pre-commit run mypy       # Type check
pre-commit run pytest-check  # Run tests
```

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Or use make
make test
make coverage
```

### Format Code

```bash
# Format all Python files
black src/ tests/

# Sort imports
isort src/ tests/

# Or use make to do both
make format
```

### Lint Code

```bash
# Check for issues
ruff check src/ tests/

# Auto-fix issues
ruff check --fix src/ tests/

# Or use make
make lint
make lint-fix
```

## What Happens on Each Commit?

When you commit, the following checks run automatically:

1. **Trailing whitespace** - Removes trailing whitespace
2. **End of file** - Ensures files end with a newline
3. **YAML/JSON/TOML checks** - Validates syntax
4. **Large file check** - Prevents committing large files
5. **Merge conflict check** - Detects merge conflict markers
6. **Black** - Formats your Python code
7. **isort** - Sorts your imports
8. **Ruff** - Lints your code and auto-fixes issues
9. **mypy** - Checks type hints
10. **pytest** - Runs your test suite

If any check fails, the commit is blocked and you need to fix the issues.

## Common Commands

```bash
# Complete setup
make setup

# Format code
make format

# Lint code
make lint
make lint-fix

# Type check
make type-check

# Run tests
make test
make coverage

# Run all pre-commit hooks
make pre-commit-run

# Update hooks to latest versions
make pre-commit-update

# Clean build artifacts
make clean
```

## Skipping Hooks (Not Recommended)

If you really need to skip hooks for a specific commit:

```bash
# Skip all hooks
git commit --no-verify

# Skip specific hooks
SKIP=black,ruff git commit -m "message"
```

**Warning:** Only skip hooks if absolutely necessary!

## Next Steps

1. Check the [README.md](README.md) for detailed documentation
2. Read [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines
3. Customize hooks in `.pre-commit-config.yaml`
4. Customize tool settings in `pyproject.toml`

## Troubleshooting

### Hooks failing?

```bash
# Update hooks
pre-commit autoupdate

# Clean and reinstall
pre-commit clean
pre-commit install
pre-commit run --all-files
```

### Import errors?

```bash
# Reinstall in development mode
pip install -e .
```

### Type checking issues?

```bash
# Check what mypy sees
mypy src/
```

## Support

- 📖 [Full Documentation](README.md)
- 🐛 [Report Issues](https://github.com/PramodKumarYadav/pre-commit-hook-for-python/issues)
- 🤝 [Contributing Guide](CONTRIBUTING.md)

Happy coding! 🚀
