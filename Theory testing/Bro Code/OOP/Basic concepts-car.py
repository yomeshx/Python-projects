class Car:                      #Class is like a blueprint, once you have one you can make many cars with different colors and models
    wheels = 4  #class variable
    def __init__(self,make,model,year,color) :      #It is necessary to pass 'self' in functions in order to execute our method
        self.make = make        #instance Variable
        self.model = model      #instance Variable  #instance variables inside the __init__ are consider "attributes"
        self.year = year        #instance Variable
        self.color = color      #instance Variable

    def drive (self):
        print("This "+self.model+" Is Driving ")
    def stop (self):
        print("This "+self.model+" Is Stopped")

#------------tests----------------------
car_1 = Car("Honda","Civic",2018,"red")
car_2 = Car("Ferrari","La ferrari",2018,"yellow")

car_1.drive()
car_2.stop()

# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)

# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)
    
                                    #note -- Class Variables
                            #-------------------------------------
#values passed to class variables are default values that applies to all things created using this class.
    #ex : you can make many cars using this class.car_1,2 etc but they will all have 4 wheels by default
    #but you can change the default and assign whatever value if you need ,like this
        #Car.wheels =6  --> assign new value to all instances
        # car_1.wheels = 8 ---> only assign to a specific instance 

                                    #note - __init__ Constructor
                            #-------------------------------------
# __init__ is called "constructor" because it construct the objects.it takes instance variables as
#-attributes that are essential to create the object.

                                    #note -- self
                            #-------------------------------------
#It is necessary to pass 'self' in functions in order to execute our methods

                                    #note -- instance variables
                            #-------------------------------------
#variables that declared inside a constructor called instance variable, as a whole all those can called as attributes
