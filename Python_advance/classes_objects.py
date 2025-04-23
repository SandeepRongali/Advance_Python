# Example 1: Define a class
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

# Example 2: Create instances
dog1 = Dog("Rex")
dog1.bark()  # Rex says woof!

# Example 3: Adding methods
class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return 3.1416 * self.radius**2

c = Circle(5)
print(c.area())  # 78.54
