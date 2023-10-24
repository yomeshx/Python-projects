#Scope = the region that a variable is recognized
#       **A variable is only available inside the region it is created
#       **There are two kinds of variables
#           1.Global
#           2.Local 

greet ="Hi"         #Global Variable (Scope = global)
def example():
    name ="Yomesh"  #Local Variable (Scope = Local)
    print (greet+" "+name)

example()