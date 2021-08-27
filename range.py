# Print range as a list
result = range(1,11)
print(result) # result will be range(1,11) because it has to be put in a list or set to show the values 
# if not if the result should be in a new line per value, use a loop 
list1 = (list(result))
print(list1)
range2 = range(11,21)
list2 = (list(range2))
print(list2)
combined_list = list1 + list2
print(combined_list)
combined_list2 = [*list1,*list2]
print(combined_list2)
list1.extend(list2)
print(list1)

# Combining dictionaries with operators 
dict1 = {'shoe': 'heels'}
dict2 = {'hair':'cornrows'}
dict_combined = dict1|dict2
print(dict_combined)
dict1.update(dict2)
print(dict1)

for value in range(1,11):
    print(value, 'interation')


range3 = range(6)  # it will start from zero if the start figure isn't given 
# range(3,9) ..... 3 is start and 9 is stop 
print(list(range3))

#   ITERATE A LOOP 5 TIMES 
for i in range(5): # the loop starts from 0-4 (5 iterations )
    print(i)

# range has a default increment value of 1 range(1,11,1)
# One can change the increment by cahnging the last one to whatever increment is desired.

range4 = range(0,30,5)
print(list(range4))
range5 = range(-10,12,2)
print(list(range5))
range6 = range(10,-10,-3)
print(list(range6))


# Task 
print(list(range(3,31,3)))

# while loop
number = 1
while i in range(6):
    print(i)
    number = number +1 
     
