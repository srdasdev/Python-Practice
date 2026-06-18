class Dog:
    def __init__(self):
        self.name = "Buddy"
    def bark(self):
        return "Woof!"



d = Dog()
print(d) # Output: <__main__.Dog object at 0x...> which is ambigous and not very informative.

# so use repr() method to get a more informative string representation of the object.

class Dog:
    def __init__(self):
        self.name = "Buddy"
    def bark(self):
        return "Woof!"
    def __repr__(self):
        return f"Dog(name={self.name})"
    
d = Dog()
print(d) 


"""
Here's __str__ vs __repr__ side by side. They both turn an object into a string, but they answer two different questions.

__repr__ → "What is this object, precisely?" (for developers — debugging, logging, the REPL)
__str__ → "How do I show this to a human?" (for end users — print, UI, reports)
"""



class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    # Developer-facing: unambiguous, looks like code to rebuild it
    def __repr__(self):
        return f"Temperature(celsius={self.celsius!r})"

    # User-facing: pretty, readable
    def __str__(self):
        return f"{self.celsius}°C"

t = Temperature(25)

print(t)        # 25°C                      ← print() uses __str__
str(t)          # '25°C'                    ← str() uses __str__
t               # Temperature(celsius=25)   ← REPL uses __repr__
repr(t)         # 'Temperature(celsius=25)' ← repr() uses __repr__
print([t])      # [Temperature(celsius=25)] ← containers ALWAYS use __repr__
