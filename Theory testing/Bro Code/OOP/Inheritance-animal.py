#       <--------------- Inheritance --------------->
#If there is methods that are common to more than 1 class we make a parent class in order to avoid having to insert same thing over and over in similar classes,
#we put all the methods that are common in a one parent class.
# so all child classes can inherit things from parent class
#and child classes has methods that only unique to them

class Animal :
    def eat (self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")
    def run (self):
        print("This animal is running")
class Duck(Animal):       #"Rabbit" Will inherit all the methods "Animal" class has ,
    def float(self):#so Rabbit is a child class and Animal is a Parent class of it
        print("This Duck is Flying")
class Deer(Animal):
    def jump(self):
        print("This Deer is jumping")
#-----------------------------------------
duck = Duck()
deer = Deer()

duck.eat()  #methods that are inherit from the parent class
deer.sleep()#methods that are inherit from the parent class

deer.jump()#methods that are unique to the child class
duck.float()#methods that are unique to the child class