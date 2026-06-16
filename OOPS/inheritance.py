"""
Definition: Child class inherits properties and methods from parent class (code reuse).

Real-World Analogy: A child inherits genes from parents — black hair, height, etc. Similarly, a child class inherits attributes and behaviors from a parent class.
"""

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
# animal = Animal()
# print(animal.speak())  # Output: Some sound
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!