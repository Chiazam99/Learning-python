# Break and continue       

for item in range(1,6):
    if item == 5:
        break 
    print(item)
print('the end')    

#
while True:
    number = int(input('enter any random number:'))
    if number >=8:
        break  
    print(number)
print('Condition is met')

# continue statement 
for a in range(3):
    number = int(input('enter number:'))
    if number > 8:   
        print('Condition is met')    
    else:
        continue

# Continue in while loop 
# x = int(input('What is X: '))
# while x>=20:
#     if x == 20:
#         x = x + 5 
#         continue
#     print('Condition has been met')

# Trial example
languages = ('Python','Java','Swift','c','c++')
for plang in languages:
    if plang == 'c++':
        continue
    print(plang)

# Trial example 2
languages = ('Python','Java','Swift','c','c++')
for plang in languages:
    if plang == 'c++' or plang == 'Swift':
        continue
    print(plang)
    

x = int(input('What is X: '))
while x<=20:
     if x < 20:
        continue
print('Condition has been met')

