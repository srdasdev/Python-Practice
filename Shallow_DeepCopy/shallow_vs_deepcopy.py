list1 = [1,2,3]
list2 = list1 # This creates a shallow copy, both list1 and list2 refer to the same list in memory
print(list1) # Output: [1, 2, 3]
print(list2) # Output: [1, 2, 3]
list2.append(4) # Modifying list2 will also modify list1 since they refer to the same list
print(list1) # Output: [1, 2, 3, 4]
print(list2) # Output: [1, 2, 3, 4]



# ==========================SHALLOW COPY===========================

# //Shallow copy creates a new object but does not create copies of nested objects. Instead, it references the original nested objects. This means that changes to nested objects in the copied object will affect the original object.

list3 = list1.copy() # This creates a shallow copy of list1, list3 is a new list but it references the same nested objects as list1
print(list3) # Output: [1, 2, 3, 4]
list3.append(5) # Modifying list3 will not affect list1 since list3 is a new list
print(list1) # Output: [1, 2, 3, 4]
print(list3) # Output: [1, 2, 3, 4, 5]


new_list = [1, 2, [3, 4]]
shallow_copied_list = new_list.copy() # This creates a shallow copy of new_list
print(shallow_copied_list) # Output: [1, 2, [3, 4]]
shallow_copied_list[2].append(5) # Modifying the nested list in shallow_copied_list will also modify the nested list in new_list since they reference the same nested list
print(new_list) # Output: [1, 2, [3, 4, 5]]
print(shallow_copied_list) # Output: [1, 2, [3, 4, 5]]

# Verify:

print(new_list[2] is shallow_copied_list[2]) # Output: True, both new_list and shallow_copied_list reference the same nested list


# Shallow Copy = 
#     ✓ Creates new outer container
#     ✗ Does NOT recursively copy nested objects
#     = Just copies the REFERENCES to nested objects





# ===========================DEEP COPY===========================
# Deep copy creates a new object and recursively copies all objects found in the original. This means that changes to any part of the copied object will not affect the original object.

import copy
deep_copied_list = copy.deepcopy(new_list) # This creates a deep copy of new_list
print(deep_copied_list) # Output: [1, 2, [3, 4, 5]]
deep_copied_list[2].append(6) # Modifying the nested list in deep_copied_list will NOT affect the nested list in new_list since deep_copied_list has its own copy of the nested list
print(new_list) # Output: [1, 2, [3, 4, 5]]
print(deep_copied_list) # Output: [1, 2, [3, 4, 5, 6]]