# Error and Exception Handling

Notes and runnable examples for Python errors and exceptions.

## Index

| Script | Documentation | Topics |
|--------|---------------|--------|
| [error_exception_handling.py](error_exception_handling.py) | [error_exception_handling.py](#error_exception_handling) | `try` / `except`, `else`, `finally`, multiple `except` blocks |

---

<a id="error_exception_handling"></a>

## error_exception_handling.py

**File:** [error_exception_handling.py](error_exception_handling.py)

**Overview:** Four small demos in one module. Uncomment the call you want in `if __name__ == "__main__":` before running.

**Run** (from this folder):

```
C:\MyPC\personal\github\python\error-exception-handling>py error_exception_handling.py
```

By default, only `try_finally()` is called.

### Demos

#### `try_except()`
* Invalid addition (`10 + '10'`) raises `TypeError`.
* Bare `except:` catches it; execution continues after the block.

**Output:**
```
try_except - Error occured
continue try_except execution
```

#### `try_except_else()`
* Valid addition (`10 + 10`); no exception.
* `else` runs only when `try` succeeds.

**Output:**
```
try_except - No erorr occured. sum=20
continue try_except_else execution
```

#### `separate_except_blocks()`
* Handlers for `TypeError`, `OSError`, then a catch-all `except`.
* With valid input, `else` prints the sum.

**Output:**
```
try_except - No erorr occured. sum=20
continue try_except_else execution
```

#### `try_finally()`
* `finally` always runs (default in `__main__`).

**Output:**
```
try_finally- finally block
```

---
