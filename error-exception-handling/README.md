# Error and Exception Handling

Notes and runnable examples for Python errors and exceptions.

## Index

| Script | Documentation |
|--------|---------------|
| [error_exception_handling.py](error_exception_handling.py) | [error_exception_handling.py](#error_exception_handling) |
| [practice.py](practice.py) | [practice.py](#practice) |

---

<a id="error_exception_handling"></a>

## error_exception_handling.py

**File:** [error_exception_handling.py](error_exception_handling.py)

**Overview:** Small demos in one module. Uncomment the call you want in `if __name__ == "__main__":` before running.

**Run** (from this folder):

```
C:\MyPC\personal\github\python\error-exception-handling>py error_exception_handling.py
```

By default, `ask_for_input()` is called (interactive; enter a number when prompted).

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
* `finally` always runs.

**Output:**
```
try_finally- finally block
```

#### `ask_for_input()`
* Loops until the user enters a valid integer.
* `try`: reads input with `int(input(...))`.
* `except`: non-numeric input prints `Not a number, try again` and `continue` retries the loop.
* `else`: runs when conversion succeeds; prints the number and `break` exits the loop.
* `finally`: runs after every attempt (invalid or valid input).

**Output** (example: invalid input `abc`, then valid `42`):
```
Enter number: abc
Not a number, try again
Finally executed
Enter number: 42
Entered number: 42
Finally executed
```

---

<a id="practice"></a>

## practice.py

**File:** [practice.py](practice.py)

**Overview:** Practice script that catches exceptions inside a loop so one failure does not stop the rest.

**Run** (from this folder):

```
C:\MyPC\personal\github\python\error-exception-handling>py practice.py
```

### Demos

#### `method1()`
* Iterates over `['a', 'b', 'c']`.
* `try`: computes `i**2` for each item.
* `except`: strings cannot be squared with `**`; bare `except` prints `Exception {i}**2` and the loop continues to the next item.

**Output:**
```
Exception a**2
Exception b**2
Exception c**2
```

---
