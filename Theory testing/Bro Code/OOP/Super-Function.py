#               <------------------ Super Functions ------------------>

#Super function allows you to access methods of a parent class.
# it returns temporary object of a parent class when used.

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

class Square (Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area (self):
        return self.length*self.width

class Cube (Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height
    def volume (self):
        return self.height*self.length*self.width
#----------------------------------------------------
square = Square(3,3)
cube = Cube(3,3,3)

print(square.area())
print(cube.volume())