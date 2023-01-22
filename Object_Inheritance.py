'''Inheritance and composition allow us to reuse class methods for other classes'''


''' Inheritance '''
# Inheritance means we have already defined the methods of one class and would like another class to use those methods as well
# the new class will have the methods of the parent class, but will also have its own methods as well

# the following shows a rectangle class, and a square class. One which inherits from the other.
# As shown, square will be a child of rectangle and rectangle will be the superclass/parentclass

class Rectangle:
    '''rectangle class has two members, length and width, and two methods to return area and perimeter using those members'''
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def area(self):
        return self._length * self._width

    def perimeter(self):
        return self._length*2 + self._width*2

class Square(Rectangle):
    def __init__(self, side):
        self._length = side  #this is known as method overriding
        # we override a method by giving the data members different behavior in the child class than it has in the parents class
        self._width = side
    '''inherits class methods from the rectangle, and reduces redundancy in code. '''
R1 = Rectangle(6, 5)
S1 = Square(5)

R1.area()
R1.perimeter()

S1.area()
S1.perimeter()

class Square2(Rectangle):
    def __init__(self, side):
        # using the super lets you temporarily call upon and use the rectangle class
        # in this case we are using side twice as its parameters in place of length width
        super().__init__(side, side)

s2 = Square2(6)

s2.perimeter()

