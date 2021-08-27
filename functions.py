#Functions use syntax:
#def_functionname():
#A function has to be called, that is the only way it's run. 
# When the function is called, it goes tothe function header and reads the statements in the function
# It can be ran multiple times 
# Before calling a function, it has to be defined 

def greet():
    print('Gege is a boy')
    return 'Chiazam is a girl'
    


greet()

# String passed during a function call is an argument 

def greet(name):
    print('How are you', name,'.')
    print(name, 'how are you doing?')


greet('Jack')

# Calculation 
def calc(num1,num2,num3,num4):
    average = (num1 + num2 + num3 + num4)/ 4
    return average

summ = calc(5,5,5,5)
print(summ)

# Built in functions 
scores = (55, 44, 66, 77, 89,23)

length = len(scores)
print(length)
addition = sum(scores)
print(addition)


# University exam grading example
marks= (55, 64, 75, 80, 65)
length_marks = len(marks)
average_marks = (sum(marks))/(length_marks)
print('Average mark is:', average_marks)

if average_marks >= 80:
    print('Your grade is A')
elif average_marks >= 60 or average_marks < 80:
    print('Your grade is B')
elif average_marks >= 50 or average_marks < 60:
    print('Your grade is C')
elif average_marks < 50:
    print('Your grade is F')

# University exam grading example using functions 
def find_avg_marks(markss):
    sum_of_mrks = sum(markss)
    how_many_subjects = len(markss)
    avg_marks = sum_of_mrks/how_many_subjects
    return avg_marks

def grade(avg_marks): 
    if avg_marks >=80:
        gradee = 'A'
    elif avg_marks >=60 and avg_marks <80:
        gradee = 'B'
    elif avg_marks >= 50 or avg_marks < 60:
        gradee = 'C'
    else: 
        gradee = 'F'
    return gradee 


markss = [50, 50, 50, 50]
avg_marks = find_avg_marks(markss)
print('The average is:', avg_marks)
gradee = grade(avg_marks)
print('Grade is:', gradee )

# Add & multiply 2 functions:

def add_numbers(n1,n2):
    addition_of_2 = n1+n2
    return addition_of_2

def multiply_numbers(n1,n2):
    multiplication_of_2 = n1 * n2
    return multiplication_of_2

n1 = 2
n2 = 10

addition_of_2 = add_numbers(n1,n2)
multiplication_of_2 = multiply_numbers(n1,n2)
print('The sum of n1 and n2:', addition_of_2)
print('The product of n1 and n2:', multiplication_of_2)



