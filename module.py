# Module is a file that contains python code that we can use in our program. 

import math  # everything in math moduleis available 
n = 25
result = math.sqrt(n)
print(result)

# to use just a specific operator from a module .. u
# use the from...import statement 

from math import prod, sqrt, pi, sin  # -or- from math import * (all operators - same as import math) (Bad practice)

n = [5,10,15,20]
product = prod(n)  # you dont need to use dot operator anymore, use operator straiaght away
print(product)

sine = sin(60)
print(sine)

area_of_a_circle = pi*(5^2)
print(area_of_a_circle)

# to know all the functions in the maths module - use DIR 
import math
print(dir(math))

# Custom Modules 
# Create your own moduel and import it to use it 
# Create a custom module called : Basic Calculator 
import Basic_calculator
result = Basic_calculator.add(6,5)
print(result)
Basic_calculator.subtract(6,5)
Basic_calculator.divide(6,5)
Basic_calculator.multiply(6,5)
