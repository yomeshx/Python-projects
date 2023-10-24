#functions return values when you call them with arguments(arguments are the values we give to parameters when we call functions)
#we uses return statement instead of print when we have to assign function call to a variable

def name(fname,lname):
    return fname+" "+lname

x = name("Yasintha","Yomesh") #return function is uses when you have to assign a function call to a variable

print(x)

"""Behind the scenes, Python adds return None to the end of any function
definition with no return statement. This is similar to how a while or for
loop implicitly ends with a continue statement. Also, if you use a return statement without a value (that is, just the return keyword by itself), then None
is returned."""