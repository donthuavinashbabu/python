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
