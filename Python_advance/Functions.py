# Example 1: Simple function
def greet():
    print("Hello!")

greet()

# Example 2: Function with parameters
def add(a, b):
    return a + b
data =3
flight = 5
print(add(data, flight))

# Example 3: Function with default value
def welcome(name="Guest"):
    print(f"Welcome, {name}!")

welcome()
welcome("Alex")

def add(a, b = 5 ):
    return a + b
data =3

print(add(data))

def add(a, b=6):
    return a + b
data =3
flight = 5
print(add(data, flight))
