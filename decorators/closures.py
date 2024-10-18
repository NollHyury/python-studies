#Closures
# At its core, a closure in Python is a function object that
# has access to variables from a passed scope or an outside score

def outer(x):
    def inner(y):
        return x + y
    return inner

closure = outer(10)
print(closure)
print(closure(10))
print(closure(5))

def make_multipler(x):
    def multipler(n):
        return x * n
    return multipler

time_two = make_multipler(2)
time_three = make_multipler(3)

print(time_two(2))
print(time_three(7))

#data hiding & encapsulation
# may should I try use this approach using Web Scrapping, e.g. keep
# auth token saved in past context of clouse function

def create_counter(start=0):
    count = [start]
    def counter():
        count[0] += 1
        return count[0]
    return counter

counter1 = create_counter()
counter1()
counter1()
print(counter1())