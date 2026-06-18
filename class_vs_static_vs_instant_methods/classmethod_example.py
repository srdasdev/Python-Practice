class Pizza:
    default_size="medium"
    def __init__(self, toppings):
        self.toppings=toppings #instance attribute

    # 1. Instance method
    def describe(self):
        return f"A {self.default_size} pizza with {', '.join(self.toppings)}"
    
    # 2. Class method
    @classmethod
    def margherita(cls):
        return cls(["cheese", "tomato"])  # Using class method to create a default pizza instance
    
# 3. Static method
    @staticmethod
    def is_valid_topping(topping):
        valid_toppings = ["cheese", "tomato", "pepperoni", "mushrooms"]
        return topping in valid_toppings
    
p = Pizza(["ham"])
print(p.describe())  # Output: A medium pizza with ham

p2= Pizza.margherita()
print(p2.describe())  # Output: A medium pizza with cheese, tomato

print(Pizza.is_valid_topping("cheese"))  # Output: True