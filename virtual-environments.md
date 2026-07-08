# Virtual Environments

A virtual environment is an isolated Python environment that allows you to manage dependencies for each project separately. It prevents conflicts between projects and avoids affecting the system-wide Python installation. Tools like venv or virtualenv are commonly used to create them.

## Why do we need a Virtual Environment
* Avoid Dependency Conflicts: Different projects may require different versions of the same library (e.g., Django 4.0 vs 4.1).
* Isolate Project Environments: Keeps each project’s packages and settings separate from others and from the system Python.
* Simplifies Project Management: Makes it easier to manage and replicate project-specific setups.
* Prevents System Interference: Avoids accidentally modifying or breaking the global Python environment.
* Enables Reproducibility: Ensures consistent behavior across development, testing and deployment environments.
* When and Where to use a Virtual Environment?
* A virtual environment should be used for every Python project. By default, all Python projects share the same location to store packages. This can cause problems if two projects need different versions of the same package, like Django. A virtual environment solves this by creating a separate space for each project’s packages, so they don’t interfere with each other. It’s basically a folder with its own Python setup. Using a virtual environment helps avoid conflicts and keeps your projects clean and organized.

## How to Create a Virtual Environment in Python
* We use the virtualenv module to create isolated environments. It creates a folder with all necessary executables for the project.

---
* A virtual environment is an isolated Python installation for a project. Packages installed with `pip` while the environment is active stay inside that project folder instead of affecting your system Python.

## Create a virtual environment

From the folder where you want the project:

```
C:\MyPC\personal\study\python>python -m venv project-1
```

Can give multiple folder names
```
python -m venv project-3 project-4
```

This creates a `project-1` directory containing its own Python interpreter and `pip`.

## Activate the environment

On Windows (Command Prompt or PowerShell):

```
C:\MyPC\personal\study\python>cd project-1

C:\MyPC\personal\study\python\project-1>Scripts\activate
```

Your prompt shows the environment name in parentheses when it is active:

```
(project-1) C:\MyPC\personal\study\python\project-1>
```

Common activation commands by platform and shell:

| Platform | Shell | Command to activate virtual environment |
| --- | --- | --- |
| POSIX | bash/zsh | `$ source <venv>/bin/activate` |
| POSIX | fish | `$ source <venv>/bin/activate.fish` |
| POSIX | csh/tcsh | `$ source <venv>/bin/activate.csh` |
| POSIX | pwsh | `$ <venv>/bin/Activate.ps1` |
| Windows | cmd.exe | `C:\> <venv>\Scripts\activate.bat` |
| Windows | PowerShell | `PS C:\> <venv>\Scripts\Activate.ps1` |

## Install packages

With the environment active, install packages into it:

```
(project-1) C:\MyPC\personal\study\python\project-1>pip install cowsay
```

Example output:

```
Collecting cowsay
  Using cached cowsay-6.1-py3-none-any.whl.metadata (5.6 kB)
Using cached cowsay-6.1-py3-none-any.whl (25 kB)
Installing collected packages: cowsay
Successfully installed cowsay-6.1
```

## Run a script

Example `cowsay-test.py`:

```python
import cowsay

cowsay.cow("Good mooooorning")
```

Run it while the environment is active:

```
(project-1) C:\MyPC\personal\study\python\project-1>py cowsay-test.py
```

Output:

```
  ________________
| Good mooooorning |
  ================
                \
                 \
                   ^__^
                   (oo)\_______
                   (__)\       )\/\
                       ||----w |
                       ||     ||
```

## Deactivate

When you are done, leave the virtual environment:

```
(project-1) C:\MyPC\personal\study\python\project-1>deactivate
```

Your prompt returns to normal and `pip install` will target system Python again unless you activate another environment.

---
To create a Python virtual environment, you don’t actually use pip directly — you use Python’s built‑in venv module. Here’s the command:
```
python -m venv myenv
```

Breakdown:
- `python` → Runs the Python interpreter.
- `-m venv` → Calls the venv module to create a virtual environment.
- `myenv` → The name of the folder where the environment will be created (you can choose any name).

After creating it, you activate the environment:
Windows (Command Prompt):
```
myenv\Scripts\activate
```
macOS/Linux (bash/zsh):
```
source myenv/bin/activate
```
Then you can use pip inside that environment to install packages:
```
pip install <package-name>
```
If you meant installing virtualenv using pip (an alternative to venv), the command would be:
```
pip install virtualenv
```
And then:
```
virtualenv myenv
```

---
## difference between `venv` and `virtualenv`
Use venv if you’re working with Python 3.3+ — it’s built-in, simple, and requires no installation. Use virtualenv if you need compatibility with Python 2, faster environment creation, or advanced features. For most modern projects, venv is the recommended choice.

# 🔑 Key Differences Between `venv` and `virtualenv`

**Use `venv` if you’re working with Python 3.3+ — it’s built-in, simple, and requires no installation.  
Use `virtualenv` if you need compatibility with Python 2, faster environment creation, or advanced features.  
For most modern projects, `venv` is the recommended choice.**

## 📊 Comparison Table

| Feature | **venv** | **virtualenv** |
|---------|-----------|----------------|
| **Availability** | Built into Python (≥3.3), no installation needed | Third-party package, install via `pip install virtualenv` |
| **Python Version Support** | Python 3.3+ only | Supports Python 2 and 3 |
| **Speed** | Slightly slower (installs pip from embedded wheel) | Faster (caches pip wheels, optimized creation) |
| **Flexibility** | Basic isolation only | More configurable, supports plugins and wrappers |
| **Use Case** | Standard choice for modern Python projects | Legacy projects, CI/CD pipelines needing speed, or when plugins are required |
| **Command Example** | `python -m venv myenv` | `virtualenv myenv` |

## 📌 Practical Guidance
- **For new projects (Python 3.3+)** → Use **`venv`**.  
- **For legacy projects (Python 2)** → Use **`virtualenv`**.  
- **For CI/CD or rapid environment creation** → `virtualenv` may be faster, but modern alternatives like **uv** or **Poetry** are even better.  
- **For dependency management** → Pair `venv` with tools like **pip-tools**, **Poetry**, or **PDM**.  

## ⚠️ Risks & Trade-offs
- **Using `venv` in Python 2 projects** → Not possible.  
- **Using `virtualenv` unnecessarily** → Adds extra dependency.  
- **Mixing environments** → Avoid switching between `venv` and `virtualenv` in the same project.  

## ✅ Recommendation
Since you’re working with **modern Python (3.x)**, use **`venv`** for simplicity and standardization.  
Reserve **`virtualenv`** only for older projects or specialized workflows.

---
## Difference between venv, virtualenv and poetry

# ⚖️ Comparing `venv`, `virtualenv`, and Poetry

## 📊 Comparison Table

| Feature | **venv** | **virtualenv** | **Poetry** |
|---------|-----------|----------------|------------|
| **Availability** | Built into Python (≥3.3) | Third-party (`pip install virtualenv`) | Third-party (`pip install poetry`) |
| **Python Version Support** | Python 3.3+ only | Python 2 & 3 | Python 3.7+ (modern focus) |
| **Purpose** | Create isolated environments | Create isolated environments (legacy + faster) | Manage environments **and** dependencies |
| **Speed** | Moderate | Faster (caches pip wheels) | Moderate (focus on reproducibility) |
| **Flexibility** | Basic isolation | Plugins, wrappers, more options | Handles dependencies, lock files, publishing |
| **Dependency Management** | Manual via `pip install` | Manual via `pip install` | Built-in (`pyproject.toml`, `poetry.lock`) |
| **Use Case** | Standard for modern Python projects | Legacy projects, CI/CD pipelines | Full project management (env + deps + publishing) |
| **Command Example** | `python -m venv myenv` | `virtualenv myenv` | `poetry init` → `poetry install` |

## 📌 Practical Guidance
- **Use `venv`** → For simple, modern Python projects where you just need isolation.  
- **Use `virtualenv`** → For legacy Python 2 projects or when speed/customization is critical.  
- **Use Poetry** → For modern projects needing **dependency management, reproducibility, and publishing**.  

## ✅ Recommendation
- For **quick isolation** → `venv`  
- For **legacy or CI/CD speed** → `virtualenv`  
- For **full project lifecycle management** → **Poetry** (increasingly popular in modern Python ecosystems).

---

## 🚀 Step-by-Step Workflow with Poetry

### Poetry is a modern tool for managing **virtual environments, dependencies, and publishing** in Python projects.

- Install Poetry
```
pip install poetry
```

- Initialize a New Project
- Creates a pyproject.toml file
- Interactive prompts let you define project metadata and dependencies
```
poetry init
```

- Add Dependencies
- Adds packages to `pyproject.toml`
- Automatically updates `poetry.lock` for reproducibility
```
poetry add requests
poetry add flask
```

- Create & Activate Virtual Environment
- Poetry automatically manages environments
- Activates the virtual environment
- All subsequent commands run inside it
```
poetry shell
```

- Install Dependencies
- Installs all dependencies listed in `pyproject.toml`
- Uses `poetry.lock` to ensure consistent versions
```
poetry install
```

- Run Your Project
- Runs scripts inside the Poetry-managed environment
```
poetry run python app.py
```

- Publish Your Package
- Builds source and wheel distributions
- Publishes to PyPI or a private repository
```
poetry build
poetry publish
```

## Summary
- venv → Simple isolation.
- virtualenv → Legacy + faster creation.
- Poetry → Full project lifecycle: environments, dependencies, reproducibility, publishing
