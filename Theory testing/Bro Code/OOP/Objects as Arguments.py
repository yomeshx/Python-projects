class Car:
    color = None

class Motorcycle:
    color = None

def change_color(vehicle,color):
    vehicle.color = color

car_1 = Car()
car_2 = Car()

bike_1= Motorcycle()
bike_2= Motorcycle()

change_color(car_1,"Red")
change_color(car_2,"Black")
change_color(car_1,"Black")
change_color(car_1,"Blue")
print(car_1.color)
print(car_2.color)
print(bike_1.color)
print(bike_2.color)