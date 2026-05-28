# Unit Testing

Notes on static analysis and automated tests in Python.

## Index

| Script / Topic | Documentation |
|----------------|---------------|
| pylint | [pylint](#pylint) |
| unittest | [unittest](#unittest) |
| [cap.py](cap.py) | [cap.py](#cap) |
| [test_cap.py](test_cap.py) | [test_cap.py](#test_cap) |

---

<a id="pylint"></a>

## pylint

**Overview:**

* Static analysis tool that inspects Python source for errors, style issues, and code smells without running the program.
* Reports messages by category (convention, refactor, warning, error, fatal) and can assign an overall score to a module or package.
* Command to install pylint: `pip install pylint`
* Run from the project or module folder with `py -m pylint <module_or_path>`.
* By default pylint uses `PEP 8` style guide.

**Example** (from this folder):

```
C:\MyPC\personal\github\python\unit-testing>py -m pylint cap.py
```

---

<a id="unittest"></a>

## unittest

**Overview:**

* Built-in testing framework in the standard library; import with `import unittest` (no extra install).
* Tests live in classes that subclass `unittest.TestCase`, with methods named `test_*` that use assertions such as `assertEqual` and `assertTrue`.
* Run all tests in a file or folder with `py -m unittest <test_module>` or `py -m unittest discover` from the directory that contains your tests.

---

<a id="cap"></a>

## cap.py

**File:** [cap.py](cap.py)

**Overview:** Small module with one function, `cap_text(text)`, used as the code under test for the unittest example in [test_cap.py](test_cap.py).

### `cap_text(text)`

* Takes a string `text` and returns it with each word capitalized using `str.title()`.
* Single word: `"python"` → `"Python"`.
* Multiple words: `"python hello world"` → `"Python Hello World"`.

---

<a id="test_cap"></a>

## test_cap.py

**File:** [test_cap.py](test_cap.py)

**Overview:** Example `unittest` module that imports [cap.py](cap.py) and checks `cap_text()` with `assertEqual`.

**Run** (from this folder):

```
C:\MyPC\personal\github\python\unit-testing>py test_cap.py
```

Or with the unittest runner:

```
C:\MyPC\personal\github\python\unit-testing>py -m unittest test_cap -v
```

### Tests

#### `test_one_word()`
* Sets `text = "python"` and calls `cap.cap_text(text)`.
* Asserts the result equals `"Python"`.

#### `test_multiple_words()`
* Sets `text = "python hello world"` and calls `cap.cap_text(text)`.
* Asserts the result equals `"Python Hello World"`.

**Output:**

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

With `-v`, each test name is printed (e.g. `test_one_word`, `test_multiple_words`) before the summary.

---
