#       <----------------------- Method Over riding ----------------------->
#If you give a same method name to both child and parent class ,method in child class will be the method that is gonna be active 
class Animal :
    def eat(self):
        print("This animal is eating")
class Rabbit(Animal):
    def eat(self):
        print("This Rabbit is eating")

#---------------------------------------
rabbit = Rabbit()

rabbit.eat()    #This will be using eat method defined in child class Rabbit not from the Parent class Animal