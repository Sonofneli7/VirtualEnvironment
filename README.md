# Python Virtual Environment Setup in VS Code

This guide will help you set up and use a Python Virtual Environment (venv) within Visual Studio Code, one of the most popular IDEs for Python development.

## Prerequisites
Before starting, make sure you have the following installed:
- Python (preferably version 3.12.4 or higher)
- Visual Studio Code (VS Code)
- Python extension for VS Code

## Steps for Setting Up a Virtual Environment in VS Code

### 1. Install Python Extension in VS Code
To use Python in VS Code, ensure the Python extension is installed:
1. Open **Extensions** in the file explorer sidebar.
2. Type `Python` in the search bar.
3. Install the extension titled **Python** by Microsoft.

### 2. Navigate to Your Project Folder
1. Open VS Code and navigate to your desired project folder. For example, a folder named `python-programming`.

### 3. Select the Python Interpreter
VS Code requires you to select the Python interpreter to use the virtual environment.

#### For Windows/Linux:
1. Open the Command Palette by pressing `Ctrl + Shift + P`.
2. Type **Python: Select Interpreter**.
3. Choose the interpreter (look for something like `.\\myenv\\Scripts\\python.exe`).

#### For macOS:
1. Open the Command Palette by pressing `Cmd + Shift + P`.
2. Type **Python: Select Interpreter**.
3. Choose the interpreter (look for something like `./myenv/bin/python`).

If you're unsure which interpreter to choose, select the **Recommended** one.

### 4. Verify Your Setup
To ensure that your virtual environment is correctly set up, follow these steps:
1. Open a terminal within VS Code by navigating to **Terminal > New Terminal**.
2. Check your Python version by running:
   ```bash
   python --version

