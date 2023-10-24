def greetings (greetings,fname,lname):
    print(f"{greetings} {fname} {lname}")


    #Keyword arguments
greetings(fname = "Yasintha",greetings = "Hi",lname ="Yomesh") # Order doesn't matter in keyword arguments

    #Positional arguments
greetings("Hello","Yasintha","Yomesh")