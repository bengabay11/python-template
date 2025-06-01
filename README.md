# Python Template

This project provides a robust boilerplate to kickstart new Python projects with best practices and essential tools preconfigured.

## What’s Included

- Package management using [uv](https://docs.astral.sh/uv/).
- Strict type-checking using [mypy](https://www.mypy-lang.org/).
- An extremely fast Python linter, code formatter and more - [ruff](https://docs.astral.sh/ruff/rules/).
- [pre-commit](https://pre-commit.com/) hooks for ruff, mypy, codespell, absolufy-imports, uv lock, and more
- `💻 .vscode/`: Editor settings and debug configuration for VS Code
- `🤖 .github/`: GitHub Actions workflow for pre-commit, and unit/integration testing
- `🔗 .gitattributes`: Consistent line endings, diff settings and common configuration for python projects.
- `📁 src/`: Source code directory (with example `main.py`)
- `📄 LICENSE`, `📖 README.md`: Licensing and documentation

## Getting Started

### Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) (for dependency management)

### Usage

1. Clone this template and rename the project directory as needed.
2. Install dependencies with uv:

   ```sh
   uv venv
   uv pip install -r pyproject.tomlpyproject.toml
   ```

3. Install the pre-commit hooks:

   ```sh
   pre-commit install
   ```

4. Start developing your Python project in the `src/` directory.

5. Run the example script:

   ```sh
   cd src
   python main.py
   ```

   Or use the vscode configuration in [launch.json](.vscode/launch.json)

## Customization

- Add your own modules to `src/`
- Update `pyproject.toml` for dependencies and metadata
- Adjust `mypy.ini` and `ruff.toml` to fit your style and needs

## License

See [LICENSE](LICENSE) for details.
