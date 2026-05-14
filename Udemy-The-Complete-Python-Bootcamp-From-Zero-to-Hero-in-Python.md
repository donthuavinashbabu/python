# Notes
* [slides](https://drive.google.com/drive/folders/1xzX9OGucdIrMWVGeMwifNyttcjds81x1?usp=sharing)

---
# Course content
* Introduction
* Python 2 vs Pytho 3
* Python setup - Environment selection, Jupytor notebook selection
* data structures - numbers, strings, lists, tuples, sets, dictionaries, boolean, files
* Comparison operators
* Python statements - if, else, elif, for, while, range, list comparison
* Methods and functions
* First milestone project
* OOP - classes, object, methods, inheritance
* Error and exception handling
* Second milestone project
* Modules and packages
* Built-in functions - map, reduce, filter, zip, enumerate, all and any
* Decorators
* Python generators
* Final capstone project
* Advanced python modules

## Why python
* Created in 1990 by `Guido Van Rassum`
* Python 3 released in 2008
* Readability, ease of use

## Installation
* Search in google - `anaconda downloads`

## Data types
* int
* float
* str - Can you both single quote or double quote
* bool
* list
* tup - Tuples. ordered `immutable` sequence of objects. Ex: (10, "hello", 123.456)
* set - unordered unique elements
* dict - Dictionaries. unordered key-value pairs. Similar to `HashMap`. Ex: {"key1": "value1", "key2": "value2"}
* Python supports `Dynamic Typing`, means we can reassign variables to different data types. Example below
```
my_dog = 2
my_dog = ["a", "b"]
my_dog = "c"
```
* use `type()` to check type of any variable
```
type(my_dog)
```

## Strings
* Length of string
```
len("hello")
```
* Get char at
```
myString = "Hello World"
hChar = myString[0] # H
```
* Get char at from last
```
myString = "Hello World"
hChar = myString[-1] # d
```
* substring
```
myString = "abcdefghijkl"
myString[2:8] # index 2 to 8, excluding index 8
myString[2:] # from index 2 to end of string
```
* step size
```
myString = "abcdefghijkl"
# step size - 2. Means jump in 2 steps
myString[::2] # acegik
myString[2:9:2] # index from 2 to 9 with step size 2
```
* Reverse string
```
myString = "abcdefghijkl"
reverseString = myString[::-1] # starting from last all the way to start with step size 1
```
* Concat
```
str1 = "a"
str2 = "b"
str3 = str1 + str3

str4 = "c"
# cccccccccc
str5 = str4 * 10
```
* upper
```
str1 = "hello"
str2 = str1.upper()
```
* split
```
str1 = "hello world"
# ["hello", "world"]. Default on white space
str2 = str1.split()
str3 = str1.split("o") # split by o
```
* format
```
"This is even number: {}, this is odd number: {}, this is prime number: {}".format("2", "3", "5")

# Welcome to python python python
"Welcome to {0} {0} {0}".format("python", "java", "aws")

# Welcome to aws java python
"Welcome to {a} {j} {p}".format(p="python", j="java", a="aws")
```
* float formatting
```
result = 100/777
# total 10 digits with 5 decimals
print("result is {r:10.5f}".format(r=result))
print("result is {r:1.5f}".format(r=result))
```
* another syntax for format using `f` string
```
greeting = "hello"

# all below are same
"{} world".format(greeting)
"{g} world".format(g=greeting)
f"{greeting} world"
```