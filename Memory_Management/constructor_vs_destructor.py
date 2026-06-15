class Myname:
    def __init__(self, name):
        self.name = name
        print("Constructor called")

    def __del__(self):
        print("Destructor called")

obj = Myname("Alice")
print("Object created with name:", obj.name)
obj1 = obj
del obj


""" Many beginners assume __del__() is guaranteed to run immediately when they call del. However, this is not the case. The del statement only decrements the reference count of the object, and the actual destruction of the object (and thus the calling of __del__) may not happen immediately. It depends on when the garbage collector decides to clean up the object.


Also, during interpreter shutdown or complex circular references, __del__() may not behave exactly as expected. That's why for files, database connections, etc., Python developers usually prefer:

with open("file.txt") as f:
    data = f.read()

instead of relying on __del__() for cleanup."""