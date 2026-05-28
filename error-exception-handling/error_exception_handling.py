def try_except():
    try:
        sum = 10 + '10'
    except:
        print("try_except - Error occured")
        
    print("continue try_except execution")
    
def try_except_else():
    try:
        sum = 10 + 10
    except:
        print("try_except - Error occured")
    else:
        print(f"try_except - No erorr occured. sum={sum}")
        
    print("continue try_except_else execution")

def separate_except_blocks():
    try:
        sum = 10 + 10
    except TypeError:
        print("try_except - TypeError - Error occured")
    except OSError:
        print("try_except - OSError - Error occured")
    except:
        print("try_except - Other Error occured")
    else:
        print(f"try_except - No erorr occured. sum={sum}")
        
    print("continue try_except_else execution")
    
def try_finally():
    try:
        sum = 10 + 10
    finally:
        print("try_finally- finally block")
        
if __name__ == "__main__":
    # try_except()
    # try_except_else()
    # separate_except_blocks()
    try_finally()