"""Definition: Show only essential features, hide complexity.

Real-World Analogy: A smartphone — you tap an icon to call, don't see the complex radio signal processing."""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass #Define contract for starting the vehicle no implementation

    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        return "Car is starting with a key."

    def stop(self):
        return "Car is stopping."


class Bike(Vehicle):
    def start(self):
        return "Bike is starting with a button."

    def stop(self):
        return "Bike is stopping."
# vehicle = Vehicle()  # This will raise an error because we cannot instantiate an abstract class
car = Car()
bike = Bike()
print(car.start())  # Output: Car is starting with a key.
print(bike.start())  # Output: Bike is starting with a button.