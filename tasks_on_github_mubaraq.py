#Obtain random die values when 2 dice are rolled 
import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("You have a ", random.randint(min, max), ",", random.randint(min, max))

    roll_again = input("Roll the dices again? (Enter yes or y to roll again.)")
    roll_again = roll_again.lower()
else:
    print('Thanks for playing. Run the code again to get random numbers.')

# obtain random number from a range 
import random

x = random.randint(1, 6)
y = random.randint(1, 6)
print(x,y)

# return a random float using RANDOM() OR UNIFORM()

p = random.random()   # random() has a default range from 0 to 1. 
q = random.random()   
r = random.uniform(0,1)  # random float/decimal value from specified range 
s = random.uniform(10,100)
t = random.randint(0,1)
print(p,q)
print(r,s,t)


def is_palindrome(word):
    if(word == word[::-1]):
        print(word[::-1])
        print("The string is a palindrome")
    else:
        print(word[::-1])
        print("The string isn't a palindrome")
        
word = str(input('Enter a word:'))
word = word.lower()     
is_palindrome(word)




