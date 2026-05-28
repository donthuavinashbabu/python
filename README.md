# Python
* [Python documentation](https://docs.python.org/3/)
* [Notes](notes.md)
* [Udemy-The-Complete-Python-Bootcamp-From-Zero-to-Hero-in-Python](Udemy-The-Complete-Python-Bootcamp-From-Zero-to-Hero-in-Python.md)
---
# Practice
* Basic Practice: http://codingbat.com/python
* More Mathematical (and Harder) Practice: https://projecteuler.net/archives
* List of Practice Problems: http://www.codeabbey.com/index/task_list
* A SubReddit Devoted to Daily Practice Problems: https://www.reddit.com/r/dailyprogrammer
* A very tricky website with very few hints and touch problems (Not for beginners but still interesting) - http://www.pythonchallenge.com/
---
# No install python labs
* https://colab.research.google.com/
* https://jupyter.org/try
---
## Example and Practice
* [Hello World](basics/helloWorld.ipynb)
* [Conditions](basics/conditions.ipynb)
* [Loops](basics/loops.ipynb)
* [File IO](basics/fileIO.ipynb)
* [Methods and Functions](basics/methodsFunctions.ipynb)
* [Lists](basics/lists.ipynb)
* [Practice Examples](basics/practice.ipynb)
* [Oops concepts](basics/oop.ipynb)
* [Practice Examples](basics/practice-2.ipynb)
* [Python Package Index](basics/pypi-python-package-index.ipynb)
* [Packages and Modules](packages-modules/README.md)
* [Error and Exception Handling](error-exception-handling/README.md)
* [Unit Testing](unit-testing/README.md)
---
# main function
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