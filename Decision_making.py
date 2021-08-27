score = int(input('What is your score? '))

if score >= 50:
    print('You passed!')
    
if score <50:    
    print('You failed. Try again')

    # Using If-else statement 

age = int(input('How old are you? '))
if age >= 18 and age <=59:
    print('You can take alcohol but do not get drunk')
if age < 18 : 
    print('You are too young. Treat your liver right!')
else: 
    print('Old cargo. Are you ready to die???')   
 
  
#  Code to get determine if a number is positive or negative 

print('Type of Number detector')
number = float(input('Enter a random number: '))
if number > 0:
    print('This is a positive number')
elif number < 0: 
    print('This is a positive number')
else:
    print('This is the origin. You probably typed zero')

