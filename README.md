# Python Template

This project offers a robust, ready-to-use boilerplate, designed to kickstart your new Python projects with confidence. It comes packed with pre-configured best practices and essential tools, letting you dive straight into development.

---

## What's Included

We've bundled the following to get you up and running quickly:

- **⚡️ Speedy Package Management:** Utilizes [uv](https://docs.astral.sh/uv/) for incredibly fast dependency resolution and package installation.
- **✅ Strict Type-Checking:** Enforces code quality with [mypy](https://www.mypy-lang.org/) for robust static type analysis, catching errors early.
- **✨ Blazing-Fast Linting & Formatting:** Leverages [ruff](https://docs.astral.sh/ruff/) for an all-in-one, high-performance linter, code formatter, and more.
- **🚫 Automated Quality Checks:** Integrates [pre-commit](https://pre-commit.com/) hooks for `ruff`, `mypy`, `codespell`, `absolufy-imports`, `uv lock`, and other essential checks, ensuring code consistency before commits.
- **💻 VS Code Integration:** Includes `.vscode/` settings for streamlined development, with editor configurations and debug settings right out of the box.
- **🤖 GitHub Actions Workflow:** Provides `.github/` workflows for automated `pre-commit` checks, unit, and integration testing (on windows/linux/mac).
- **🔗 Git Attributes:** Standardizes `.gitattributes` for consistent line endings, optimized diffs, and common Git configurations tailored for Python projects.
- **📁 Structured Source Directory:** A clear `src/` directory where your application code resides, complete with an example `main.py` to get you started.
- **🌈 Enhanced Terminal Logging:** Configured with [colorlog](https://pypi.org/project/colorlog/) to provide highly readable, colored log output directly in your terminal, making debugging a breeze.
- **📄 Standard Project Files:** Includes a `LICENSE` and this `README.md` for proper project documentation and licensing.

---

## Getting Started

Follow these steps to set up your new project:

### Prerequisites

Before you begin, ensure you have:

- **Python 3.8 or higher** installed on your system.
- **[uv](https://github.com/astral-sh/uv)**, our recommended tool for dependency management.

### Usage

1. **Clone the Template:**
   Clone this repository and rename the project directory to your desired project name:

2. **Install Dependencies:**
   Initialize a virtual environment and install all project dependencies using `uv`:

   ```sh
   uv venv
   uv pip install -r pyproject.toml
   ```

3. **Install Pre-Commit Hooks:**
   Set up the pre-commit hooks to automate code quality checks before each commit:

   ```sh
   pre-commit install
   ```

4. **Start Developing:**
   Begin building your awesome Python project within the `src/` directory.

5. **Run the Example Script:**
   Test your setup by running the included example:

   ```sh
   cd src
   python main.py
   ```

   Alternatively, you can use the pre-configured VS Code debug settings in [.vscode/launch.json](.vscode/launch.json) for a seamless debugging experience.

---

## Customization

This template is designed to be flexible. Here's how you can tailor it to your needs:

- **Add Your Modules:** Create and organize your application's modules within the `src/` directory.
- **Manage Dependencies:** Update `pyproject.toml` to add or remove project dependencies and adjust metadata.
- **Configure Tools:** Fine-tune `mypy.ini` and `ruff.toml` to align with your specific coding style and static analysis requirements.

---

## License

This project is open-sourced under the terms of the [LICENSE](LICENSE).
