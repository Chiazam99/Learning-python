# Class is the blueprint, outline, format, structure, 
# Object is the content, actual house
# In objects - functions are called methods while variables are called attributes 

# PROGRAM TO DETERMINE IF STUDENT PASSED OR NOT 
class Student: 
    pass # NO METHOD IN HERE YET THAT'S WHY WE ARE PASSING IT.

student1 = Student()
student1.name = 'Harry'
student1.score = 12

print(student1.name)
print(student1.score)


class Student: 
    def check_pass_fail(self):
        if self.score >=45:
            return 'Passed'
        else:
            return 'Failed'

student1 = Student()
student1.name = 'Harry'
student1.score = 12


print(student1.score) # not necessary to print score but I would like to see score
pass_or_fail = student1.check_pass_fail()
print(pass_or_fail) 

student2 = Student()
student2.name = 'JAVAK'
student2.score = 90


print(student2.score) # not necessary to print score but I would like to see score
pass_or_fail = student2.check_pass_fail()
print(pass_or_fail) 

# It is not good practice to define the attributes of objects outside the class
# The init method (Function) is used to define the attributes in the class 

# Example 
class Student: 
    def __init__(self, name, score):    # Function/ method to call the variables/attributes to used in the obeject
        self.name = name
        self.score = score

    def check_pass_fail(self):
        if self.score >=45:
            return 'Passed'
        else:
            return 'Failed'

    


student_name = str(input('Name of student:'))
print(student_name)
student_score = float(input('Students score:'))
print(student_score)
student1 = Student(student_name,student_score)
#student1 = Student('Hannah',23)
pass_or_fail = student1.check_pass_fail()
print(pass_or_fail)


# Addition of 2 numbers with object outside class 
class Addition:
    def add2_numbers(self, n1, n2):
        sum = n1 + n2  
        return sum 


n1 = 4
n2 = 5
result = Addition().add2_numbers(n1,n2)
# -OR-  
# adding = Addition()  
# result = adding.add2numbers(n1,n2)
print(result) 


# Addition of 2 numbers with object inside class 
class Addition:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def add2_numbers(self):
        sum = self.n1 + self.n2  
        return sum 

adding = Addition(10,20)
result2 = adding.add2_numbers()
print(result2)




# Perimeter of a triangle 
class Triangle:
    def __init__(self,l1,l2,w):
        self.l1 = l1
        self.l2 = l2
        self.w = w

    def perimeter(self):
        tri_perimeter = self.l1 + self.l2 + self.w
        return tri_perimeter
    
    def type_triangle(self):
        if self.l1 == self.l2 == self.w:
            return'equilateral triangle'
        if self.l1 == self.l2 != self.w:
            return'isoscles triangle'
        if self.l1 != self.l2 != self.w:
            return' scalene triangle'

t = Triangle(2,2,2)
result = t.perimeter()
result2 = t.type_triangle()
print('The type of triangle is:',result2, 'The perimeter is:',result)


