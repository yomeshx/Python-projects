#Just like list-Comprehensions this creates a dictionary using an expression
#Just like list-Comprehensions you can skip writing loops and sextain lambda-functions


#======================= Source =======================
cities_in_F = {"New York" : 32,"Boston" : 75,"Los Angeles" : 100,"Chicago" : 50}   #Cities in Celsius
whether = {"New York" : "Snowing","Boston" :"Sunny","Los Angeles" :"Sunny","Chicago" : "Cloudy"}
#======================================================

#STRUCTUREs
#1. dictionary = {key : 'expression' for (key,value) in 'iterable'}
#2. dictionary = {key : 'expression' for (key,value) in 'iterable' if conditional}
#3. dictionary = {key : (if/else) for (key,value) in 'iterable'}
#4. dictionary = {key : function (value) for (key,value) in 'iterable'}

#01 --------------------------------------------------------------------------------------------------
cities_in_C = {key : round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
                        #f --> C formula
print(cities_in_C)

#02 --------------------------------------------------------------------------------------------------

good_whether = {key : value for (key,value) in whether.items() if value == "Sunny"}
print(good_whether)

#03 --------------------------------------------------------------------------------------------------

hot_or_cold = {key : "Cold" if value <= 40 else "Warm" for (key , value) in cities_in_F.items()}
print(hot_or_cold)

#04 --------------------------------------------------------------------------------------------------
#Basically putting if else methods inside a function and calling it rather than directly giving it like ex: #03 
def check_temp(temp):
    if temp >= 70:
        return "Hot"
    elif 69 >= temp >= 40:
        return "Warm"
    else :
        return "Cold"
hot_or_cold = {key : check_temp(value) for (key , value) in cities_in_F.items()}
print(hot_or_cold)