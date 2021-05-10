def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    '''
     this just takes one argument

    '''
    print(f"arg1: {arg1}")

def print_none():
    '''
     this one takes no arguments

    '''
    print("I got nothin'.")
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

# print(print_one.__doc__)
