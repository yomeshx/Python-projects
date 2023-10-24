#1.Dictionaries allows you to add items as a pair of a key and a value
#2.Dict is best for items that regularly changes its value
#you can retrieve a value of a key by dic_name[key] just like calling index of a item on the list
#if you wanna count stuff or make a simple database that contain key and values dictionary is the best data type suit for it.
#You can use FOR loop in dictionaries to,
    #1.2 Only iterate Keys in the dic    Ex:- for key in dic1.keys():
    #2.2 Only iterate values in the dic  Ex:- for value in dic1.values():
    #3.2iterate both Keys and Values in the dic Ex:- for key,value in dic1.items()

Dic_1 = {"Red" : 10 , "Blue" : 20 , "Green" : 30 , "Black" : 100}

print(Dic_1)
print(Dic_1["Red"])#prints value of red key

#you can simply add things to a dict like this
Dic_1["Yellow"] = 40

print(Dic_1)


############################################

#just like lists you can make dictionaries using a function 
DC = dict() #Creating a dictionary called DC
#then adding items to the dictionary
    #Key    #Value

DC["Apple"] = 10
DC["Orange"] = 30
DC["Banana"] =15
DC["Water Mellon"] = 50


print(DC)

############################################
#Dictionaries are not ordered in a way..so there's no index
#There is no find() function in Dicts ,but you can use "in" to find if something in your dict it will give bool value as True or False


menu = {
 #   "Green tea" : 30 ,
    "Black coffee" : 50 ,
    "Cappuccino" : 110 ,
    "High tea" : 60 ,
}

for key in menu.keys(): #' .keys() ' function is used for only take key(name) out of the dictionary
    print (key)

#in  python, dictionaries allows you to iterate 2 variables .first one is for the key and second one is for the value
for item,availability in menu.items():  # .items() function must be used in order this to happen
    print(f"we have {availability} {item}s left\n")

#You can check if there an item as Green tea in the dictionary.if there is no such a item it will show the default value as "Sorry not available"
fusion = menu.get("Green tea","Sorry not available\n") 
print(fusion)

print(menu["High tea"]) #prints the value of key "High tea"


######################################################################
cities = {

    "New Zealand" :"Wellington" ,
    "China" :"Beijing",
    "Canada" :"Ottawa",
    "Sweden" :"Stockholm",
}

cities.update({"Germany":"Berlin"}) #You can Update (Replace) a value of a existing key
                                    # or you can add an item as new using Update
cities.update({"Australia" :"Canberra"})

get_city_1 = cities.get("Germany","Not on the list")
get_city_2 = cities.get("Australia","Not on the list")
print(get_city_1)
print(get_city_2)

cities.pop("China") #Pop Uses to remove an item
print(cities)

cities.clear() #Clears everything and makes it empty
#summery of useful functions

    #menu.keys() #Only show keys in the dictionary
    #menu.values() # Only show Values in the dictionary
    #menu.get("key","Default value if there is no such a item")
    #menu.update() #to change make changes to a value of a existing key or you can use it as a another method to add a item 
    #Pop Uses to remove an item