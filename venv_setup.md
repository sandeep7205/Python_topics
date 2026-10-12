# 1. Python Virtual Environment (venv) Guide## 1. Setting Up the Virtual Environment
To create a new virtual environment, open your terminal, navigate to your project directory, and run the following command:

```powershell
python -m venv venv
```

Note: The second venv is the name of the folder where your virtual environment files will live. You can name it anything, but venv is the standard convention.
# 2. Activating the Virtual Environment
Before you can use the environment, you must activate it. The command depends on your operating system and the terminal type you are using.
## Windows

* PowerShell:
```powershell
venv\Scripts\Activate.ps1
```

(If you get a script execution error, run Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process first)
* Command Prompt (cmd):
```powershell
venv\Scripts\activate.bat
```
* Git Bash:
```powershell
source venv/Scripts/activate
```

## macOS / Linux

* Bash/Zsh Terminal:
```powershell
source venv/bin/activate
```

💡 How to know it worked: Once activated, you will see the name of your environment in parentheses (venv) at the very beginning of your terminal prompt line.

# 3. Installing Packages & Managing Dependencies
Once your virtual environment is active, any package you install will be contained entirely within this environment, keeping your global system clean.
## Installing a Specific Package
To install a single library (for example, requests), use:
```powershell
pip install requests
```
## Creating a requirements.txt File
To share your project with others or back up your dependencies, save a list of your installed packages to a text file:
```powershell
pip freeze > requirements.txt
```
## Installing from an Existing requirements.txt
If you are downloading a project that already has a list of dependencies, you can install all of them at once by running:
```powershell
pip install -r requirements.txt
```

## Verify
```powershell
pip list
```

# 4. Deactivating the Virtual Environment
When you are finished working on your project and want to return to your global system Python configuration, simply type this single command from any directory in your terminal:
```powershell
deactivate
```