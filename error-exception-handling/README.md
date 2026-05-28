# Error and Exception Handling

Notes and runnable examples for Python errors and exceptions.

## Index

| File | Topics |
|------|--------|
| [error_exception_handling.py](error_exception_handling.py) | `try` / `except`, `else`, `finally`, multiple `except` blocks |

*Add a row here when you add a new `.py` file.*

---

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

## Adding a new file

1. Add the script in this folder (e.g. `custom_exceptions.py`).
2. Add a row to the **Index** table (file link + short topic list).
3. Copy the section below and fill it in.

```markdown
## your_new_file.py

**File:** [your_new_file.py](your_new_file.py)

**Overview:** One sentence on what this file teaches.

**Run:**

\`\`\`
C:\MyPC\personal\github\python\error-exception-handling>py your_new_file.py
\`\`\`

### Demos

#### `demo_name()`
* What it does.

**Output:**
\`\`\`
expected lines here
\`\`\`
```

Keep the same headings per file so the README stays easy to scan as it grows.
