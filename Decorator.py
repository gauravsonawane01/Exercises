"""
Simple decorator
"""
def div(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):

        if a<b:
            return False
        else :
            return func(a,b)

    return inner

div = smart_div(div)

div(4,2)


#Decorator with paramater

import random

def power_of(exponent):
    def decorator(fnc):
        def inner():
            return fnc()**exponent
        return inner
    return decorator

@power_of(3)
def random_odd_digit():
    return random.choice([1,2,3,4])

print(random_odd_digit())
