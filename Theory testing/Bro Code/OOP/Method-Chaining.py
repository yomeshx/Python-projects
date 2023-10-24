#           <--------------------- Method Chaining --------------------->
#instead of calling methods in multiple lines , calling multiple methods in a single line is called "method chaining"
#When you using method chaining it expect to return something from the method at the end ,so that why use 'return self'
class Car:
    def turn_on(self):
        print("Engine Turned On")
        return self
    def change_gear (self):
        print("Gear Up")
        return self
    def brake (self):
        print("Pushed the Break")
        return self
    def turn_off(self):
        print("Engine turned Off")
        return self
#---------------------------------------------

car = Car()

car.turn_on().change_gear().brake().turn_off()  #Method chaining
#Another way to use method chain
car.turn_on()\
    .change_gear()\
    .brake()\
    .turn_off()