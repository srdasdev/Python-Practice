"""
Q: can you achieve polymorphism without inheritance in python?

A: Yes, you can achieve polymorphism without inheritance in Python through a concept called "duck typing." Duck typing is a programming style that does not look at an object's type to determine if it has the right behavior; instead, it looks at the presence of certain methods and properties. If an object has the necessary methods and properties, it can be used in place of another object, regardless of its actual type.
"""

class Car:
    def start(self):
        return "car started"
class Bike:
    def start(self):
        return "bike started"

def start_vehicle(vehicle):
    return vehicle.start()

# car = Car()
# bike = Bike()

# print(start_vehicle(car))  # Output: car started
# print(start_vehicle(bike))  # Output: bike started


for vehicle in [Car(), Bike()]:
    print(vehicle.start())  # Output: car started, bike started



#Another example of duck typing:

class SpecialString:
    def __len__(self):
        return 42

string = SpecialString()
print(len(string)) # Output: 42, even though SpecialString is not a built-in string type, it can be used with len() because it implements the __len__ method.
