# code to find all numbers which are divisible by 7 but are not a multiple of 5 
#between 2000 and 3200 (both included).
# in a comma-separated sequence on a single line

list_of_num_divisble_7_not_5 = list()
for n in range(2000, 3201):
    if (n%7 == 0) and (n%5 != 0):
        list_of_num_divisble_7_not_5.append(n)
print(list_of_num_divisble_7_not_5)


# Finding factorial of numbers 
number = int(input('Enter a number you desire to know the factorial of:'))
factorial = 1 
if number < 0:
    print('This is a negative number. You can\'t find the factorial of a negative number.')
elif number == 0:
    print('Factorial is 1.')
else:
    for n in range(1,number +1):
        factorial = factorial * n
    print('The factorial value is:', factorial)
        
