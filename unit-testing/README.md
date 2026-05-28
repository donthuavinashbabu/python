# Unit Testing

Notes on static analysis and automated tests in Python.

## Index

| Topic | Documentation |
|-------|---------------|
| pylint | [pylint](#pylint) |
| unittest | [unittest](#unittest) |

---

<a id="pylint"></a>

## pylint

**Overview:**

* Static analysis tool that inspects Python source for errors, style issues, and code smells without running the program.
* Reports messages by category (convention, refactor, warning, error, fatal) and can assign an overall score to a module or package.
* Run from the project or module folder with `py -m pylint <module_or_path>`.

---

<a id="unittest"></a>

## unittest

**Overview:**

* Built-in testing framework in the standard library; import with `import unittest` (no extra install).
* Tests live in classes that subclass `unittest.TestCase`, with methods named `test_*` that use assertions such as `assertEqual` and `assertTrue`.
* Run all tests in a file or folder with `py -m unittest <test_module>` or `py -m unittest discover` from the directory that contains your tests.

---
