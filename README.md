# Python Data Science 1

## Environment Setup

Run the following commands from the project root.

Create a virtual environment (first-time setup only):

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Deactivate the virtual environment:

```bash
deactivate
```

## Dependency Management

Install a new package:

```bash
pip install <package>
```

*Make sure the virtual environment is activated before installing new packages.*

Update the requirements file:

```bash
pip freeze > requirements.txt
```

## Environment Verification

Check the current Python interpreter:

```bash
which python3
```

Check the Python version:

```bash
python3 --version
```

List installed packages:

```bash
pip list
```

Check dependency compatibility:

```bash
pip check
```

## VS Code Configuration

To ensure that VS Code and Pylance recognize the packages installed in the virtual environment:

1. Open the Command Palette (`Ctrl + Shift + P`).
2. Select `Python: Select Interpreter`.
3. Select the `.venv/bin/python3` interpreter.
4. If the interpreter is not listed, select `Enter interpreter path...`.

To retrieve the interpreter's absolute path, activate the virtual environment and run:

```bash
which python3
```

Copy the returned path and paste it into VS Code.

If import warnings persist, reload VS Code using `Developer: Reload Window` from the Command Palette.

**Note:** VS Code saves the interpreter selection for the current workspace.