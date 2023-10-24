#revision  
    #sort it
    #filter it
    # map
    #reduce
    # list comprehensions
lst = [10,20,30,40,50,60,70,80,90]
temp_in_f = {"New York" : 32,"Boston" : 75,"Los Angeles" : 100,"Chicago" : 50}
whether = {"New York" : "Snowing","Boston" :"Sunny","Los Angeles" :"Sunny","Chicago" : "Cloudy"}
#------------------------------------------------------------
lst.sort(reverse=True)  #sort
print (lst)

#------------------------------------------------------------
lsfil = list(filter(lambda x : x>= 40 , lst)) #filtering
print(lsfil)

#------------------------------------------------------------
lsmap = list(map(lambda x : x *2 , lst))    #map
print(lsmap)

#------------------------------------------------------------
import functools

lsred = functools.reduce(lambda x , y : x+y , lst)  #reduce
print (lsred)
#------------------------------------------------------------

sub_list = [i for i in lst if i > 30]               #list comprehensions
print(sub_list)
#------------------------------------------------------------
                                                    #Dictionary comprehensions
# ex : 01
temp_in_C = {key : round((value - 32) * (5/9)) for (key ,value) in temp_in_f.items() }
print(temp_in_C)
# ex : 02
good_whether = {key : value for (key,value) in whether.items() if value == "Sunny"}
print(good_whether)
# ex : 03 Using if / else
hot_or_cold = {key : "Cold" if value <= 40 else "Warm" for (key , value) in temp_in_f.items()}
print(hot_or_cold)