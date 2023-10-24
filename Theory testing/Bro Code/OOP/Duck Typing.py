#                   <------------------ Duck Typing ------------------>
#Class type will not be checked if minimum methods or attributes are present
class Duck:
    def walk (self):
        print("This duck is walking")
    def talk (self):
        print("This duck is quacking")

class Chicken:
    def walk (self):
        print("This chicken is walking")
    def talk (self):
        print("This chicken is clucking")

class Person:
    def catch (self,bird):
        bird.walk()
        bird.talk()
        print("You caught the critter")

duck = Duck ()
chicken = Chicken()
person = Person()

person.catch(duck)
print("-----------------------")
person.catch(chicken)