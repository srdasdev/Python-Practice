x = [1,2,4]
y= [1,2,4]

if(x == y):
    print("x and y are equal")

# Here it will print x and y are equal because the == operator checks for value equality. It compares the contents of the lists and finds that they are the same.


# Identity operator (is): The identity operator (is) checks whether two variables refer to the same object in memory. It returns True if both variables point to the same object, and False otherwise.

z=x
if(x is y):
    print("x and y are the same object")
elif x is z:
    print("x and z are the same object")
else:
    print("x and y are different objects")
# Here it will print x and z are the same object because x and z refer to the same list in memory, while y is a different list with the same contents.