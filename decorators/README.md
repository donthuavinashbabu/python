# Decorators

* Similar to Annotations in Java
* Used to add additional functionality to a function
* Used to add logging, authentication, etc.

Notes and runnable examples for Python decorators.

## Index

| Script | Documentation |
|--------|---------------|
| [decorators.py](decorators.py) | [decorators.py](#decorators) |

---

<a id="decorators"></a>

## decorators.py

**File:** [decorators.py](decorators.py)

**Overview:** Step-by-step examples that build up to decorators: assigning functions to variables, passing functions as arguments, wrapping a function manually, and applying a decorator with `@` syntax.

**Run** (from this folder):

```
C:\MyPC\personal\github\python\decorators>py decorators.py
```

**Output:**

```
method1
method1
Stared function3
Inside function2
Completed function3
Some extra code before original function
Inside function4
Some extra code after original function
Some extra code before original function
Inside function5
Some extra code after original function
```

### Functions as first-class objects

Functions can be assigned to variables and called through those variables, just like any other object.

```python
def function1():
    return "method1"

myFunction1 = function1
print(function1())    # method1
print(myFunction1())  # method1
```

Both calls invoke the same function.

### Higher-order functions

A function can accept another function as an argument and call it.

```python
def function2():
    return "Inside function2"

def function3(myFunc):
    print("Stared function3")
    print(myFunc())
    print("Completed function3")

function3(function2)
```

`function3` runs code before and after calling the function passed in.

### Manual decorator application

A **decorator** is a function that takes a function, wraps it with extra behavior, and returns the wrapper.

```python
def decorator1(my_func):
    def wrap_func():
        print("Some extra code before original function")
        my_func()
        print("Some extra code after original function")
    return wrap_func

def function4():
    print("Inside function4")

decorated_function = decorator1(function4)
decorated_function()
```

`decorator1(function4)` returns `wrap_func`. Calling `decorated_function()` runs the wrapper, which executes the extra code around `function4`.

### `@` syntax

The `@` syntax applies a decorator at definition time. These two forms are equivalent:

```python
@decorator1
def function5():
    print("Inside function5")

function5()
```

is the same as:

```python
def function5():
    print("Inside function5")

function5 = decorator1(function5)
function5()
```

Both `function4` (manual) and `function5` (`@decorator1`) produce the same before/after wrapper output.
