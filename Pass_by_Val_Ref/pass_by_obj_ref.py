"""
In Python, when we pass an object to a function, we are passing a reference to that object. This means that if the object is mutable (like a list or a dictionary), changes made to the object within the function will affect the original object outside the function. However, if the object is immutable (like a string or an integer), any changes made to it within the function will not affect the original object outside the function, because a new object will be created for the modified value.
"""

# Example with a mutable object (list):
def modify_list(my_list):
    my_list.append(4) # This modifies the original list since lists are mutable 
my_list = [1, 2, 3]
print(f"Memory address of list before modification {id(my_list)}") # Output: Memory address of the original list [1, 2, 3]
print("Before modification:", my_list) # Output: Before modification: [1, 2, 3]
modify_list(my_list)

print("After modification:", my_list) # Output: After modification: [1, 2, 3, 4]

print(f"Memory address of list after modification {id(my_list)}") # Output: Memory address of the modified list [1, 2, 3, 4], unchanged


















# Example with an immutable object (string):
def modify_string(my_string):
    my_string += " World" # This creates a new string object since strings are immutable
    return my_string
my_string = "Hello"
print("Before modification:", my_string) # Output: Before modification: Hello

print(f"Memory address before modification {id(my_string)}") # Output: Memory address of the original string "Hello"

result = modify_string(my_string)

print("After modification:", my_string) # Output: After modification: Hello

print(f"After Modification {id(my_string)}") # Output: Memory address of the original string "Hello", unchanged

print(f"Memory address of modified string {id(result)}") # Output: Memory address of the new string "Hello World", different from the original string "Hello"