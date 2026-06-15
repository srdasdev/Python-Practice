
# *args (Non-keyword Arguments)

def add(*args):
    print(f"Type: {type(args)}")      # <class 'tuple'>
    print(f"Args: {args}")             # (1, 2, 3, 4, 5)
    return sum(args)

add(1, 2, 3, 4, 5)  # Returns 15

# **kwargs (Keyword Arguments)
def greet(**kwargs):
    print(f"Type: {type(kwargs)}")     # <class 'dict'>
    print(f"Kwargs: {kwargs}")         # {'name': 'John', 'age': 30}
    
greet(name="John", age=30, city="NYC")


# All keyword arguments are packed into a dictionary named kwargs
# Keys are the parameter names, values are what you passed
# Access them like a dict: kwargs['name'], kwargs['age'], etc.