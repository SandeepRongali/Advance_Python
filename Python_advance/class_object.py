
# Class: A blueprint for creating objects.
#
# Object: An instance of a class.

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

# Create an object
dog1 = Dog("Tommy")
dog1.bark()