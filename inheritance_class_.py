# allows you inherit attributes and methods from a parent class to a child class


class Animal:
    def eat(self):
        print('I can eat.')

class Dog(Animal):  # (Animal) makes it a child class 
    def bark(self):
        print('I can bark.')
class Cow(Animal):  # (Animal) makes it a child class 
    def moo(self):
        print('I can moo.')
class Parrot:  # parent class
    def talk(self):
        print('I can talk.')


dog1 = Dog()
dog1.eat() # eat can work here because it is a child class of animal and hence all i animal can work for it 
dog1.bark()
Cow1 = Cow()
Cow1.eat() # eat can work here because it is a child class of animal and hence all i animal can work for it 
Cow1.moo()
parrot1 = Parrot()
#parrot1.eat() # eat CAN'T work here because it is a child class of animal and hence all i animal can work for it 
parrot1.talk()

# POLYGON parent class thta calclates the perimteter and displays info 
# It has child classes for specific polygons 

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print(' A polydon is a 2 dimensional shape with straight lines.')

    def perimeter_of_polygon(self):
        perimeter = sum(self.sides)
        print('The perimeter is:', perimeter)

    def area_of_polygon(self):
        area = 1
        for sides in self.sides:
            area = area * sides
            #   -OR-
    #   import math
    #   area = math.prod(self.sides) 
        print('Areas is:',area)
class Triangles(Polygon):
    def display_info(self):
        print('Triangle is a polgon with 3 sides.')
        # In other to display display_info in Polygon class, 
        # add a line of code to the traingle class stating that.
        Polygon.display_info(self)  
        # -OR-
        super().display_info()
class Quadilaterals(Polygon):
    def display_info(self):
        print('Quad is a polgon with 4 sides.')

triangle1 = Triangles([2,4,5])
triangle1.perimeter_of_polygon()
# Method overriding  or function overriding
# ---- if the same method/function exists in parent and child class, 
# the method/ function of the parent class will be overidden.
# parent class is called base class
# child class is called derived class
#hence.....
triangle1.display_info()
# this line of code prints display_info of triangle method
# In other to display display_info in Polygon class, 
# add a line of code to the traingle class stating that 
# anoher methos id using the super function - 
# It displays the super function result in a subclass
triangle1.area_of_polygon()
