# Makefile for Python project with pre-commit hooks

.PHONY: help install install-dev setup clean test lint format type-check pre-commit-install pre-commit-run pre-commit-update coverage

help:
	@echo "Available commands:"
	@echo "  make install            - Install production dependencies"
	@echo "  make install-dev        - Install development dependencies"
	@echo "  make setup              - Complete setup (install-dev + pre-commit)"
	@echo "  make clean              - Remove build artifacts and cache"
	@echo "  make test               - Run tests with pytest"
	@echo "  make coverage           - Run tests with coverage report"
	@echo "  make lint               - Run linter (ruff)"
	@echo "  make format             - Format code (black + isort)"
	@echo "  make type-check         - Run type checker (mypy)"
	@echo "  make pre-commit-install - Install pre-commit hooks"
	@echo "  make pre-commit-run     - Run pre-commit on all files"
	@echo "  make pre-commit-update  - Update pre-commit hooks"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt
	pip install -e .

setup: install-dev pre-commit-install
	@echo "Setup complete! You're ready to start developing."

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

test:
	pytest

coverage:
	pytest --cov=src --cov-report=term-missing --cov-report=html
	@echo "Coverage report generated in htmlcov/index.html"

lint:
	ruff check src/ tests/

lint-fix:
	ruff check --fix src/ tests/

format:
	black src/ tests/
	isort src/ tests/

type-check:
	mypy src/

pre-commit-install:
	pre-commit install

pre-commit-run:
	pre-commit run --all-files

pre-commit-update:
	pre-commit autoupdate

# Run all quality checks
check: format lint type-check test
	@echo "All checks passed!"
