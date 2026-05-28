from main_function import method1, method2

print("__name__: ", __name__)
print("Hello world 2")

def method3():
    print("method3")

def method4():
    print("method4")

if __name__ == "__main__":
    print("Running main function2")
    method1()
    method2()
    method3()
    method4()