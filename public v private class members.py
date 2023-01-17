''' When a class data member is private, it cannot be used outside the scope of its class.
Python does not have a specific keyword to make a class private, however any data member whose
name begins with an underscore will be treated as private. Private data classes are used for data hiding,
for when we do not want class member data to be accessed or manipulated'''

# For example, in the following example we have student objects with the following data members:
# Age
# Grade
# Name

class Student:
    # the self variable represents the instance of the object
    def __init__(self, name, grade, age): #__init__ is a constructor allowing python to
        # instantiate an object and pass the following additional arguements:
        self._name = name
        self._grade = grade
        self.age = age

#lets create an instance of this student class:

Jakob = Student("Jakob", 94, 21)

print(Jakob.age) # note that we can access this data member as we have specified it as a public type
# (no underscore after the self reference)
# but we cannot access any other members:
# print(Jakob.name, Jakob.grade, will not be retrieved unless we create specific class functions
# that let us retrieve them. Like so:

class Student2:
    def __init__(self, name, grade, age):
        self._name = name
        self._grade = grade
        self.age = age

    def get_grade(self):  # <-- allows us to retrieve the private class member `grade`
        return self._grade

Alex = Student2("Alex", 88, 21)
print(Alex.get_grade())

# The reason as to why private class members are preferred is so the object member data cannot be accessed
# or changed outside of the class. For example, we are able to change Alex's age outside of the class below:
# This can make for sticky situations when debugging

Alex.age = 23
print(Alex.age)
