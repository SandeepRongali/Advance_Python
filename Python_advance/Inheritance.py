# Allows a class to use methods and properties of another class (reusability).

class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):  # Inherits from Animal
    def speak(self):
        print("Meow")

c = Cat()
c.speak()

