"""
What is functools?

functools is a standard library module providing higher-order functions — functions that operate on or return other functions. It's used for caching, partial application, decorators, and operator-based reductions.
"""
from functools import reduce
number = [1, 2, 3, 4, 5]
result = reduce(lambda acc, x: acc + x,number)
print(result)  # Output: 15

# Practical example of reduce function
# first_element=number[0]
# second_element=number[1]
# result=0
# for i in range(len(number)):
#     if(i == 0):
#         result=first_element + second_element
#     else:
#         result = result + number[i+1] if i+1 < len(number) else result
    
# print(result)  # Output: 15


"What's the difference between map/filter and reduce?"

"map and filter return iterables (transform/select elements), while reduce collapses the whole iterable down to one final value."


# Decorators are a powerful tool in Python that allow you to modify the behavior of a function or class. They are often used for logging, access control, memoization, and more. A decorator is a function that takes another function as an argument and returns a new function that can add some kind of functionality to the original function.
# A decorated function loses its original __name__ and __doc__, because the wrapper function replaces it. wraps copies that metadata over so introspection/debugging still works correctly.

# Example of a wrap decorator:
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func()
        print("Something is happening after the function is called.")
    return wrapper 
@my_decorator
def say_hello():
    """This function says hello."""
    print("Hello!")
print((say_hello.__name__))  # Output: wrapper if we don't use wraps, but with wraps it will output: say_hello
print(say_hello.__doc__)  # Output: None if we don't use wraps, but with wraps it will output: This function says hello.
print(dir())
