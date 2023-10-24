#You can introduce your own error to your program
name =input("Name")
if not name :
    raise ValueError("You didn't give your name dummy !")
print (name)

# YOU can name your own error too

# if not name :
#     raise YomeshError("You didn't give your name dummy !")