"""
Docstring for MRO.method_resolution_order

Method Resolution Order (MRO) defines the order in which Python searches for a method in a class and its parent classes. It becomes important when the same method exists in more than one class in an inheritance chain, especially in multiple inheritance.

The example shows how Python decides which method to execute when both a parent and a child class have a method with the same name.
"""

class A:
    def greet(self):
        return "Hello from A"


class B(A):
    def greet(self):
        return "Hello from B"

a = B()
print(a.greet())  # Output: Hello from B

print(B.__mro__)  # Output: (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

# When obj.fun() is called, Python first looks in class B.
# Since B defines fun(), it runs that method and does not check class A.
# The MRO here is: B -> A.



# Multiple Inheritance (Diamond Problem)


class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    def greet(self):
        return "Hello from C"
class D(B, C):
    pass

a = D()
print(a.greet())  # Output: Hello from B
print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# Explanation:
# D inherits from B and C.
# Python follows the MRO: D -> B -> C -> A.
# Since B has fun(), it is executed and the search stops.


"""Methods to View Method Resolution Order (MRO) of a Class
Python provides two ways to check the method resolution order (MRO) of a class:

__mro__ attribute: shows a tuple of classes in the order Python searches for methods.
mro() method: returns a list of classes in the MRO."""

