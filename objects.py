# EVERYTHING IS AN OBJECT 

lists =[2,5,7,9]
print(type(lists))

sets ={2,5,7,9}
print(type(sets))

integerss = 5
print(type(integerss))

strings = 'ddd'
print(type(strings))

def function_fun():
    pass

print(type(function_fun))

# DIR FUNCTION 
# Used to list out all methods and variables of an object 

result = [1,2]
print(dir(result))
# shows all you can us with the list
result2 = {1,2}
print(dir(result2))

# ID FUNCTION  - Helps one know the ID of a function
# ID is unique and constant through out life time of object
print(id(result))
print(id(result2))

# When an object is assigned to a variable, thesame object can be assigned to another variable

a = [ 3,4,5]
b = a

a.append('a')
print(a)
print(b)

# in order to not modify b, copy a into be and then make changed
# How to copy 
a = [ 3,4,5]
b = a.copy()

a.append('a')
print(a)
print(b)


