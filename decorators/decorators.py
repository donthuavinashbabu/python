# assign function to variable and execute
def function1():
    return "method1"
myFunction1 = function1
print(function1())
print(myFunction1())

def function2():
    return "Inside function2"

def function3(myFunc):
    print("Stared function3")
    print(myFunc())
    print("Completed function3")
function3(function2)

# decorator
def decorator1(my_func):
    
    def wrap_func():
        print("Some extra code before original function")
        my_func()
        print("Some extra code after original function")
    
    return wrap_func

def function4():
    print("Inside function4")

# Applying decorator on function4
decorated_function = decorator1(function4)
decorated_function()

# applying decorator with @ syntax. Same as function4 above
@decorator1
def function5():
    print("Inside function5")
function5()