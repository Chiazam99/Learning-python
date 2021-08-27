# Code to test nested if statement

age = int(input('How old are you? '))
if age >= 18 and age <=59:
    print('You can take alcohol but do not get drunk')
    Faith = input('Are you a believer? (Respond with yes or no): ')
    Faith = Faith.lower()
    if Faith == 'yes' or Faith == 'no':
        pass
        if Faith == 'yes': 
            print('Not everything is expedient 1 Cor 10:23')
        elif Faith == 'no':
            print('Drink with sense')
        else:
                print('Invalid response')
elif age < 18 : 
    print('You are too young. Treat your liver right!') 
else: 
    print('Old cargo. Are you ready to die???')  
