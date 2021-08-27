# WHILE LOOP 
count = 0
while count < 4:
    print('loop loop loop')
    count = count + 1 

# adding limit to loop
count = 0
while count <= 4:
    print(count)
    count = count + 1 

number  = 1
multiplier = 2
product = multiplier * number
while number <=10:
    print(multiplier,'x',number,'=',product)
    number = number + 1 


# FOR LOOP 

text = 'strawberry'

for character in text:
    print(character)

# ANOTHER FOR LOOP  
text = 'strawberry','beans', 'fish'
for food in text:
    print(food)

# TIMETABLE USING FOR LOOP
multiplier = int(input('Enter the times table you want displayed on the screen:'))

for number in range(1,13):
    product = multiplier * number
    print(number,'x',multiplier,'=',product)


# FOR SUM OF NUMBERS FROM 1-100
total = 0
for additive in range(1,101): 
    total = total + additive
    print(total)







