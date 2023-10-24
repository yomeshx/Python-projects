#           <--------------- Multi-level inheritance --------------->
#note - works like family tree,  parent inherit qualities from their parents
    #and children inherit qualities from grand parents and parents

class Organism:         #Grand Parent
    alive = True

class Animal(Organism): #Parent Class
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Dog(Animal):      #Child Class
    def bark (self):
        print("This dog is barking")

class Cat(Animal):
    def meow (self):
        print("This cat is meowing")

class Parrot(Animal):
    def fly (self):
        print("This Parrot is flying")

#------------------------------------------
dog = Dog()

#so child class inherit methods from both parents and grand parent in multi-lvl
dog.bark()
dog.eat()
dog.sleep()