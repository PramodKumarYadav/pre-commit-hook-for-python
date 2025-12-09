"""Setup file for the package."""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pre-commit-hook-for-python",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A template repository for working with pre-commit hooks for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PramodKumarYadav/pre-commit-hook-for-python",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pre-commit>=3.6.0",
            "black>=23.12.0",
            "isort>=5.13.0",
            "ruff>=0.1.9",
            "mypy>=1.8.0",
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
        ],
    },
)
