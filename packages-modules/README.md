# Python packages and modules
* Created 2 files - [animal.py](animal.py), [dog.py](dog.py)
* Import [animal.py](animal.py) in [dog.py](dog.py)
* Execute [dog.py](dog.py) using following commands. All belows commands are same:
```
C:\MyPC\personal\bitbucket\work\study\python\packages-modules>python dog.py
I am an animal
```
```
C:\MyPC\personal\bitbucket\work\study\python\packages-modules>py dog.py
I am an animal
```
```
C:\MyPC\personal\bitbucket\work\study\python\packages-modules>uv run python dog.py
I am an animal
```
```
C:\MyPC\personal\bitbucket\work\study\python\packages-modules>uv run py dog.py
I am an animal
```

---
# Modules and Packages
* File: [use_packages.py](use_packages.py)
* Demonstrates importing from package and subpackage:
  * `from MainPackage import main_package`
  * `from MainPackage.SubPackage1 import sub_package_1, sub_report2`
* Calls three functions:
  * `main_package.main_report()`
  * `sub_package_1.sub_report1()`
  * `sub_report2()`
* `sub_report2` can be imported directly from `SubPackage1` because it is re-exported in `SubPackage1/__init__.py`.
* If `sub_report2` is now re-exported in `SubPackage1/__init__.py`, import it directly from the module:
  * `from MainPackage.SubPackage1.sub_package_1 import sub_report2`
* Common `ImportError` checks:
  * Run the command from the `packages-modules` directory so `MainPackage` is on Python path.
  * Ensure `MainPackage/__init__.py` and `MainPackage/SubPackage1/__init__.py` exist.
  * Verify function name is `sub_report2` and it is defined in `sub_package_1.py`.
* Run command:
```
C:\MyPC\personal\github\python\packages-modules>py use_packages.py
```
* Expected output:
```
I am MainPackage.main_report
I am SubPackage1.sub_report1
I am SubPackage1.sub_report2
```