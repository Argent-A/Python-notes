
''' Composition '''
# Object composition refers to when one class obtains an object of another class as one if its data members.
#the 3 classes below show inheritance, the 4th class shows composition. 

class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * self._length + 2 * self._width


class Square(Rectangle):
    def __init__(self, side):
        self._length = side
        self._width = side


class Cube1(Square):
    def surface_Area(self):
        return  super().area()*6

    def volume(self):
        return super().area()*self._length

'''
The square class is a child class of rectangle
The cube class is a child class of square
The cube class is inheriting methods from the rectangle class through the square class

However this structure can more simply be constructed through composition. 

the best way to consider whether to use composition or inheritance is to think of 
'is-a' relationship vs 'has-a' relationship types.
A cube 'has a' square - 6 of them. However it is not a square, therefore it is better to use a square class within its methods through composition. 
A square 'is a' rectangle, therefore it was appropriate to have square inherit the rectangle class

More simply, 
Inheritance is about a relation between classes.

Composition is a about relations between objects of classes.

Tangible examples:
Car: Gasoline and electric cars can be child classes of the car class Inheritance would make logical sense for them. 

Motorcycles may have many of the same methods and characteristics as cars, but should not inherit a car class. But using 
a car class to compose certain methods for motorcycles may seem more reasonable. (distance traveled, MPG, etc)
'''



class Cube2:
    def __init__(self, side):
        self.face = Square(side)  # face is a data member of type Square
        # therefore we are using a square object directly within the cube class instead of
        # inheriting the methods of rectangle

    def surface_area(self):
        return self.face.area() * 6

    #now we take the square object (self.face), use its method "area" to return the surface area of the cube


    def volume(self):
        return self.face.area() * self.face.get_length()
    #we take methods of the square class - these methods are inherited where rectangle is the parent class and square is the child.



'''what is really happening between the two cube classes:

Cube1: We inherit the methods of the square class and thus gain access to them without instantiating a square object.

Cube2: Using the square class within the cube class (composition) allows us to directly use square class methods through instantiation. 

Both cube1, cube2, classes essentially perform the same function. However, we are generally advised to lean to composition when in doubt.

Inheritance is perfectly fine as long as your code is straightforward, but if your code needs heavy modification down the line it is wiser to use composition.

'''
