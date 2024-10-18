def simple_decorator(func):
    def wrapper():
        print("Before function execution")
        result = func()
        print("After function execution")
        return result
    return wrapper

@simple_decorator
def greet():
    return "Hello, world!"

greet()

def simple_decorator(func):
    def wrapper(name):
        print("Before function execution")
        result = func(name)
        print("After function execution")
        return result
    return wrapper

@simple_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("Andy"))


def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result
    return wrapper

@simple_decorator
def greet(name, surname):
    return f"Hello, {name} {surname}!"

print(greet("Andy", "Noll"))


#-------- Logger challenge
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function: {func.__name__} returned: {result}")
        return result
    return wrapper

@logger
def calculate_sum(a,b):
    return a + b

calculate_sum(3,5)