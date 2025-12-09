# Pre-commit Hooks for Python

A comprehensive template repository demonstrating best practices for Python development using pre-commit hooks. This template includes automated code formatting, linting, type checking, and testing.

## 🎯 Features

This repository includes pre-commit hooks for:

- **Code Formatting**
  - [Black](https://github.com/psf/black) - Opinionated Python code formatter
  - [isort](https://github.com/PyCQA/isort) - Automatic import sorting

- **Linting**
  - [Ruff](https://github.com/astral-sh/ruff) - Fast Python linter (replaces Flake8, pylint, etc.)

- **Type Checking**
  - [mypy](https://github.com/python/mypy) - Static type checker

- **Testing**
  - [pytest](https://github.com/pytest-dev/pytest) - Testing framework
  - [pytest-cov](https://github.com/pytest-dev/pytest-cov) - Coverage reporting

- **General Checks**
  - Trailing whitespace removal
  - End-of-file fixer
  - YAML/JSON/TOML validation
  - Large file detection
  - Merge conflict detection
  - Debug statement detection

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🚀 Installation

### 1. Clone or Use This Template

```bash
# Clone this repository
git clone https://github.com/PramodKumarYadav/pre-commit-hook-for-python.git
cd pre-commit-hook-for-python

# Or click "Use this template" on GitHub
```

### 2. Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Or install using pyproject.toml
pip install -e ".[dev]"
```

### 4. Install Pre-commit Hooks

```bash
# Install the pre-commit hooks
pre-commit install

# (Optional) Run hooks on all files
pre-commit run --all-files
```

## 💻 Usage

### Running Pre-commit Hooks

Once installed, the hooks will automatically run on every `git commit`. You can also run them manually:

```bash
# Run on all files
pre-commit run --all-files

# Run on staged files only
pre-commit run

# Run a specific hook
pre-commit run black
pre-commit run ruff
pre-commit run pytest-check
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_calculator.py

# Run tests in verbose mode
pytest -v
```

### Code Formatting

```bash
# Format code with Black
black src/ tests/

# Sort imports with isort
isort src/ tests/

# Both will run automatically on commit
```

### Linting

```bash
# Lint with Ruff
ruff check src/ tests/

# Auto-fix issues
ruff check --fix src/ tests/
```

### Type Checking

```bash
# Check types with mypy
mypy src/
```

## 📁 Project Structure

```
pre-commit-hook-for-python/
├── .pre-commit-config.yaml    # Pre-commit hooks configuration
├── pyproject.toml              # Project and tool configurations
├── requirements.txt            # Production dependencies
├── requirements-dev.txt        # Development dependencies
├── src/                        # Source code
│   ├── __init__.py
│   └── sample_module/
│       ├── __init__.py
│       ├── calculator.py       # Sample calculator module
│       └── string_utils.py     # Sample string utilities
└── tests/                      # Test files
    ├── __init__.py
    ├── test_calculator.py      # Calculator tests
    └── test_string_utils.py    # String utilities tests
```

## ⚙️ Configuration

### Black Configuration

Black is configured in `pyproject.toml`:
- Line length: 88 characters
- Target Python versions: 3.8-3.12

### isort Configuration

isort is configured to work with Black:
- Profile: black
- Line length: 88 characters

### Ruff Configuration

Ruff replaces multiple tools (Flake8, pylint, etc.):
- Includes checks for: pycodestyle, pyflakes, isort, flake8-bugbear, pyupgrade
- Line length: 88 characters
- Auto-fixes enabled

### mypy Configuration

Type checking configuration:
- Target: Python 3.8+
- Ignores missing imports by default

### pytest Configuration

Testing framework configuration:
- Minimum version: 7.0
- Coverage reporting enabled
- Test discovery: `test_*.py` and `*_test.py`

## 🔧 Customization

### Adding New Hooks

Edit `.pre-commit-config.yaml` to add more hooks. Visit [pre-commit.com/hooks.html](https://pre-commit.com/hooks.html) for available hooks.

### Modifying Tool Settings

Edit `pyproject.toml` to customize tool configurations:

```toml
[tool.black]
line-length = 100  # Change line length

[tool.ruff]
ignore = ["E501"]  # Ignore specific rules

[tool.pytest.ini_options]
addopts = "-v"     # Add pytest options
```

### Skipping Hooks

To skip hooks for a specific commit:

```bash
# Skip all hooks
git commit --no-verify

# Skip specific hook
SKIP=black git commit -m "message"

# Skip multiple hooks
SKIP=black,ruff git commit -m "message"
```

## 📚 Hook Details

### 1. Black (Code Formatter)

Automatically formats Python code to ensure consistent style.

- **When it runs**: On every commit
- **What it does**: Reformats code to Black's style
- **Configuration**: `pyproject.toml` → `[tool.black]`

### 2. isort (Import Sorter)

Sorts and organizes import statements.

- **When it runs**: On every commit
- **What it does**: Sorts imports alphabetically and by type
- **Configuration**: `pyproject.toml` → `[tool.isort]`

### 3. Ruff (Linter)

Fast Python linter that checks for errors and style issues.

- **When it runs**: On every commit
- **What it does**: Checks code quality and fixes issues automatically
- **Configuration**: `pyproject.toml` → `[tool.ruff]`

### 4. mypy (Type Checker)

Static type checker for Python.

- **When it runs**: On every commit
- **What it does**: Checks type hints and catches type errors
- **Configuration**: `pyproject.toml` → `[tool.mypy]`

### 5. pytest (Test Runner)

Runs Python tests to ensure code correctness.

- **When it runs**: On every commit (only on Python files)
- **What it does**: Runs test suite to catch breaking changes
- **Configuration**: `pyproject.toml` → `[tool.pytest.ini_options]`

## 🎓 Best Practices

1. **Run hooks before pushing**: Always run `pre-commit run --all-files` before pushing
2. **Keep hooks updated**: Run `pre-commit autoupdate` regularly
3. **Don't skip hooks unnecessarily**: Hooks are there to help maintain code quality
4. **Write tests first**: Add tests for new features before implementing them
5. **Use type hints**: Add type hints to all functions for better code quality
6. **Keep commits small**: Smaller commits make it easier to identify issues

## 🔍 Troubleshooting

### Hooks failing?

```bash
# Update pre-commit hooks
pre-commit autoupdate

# Clean cache and reinstall
pre-commit clean
pre-commit install
```

### Import errors in tests?

```bash
# Install package in development mode
pip install -e .
```

### mypy type checking issues?

```bash
# Install type stubs
pip install types-all
```

## 📖 Additional Resources

- [Pre-commit Documentation](https://pre-commit.com/)
- [Black Documentation](https://black.readthedocs.io/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [pytest Documentation](https://docs.pytest.org/)
- [mypy Documentation](https://mypy.readthedocs.io/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run pre-commit hooks
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Pre-commit framework by Anthony Sottile
- Black formatter by Python Software Foundation
- Ruff linter by Astral
- pytest testing framework
- All contributors to the open-source tools used in this template
