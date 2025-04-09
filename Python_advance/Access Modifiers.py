# Used to control access to class variables and methods.
#
#
# Public	name	Accessible from anywhere
# Protected	_name	Accessible within class and subclasses
# Private	__name	Cannot be accessed directly from outside

class Person:
    def __init__(self):
        self.name = "Alice"       # Public
        self._age = 25            # Protected
        self.__ssn = "123-45-6789"  # Private

    def get_ssn(self):
        return self.__ssn

p = Person()
print(p.name)
print(p._age)
# print(p.__ssn)  Error: private
print(p.get_ssn())


# Public and protected variables can be accessed.
#
# Private variables can't be accessed directly (they are "name mangled").