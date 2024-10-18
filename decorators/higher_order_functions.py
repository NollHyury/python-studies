#Higher-Order Functions
def loud(func):
    def wrapper():
        return func().upper() + "!!!"
    return wrapper

def greet():
    return "Hello, there"

#HOFs
#-> Take one or more functions as their arguments, or
#-> return a function as its result

loud_greet = loud(greet)
print(loud_greet())

def double_add(func, *args):
    def wrapper():
        return (func(args)) * 2
    return wrapper


double = double_add(sum,5,2)
print(double())


#First Class Functions:
def loud_greeting(name):
    return f"HELLO {name.upper()}!"

def quiet_greeting(name):
    return f"Hello {name}..."

from typing import Callable
def greet(name: str, greeting: Callable[[str],str]) -> str:
    return greeting(name)

print(greet("Andy", loud_greeting))

