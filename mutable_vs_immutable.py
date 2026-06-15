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
# //But note that the original string "Hello" is not modified; instead, a new string "Hello World" is created and assigned to str1. The original string remains unchanged.


