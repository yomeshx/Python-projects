#               <--------------------- Lambda Function --------------------->

#function that are written in single line using lambda keyword
#Think it as a short cut to avoid many lines of code
 
#A lambda function is a small anonymous function(Don't have a name).
# A lambda function can take any number of arguments, but can only have one expression
#----------------ex1-------------------
double = lambda x : x*2
#fun_name#arguments: expression
print(double(5))
#----------------ex2-------------------
multiply = lambda x , y : x*y
              #arguments: expression
print(multiply(5,10))
#----------------ex3-------------------
add = lambda a ,b ,c ,d : a+b+c+d
            #arguments: expression
print(add(2,1,7,10))
#----------------ex4-------------------
full_name = lambda fname,lname : fname+" "+lname
                    #arguments: expression
print(full_name("Yasintha","Yomesh"))
#----------------ex5-------------------
age_check = lambda age : True if age >= 18 else False
            #arguments: expression
print(age_check(20))