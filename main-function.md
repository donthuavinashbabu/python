# Main Function

* Files:
  * [main_function.py](main_function.py)
  * [main_function_2.py](main_function_2.py)
* `main_function.py`:
  * Prints module name and greeting.
  * Defines `method1()` and `method2()`.
  * Executes the main block only when run directly (`if __name__ == "__main__":`).
  * Run:
```
C:\MyPC\personal\github\python>py main_function.py
```
  * Output:
```
__name__:  __main__
Hello world
Running main function
method1
method2
```
* `main_function_2.py`:
  * Imports `method1()` and `method2()` from `main_function.py`.
  * Importing `main_function` runs top-level statements in `main_function.py`, so its `print` lines appear first.
  * Then `main_function_2.py` prints its own module name and greeting.
  * In its main block, it runs inherited methods plus `method3()` and `method4()`.
  * Run:
```
C:\MyPC\personal\github\python>py main_function_2.py
```
  * Output:
```
__name__:  main_function
Hello world
__name__:  __main__
Hello world 2
Running main function2
method1
method2
method3
method4
```
