#               <----------------- Abstract Classes and methods ----------------->
#Abstract classes are work like a model structure,it contains abstract methods .it just a plan to look at.
# Abstract classes prevents you from making objects of their class
from abc import ABC,abstractmethod      #1.You need to import ABC and abstractmethod from the abc library
class Vehicle (ABC):

    @abstractmethod                     #2.You need to add '@abstractmethod' before def to all the methods you wish to make act as abstract method
    def start (self):
        print("This vehicle is running")

    @abstractmethod
    def drive (self):
        print("This vehicle is now driving")

    @abstractmethod
    def stop(self):
        print("This vehicle is stopped")

class Motorcycle(Vehicle):          #You cant skip adding any method that are in the abstract class.it makes sure you override all methods
                                    #so you can say it is a model of other classes we make,we make child classes by overriding abstract methods given on the abstract classes 
                                    #if you forget to override a method it will show TypeError: Can't instantiate abstract class Motorcycle with abstract method stop
    def start (self):
        print("This Motor cycle engine is running idle")
    def drive(self):
        print("This Motor cycle is now driving")
    def stop (self):
        print("This motor cycle is now stopped ")

#---------------------------------------------------------------
bike = Motorcycle()
bike.start()

#<----Summery---->
#Abstract classes is like a instruction\plan of other classes ,it doesn't do anything only act as a "ensure everything is added as planed" 
#You cant skip adding any method that are in the abstract class.it makes sure you override all methods
#so you can say it is a model of other classes we make,we make child classes by overriding abstract methods given on the abstract classes 
#if you forget to override a method it will show TypeError: Can't instantiate abstract class Motorcycle with abstract method stop