numbers = 1
while numbers <=100:
    if numbers %5 == 0 and numbers%3 == 0:
        print('fizzbuzz')
    elif numbers%3 == 0: 
        print('fizz')
    elif numbers%5 == 0:
        print('buzz')
    else: 
        print(numbers)
    numbers = numbers + 1 


for numbers in range(1,101):
    if numbers %5 == 0 and numbers%3 == 0:
        print('fizzbuzz')
    elif numbers%3 == 0: 
        print('fizz')
    elif numbers%5 == 0:
        print('buzz')
    else: 
        print(numbers)


def prime_checker(n1):
    if n1 > 1:     # for numbers less 1 ... negative numbers 
        for n in range(2,n1): 
    # starts from 2 because every number is divisible by 1 and if it begins at 1, the result wouldnt
    #  exceed the first part of if statement 
            if n1%n == 0:
                print(n1,'is not a prime number.')
                break
        else:
            print(n1,'is a prime number.')
             
    else:
        print(n1,'is not a prime number.') 

n1 = int(input('Enter a number:'))
prime_checker(n1) 

# How to put up a condition for 2 ..... 2 begins the range 

# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, 
# between 1500 and 2700 (both included).


list_of_multiples_of_5_and_7 =list()
set_of_multiples_of_5_and_7 =set()
for n in range(1500,2701):
    if (n % 7 == 0) and (n % 5 == 0):
        # how to put your numbers in a set. 
        list_of_multiples_of_5_and_7.append(n)
        set_of_multiples_of_5_and_7.add(n)
print(list_of_multiples_of_5_and_7) 
print(set_of_multiples_of_5_and_7)

food = { 'breakfast':'bread', 'lunch': 'swallow', 'dinner':'rice'}
#print(set(food))
print(food.keys())  #prints the keys in a dictionary
print(food.values()) # prints the values in a dictionary
print(set(food.keys()))   #prints a set of the keys in a dictionary
print(set(food.values()))   #prints a set of the values in a dictionary



        




