'''sometimes it is easier to just use list comprehension
rather than looping through a list and appending values to a new list. The example below
demonstrates an example of each.'''


#The class and function below are set up to be used in the function examples that come afterwards (example 1&2)
class car:
    def __init__(self, name, mpg):
        self._name = name
        self._mpg = mpg

    def get_mpg(self):
        return self._mpg

def max_val(vals):
    '''function that finds max value in a list'''
    max = None
    for val in vals:
        if max == None:
            max = val
        else:
            if val > max:
                max = val
    return max



#Examples are below:
#-------------------------------------

#Example 1: Using a list to append new values

def find_highest_mpg(cars):
    ''' this creates a new list - MPG, and appends each element that is selected/filtered
     in the list comprehension below. There is no need to create an empty list and explicitly append
     values in this case. '''
    MPG = [car.get_mpg() for car in cars]
    return max_val(MPG)


#-------------------------------------

#Example 2:

#Using list comprehension

def find_highest_mpg2(cars):
    MPG = []
    for car in cars:
        MPG.append(car.get_mpg())
    return max_val(MPG)
#-------------------------------------

hyundai = car("Sonata", 37)
honda = car("Accord", 35)
toyota = car("Camry", 36)
nissan = car("Maxima", 34)

car_list = [hyundai, honda, toyota, nissan]

#Calling the first function
find_highest_mpg(car_list)

#Calling the second function
find_highest_mpg2(car_list)
