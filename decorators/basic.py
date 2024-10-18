#Basic introduction to decorators

def fry():
    return "Frying the food!"

def grill():
    return "Grilling the food!"

def boil():
    return "Boiling the food!"

# '@' - Pie decorator syntax
def seasoning(chef):
    def wrapper():
        print("Adding some salt and pepper!")
        return chef()
    return wrapper

@seasoning
def fry():
    return "Frying the food!"

@seasoning
def grill():
    return "Grilling the food!"


def boil():
    return "Boiling the food!"


print(fry())
print(boil())