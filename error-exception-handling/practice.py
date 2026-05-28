def method1():
    list1 = ['a', 'b', 'c']
    for i in list1:
        try:
            result = i**2
        except:
            print(f"Exception {i}**2")

if __name__ == "__main__":
    method1()