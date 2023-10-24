import random
class Hat:
    
    def __init__(self):
        self.houses =["griffindoor","hufflepuff","slytherin","ravenclaw"]

    def sort(self,name):
        print (name ," belongs to ",random.choice(self.houses))

hat = Hat()     #This is called instantiate (basically assigning a function/class to a variable)
hat.sort("Harry")


#--------------ClassMethods---------------------------------------------------------------------------------

# @classmethod
#we normally write method inside of classes that are automatically passed in reference to self (current object)
#-but sometimes we don't need that. we can create classes even without objects in it .
# for example, purposes like container for data that somehow related to the code. but we don't want to initiate anything.that just hold some data inside the class if we ever want to use them

import random

class Hat:

    houses =["griffindoor","hufflepuff","slytherin","ravenclaw"]    #This is a class variable.(variable that doesn't instantiate and work like a normal variable)
                                                                    #note that we did't define this inside a __init__ method and variable as self.houses. this is just work as a normal variable.  
                                                                    #this variable can be used in any functions of the class now(shared data).not only in current object

    @classmethod
    def sort(cls,name): #note that we use another variable called cls instead of self because this is classmethod
        print (name ," belongs to ",random.choice(cls.houses)) #self.houses is a instance variable, cls.houses is a class variable

Hat.sort("Harry")