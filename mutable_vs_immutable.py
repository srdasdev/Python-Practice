#Immutable means that the value of the object cannot be changed after it is created. In Python, examples of immutable objects include int, float, bool, string (str) and tuple.

# In simple terms, once you create an immutable object, you cannot modify its value. If you try to change it, a new object will be created instead.


# Exception: However, there is an exception in immutability as well. We know that a tuple in Python is immutable. But the tuple consists of a sequence of names with unchangeable bindings to objects. Consider a tuple:

# tup = ([3, 4, 5], 'myname') 


# Example of mutable objects in Python include list, set, and dictionary. These objects can be modified after they are created. For example, you can add or remove elements from a list, change the value of a key in a dictionary, or add/remove elements from a set.

#**Mutable**

list1 = [1, 2, 3]
print("Original list:", list1)
list1.append(4)
print("Modified list:", list1) #output: Modified list: [1, 2, 3, 4]


#**Immutable**
str1 = "Hello"
print("Original string:", str1)
str1 = str1 + " World"
print("Modified string:", str1) #output: Modified string: Hello World
print(id(str1)) # Output: Memory address of the new string "Hello World"
print(id("Hello")) # Output: Memory address of the original string "Hello"
# //But note that the original string "Hello" is not modified; instead, a new string "Hello World" is created and assigned to str1. The original string remains unchanged.


# Ints are also immutable:
num1 = 10
print("Original number:", num1)
num1 += 5
print("Modified number:", num1) #output: Modified number: 15
print(id(num1)) # Output: Memory address of the new number 15
print(id(10)) # Output: Memory address of the original number 10
# //Similar to strings, when we modify num1, a new integer object is created with the value 15, and num1 now references this new object. The original integer 10 remains unchanged.