# Contributing to Pre-commit Hooks for Python

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/pre-commit-hook-for-python.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Set up the development environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements-dev.txt
   pip install -e .
   pre-commit install
   ```

## Development Workflow

1. Make your changes
2. Write or update tests
3. Run the test suite: `pytest`
4. Format your code: `make format`
5. Run linting: `make lint`
6. Run type checking: `make type-check`
7. Run all pre-commit hooks: `pre-commit run --all-files`
8. Commit your changes: `git commit -m "Description of changes"`
9. Push to your fork: `git push origin feature/your-feature-name`
10. Create a Pull Request

## Code Standards

- Follow PEP 8 style guide (enforced by Black and Ruff)
- Write docstrings for all functions and classes (Google style)
- Add type hints to function signatures
- Maintain test coverage above 80%
- Keep functions focused and small
- Write clear commit messages

## Testing

- Write tests for all new features
- Ensure all tests pass before submitting PR
- Use descriptive test names
- Follow the Arrange-Act-Assert pattern

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Ensure all tests pass and pre-commit hooks succeed
3. Update documentation if you've made significant changes
4. Your PR will be reviewed by maintainers
5. Address any feedback from reviewers
6. Once approved, your PR will be merged

## Questions?

If you have questions, please open an issue for discussion.

Thank you for contributing!
