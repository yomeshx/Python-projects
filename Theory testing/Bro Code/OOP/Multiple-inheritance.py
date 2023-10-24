#                   <--------------- Multiple inheritance --------------->

#Note - When a child class inherit methods from more than one different parent classes, it consider it has 
        # -multiple inheritance.

class Prey:         #Parent Class 1
    def flee (self):
        print("fleeing from the predator")

class Predator:     #Parent Class 2
    def chase(self):
        print("Chasing the prey")

class Fish(Prey,Predator):  #Child Class with multiple inheritance
    def swim (self):
        print("Fish is swimming")

#-------------------------------------------------------
fish = Fish()
fish.flee()
fish.chase()
fish.swim()