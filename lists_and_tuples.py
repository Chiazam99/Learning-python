# list of integers and number of list items 
list1 =  (1, 2 ,3,4, 5,6,7,7,8,9)   # tuple 
print(list1)
print(len(list1))
print(list1[0:8])   # slicing list 

# Empty list
list2 = ()  # tuple
print(list2)
print(len(list2))

# Mixed list 
list3 = ('hi', 'girl', 3, 2.5 ) # tuple
print(list3)
print(len(list3))

# Replacing list elements - one element 
list4 =  [1, 2 ,3,4, 5,6,7,7,8,9]   # list
print(list4)
print(len(list4))
print(list4[0:8])
list4[0] = 3000
print(list4)

# Replacing list elements - multiple element 
list4 =  [1, 2 ,3,4, 5,6,7,7,8,9]   # list
list4[0:2] = [3000, 1000, 2000]
print(list4)

# Confirm elements in list 
print(50 in list4)
print(3000 in list4)
print(9 in list4)

# Print elements in list individually 
for elements in list4:
    print(elements)

# Add elements to list 
list4.append('Hello')
print(list4)

# Inserting to a particular position 
list4.insert(0,'hi')
print(list4)

# Remove element in list 
list4.remove(7)
list4.remove(7)
print(list4)

# Create new copy of list 
list5 = list4.copy()
print(list5)

# Random list trying out if true and false have to be in apostrophe 
random_list = [2, 5, False, True]
print(random_list) 

