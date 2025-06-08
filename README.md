# AnoDesign


Designs and testing, mainly in Python.


## Book Notes

Notes for _Generating Sound & Organizing Time_ by Wakefield and Taylor can be found 
in ```gen/GSOT1/Booknotes.md```.


## UV Notes

[UV](https://github.com/astral-sh/uv) is used to manage the project and Python packages to make this work.

### Installation

```zsh
brew install uv
```


### Run Jupyter Lab in the Browser

```zsh
uv run --with jupyter jupyter lab
```


### Documentation

- [Documentation](https://docs.astral.sh/uv/)
- [Features](https://docs.astral.sh/uv/getting-started/features/)
- [Tools](https://docs.astral.sh/uv/concepts/tools/#upgrading-tools)


### Commands

```zsh
uv add pandas               # Install a Python library (e.g., pandas)
uv remove pandas            # Uninstall a Python library (e.g., pandas)
uv run example.py           # Run a Python script
uv run pytest               # Run pytest

```

## Ruff Notes

[Ruff](https://github.com/astral-sh/ruff) is a Python linter and code formatter.


### Installation

```zsh
brew install ruff
```

### Documentation

- [Documentation](https://docs.astral.sh/ruff/)
- [Linter](https://docs.astral.sh/ruff/linter/)
- [Formatter](https://docs.astral.sh/ruff/formatter/)


### Commands

```zsh
# Linter
ruff check                    # Lint files in the current directory.
ruff check --fix              # Lint files in the current directory and fix any fixable errors.
ruff check --watch            # Lint files in the current directory and re-lint on change.
ruff check path/to/code/      # Lint files in `path/to/code`.

# Formatter
ruff format                   # Format all files in the current directory.
ruff format path/to/code/     # Format all files in `path/to/code` (and any subdirectories).
ruff format path/to/file.py   # Format a single file.
```
