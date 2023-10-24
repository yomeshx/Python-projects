#String format is optional way to print something with same type or different types variables
#just like f"bla bla {non-str-variable} bla bla" method, but little different.
#we can also use positional arguments in this method of printing
animal = "deer"
height = 6
object_ = "fence"
animal = animal.capitalize()

print("{} jumped over {} feet {}".format(animal,height,object_)) #multiple {} will have value according to the given order inside the format function
print("{} jumped over {} feet {}".format("Rabbit",5,"Rock")) #you can either just straight up give the thing you want to print inside the format function
                                                            #-or the variable name inside the format function
print("\n")
#||||||||||||||||||||||<--How to use this method more advanced ways-->||||||||||||||||||||||
#1
print("{2} jumped over {1} feet {0}".format(animal,height,object_))#Positional arg method #you can include index numbers inside {} to use any argument at any place 
                                #index =     #0      #1     #2
#2
print("{animal} jumped over {height} feet {object_}".format(animal="betta",height=7,object_="wall"))#keyword argument method

#3
line = "Hey {},can i have {} of those cupcakes"
print(line.format("Mia",3))
line = "Hey {0},can i have {1} of those cupcakes"
print(line.format("Jinny",2))
line = "Hey {name},can i have {amount} of those cupcakes"
print(line.format(name="Stoya",amount=4))

print("\n")

print("{} jumped over {:3} feet {}".format("Rabbit",5,"Rock")) #You can make spaces (paddings) by ':number of spaces' inside a {}
print("{} jumped over {:<3} feet {}".format("Rabbit",5,"Rock")) #align to the left
print("{} jumped over {:>3} feet {}".format("Rabbit",5,"Rock")) #align to the right
print("{} jumped over {:^3} feet {}".format("Rabbit",5,"Rock")) #align to the center

print("\n")
                                                                                                #keyword arguments
print("{animal} jumped over {height:5} feet {object_}".format(animal = "Rabbit",height =5,object_ ="Rock")) #You can make spaces (paddings) by ':number of spaces' inside a {}
print("{animal} jumped over {height:<5} feet {object_}".format(animal = "Rabbit",height =5,object_ ="Rock")) #align to the left
print("{animal} jumped over {height:>5} feet {object_}".format(animal = "Rabbit",height =5,object_ ="Rock"))  #align to the right
print("{animal} jumped over {height:^5} feet {object_}".format(animal = "Rabbit",height =5,object_ ="Rock"))  #align to the center