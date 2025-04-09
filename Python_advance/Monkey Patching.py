# Changing the behavior of a class or function at runtime.

class Greet:
    def say_hello(self):
        print("Hello!")

g = Greet()
g.say_hello()

# Monkey patch: change say_hello method
def new_hello(self):
    print("Hi there!")

Greet.say_hello = new_hello

g.say_hello()

# We changed the method say_hello after the object was created — that’s monkey patching.