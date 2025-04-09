# Hiding unnecessary details and only showing essential parts.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started!")

my_car = Car()
my_car.start_engine()
