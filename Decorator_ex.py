"""
Write different methods for addition,substraction,division,multiplication of number.
Write decoratoe which will call above methods only id
1.Only 2 input values are allowed
2.Both inputs should be of type integer
3.Both input values are positive integer only
"""

def add(a,b):
    print(a+b)

def substract(a,b):
    print(a-b)
def div(a,b):
    print(a/b)

def mul(a,b):
    print(a*b)

def decorator(fnc):
    def wrapper(a,b):
        if(isinstance(a, int) and isinstance(b, int) and a>0 and b>0):
            return fnc(a,b)
        else:
            return print("Enter int value")
    return wrapper


add = decorator(add)
add(4,4)
mul(2,2)




