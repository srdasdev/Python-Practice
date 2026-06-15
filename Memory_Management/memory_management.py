"""In python memory management is handled by the Python memory manager. The memory manager is responsible for allocating and deallocating memory for objects in Python. It uses a private heap to store all the objects and data structures. The memory manager also has an inbuilt garbage collector that automatically frees up memory by removing objects that are no longer in use.

By default, Python uses reference counting to keep track of the number of references to an object. When the reference count of an object drops to zero, it means that the object is no longer in use and can be safely deallocated.

Reference counting is a simple and efficient way to manage memory, but it has some limitations. For example, it cannot handle circular references, where two or more objects reference each other. In such cases, the reference count of the objects will never drop to zero, and they will not be deallocated, leading to memory leaks.
 """


a = [1, 2, 3, 4, 5]
b = a
c = a

del b #ref count 2
del c #ref count 1

del a #ref count 0, memory is deallocated


#Cyclic references can be handled by the garbage collector, which is a part of the memory manager. The garbage collector uses a technique called "mark-and-sweep" to identify and remove objects that are no longer in use, even if they are part of a circular reference.

# Example of cyclic reference:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node(1)
b = Node(2)
a.next = b
b.next = a  # creates    a circular reference
a.next.value = 2
print(a.next.value)  # Output: 1


del a  # ref count of a is 0, but b still has a reference to it
del b  # ref count of b is 0, but a still has a reference to it

"""a.next and b.next still reference each other, creating a circular reference. The garbage collector will eventually detect this and free the memory used by both objects.


To remove circular references, you can use the `gc` module in Python, which provides functions to interact with the garbage collector. You can manually trigger garbage collection using `gc.collect()`, which will force the garbage collector to run and clean up any circular references."""

import gc

print("Before garbage collection:")

collected = gc.collect()  # Manually trigger garbage collection to clean up circular references

print(f"GC collected {collected} objects")
print("After gc.collect()")

