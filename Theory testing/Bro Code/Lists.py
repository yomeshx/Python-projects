food= ["coffee","Cake","Biscuits","sausage","Beer"]
#1.for loop to iterate items in a list
for x in food:
    print(x)

#2.built-in methods in lists
food.append("Apple Pie") #Adding new item to the list #this will add to the end of the list
print(food)
food.remove("Biscuits") #Removing item 'Biscuit'
print(food)
food[0] = "sushi" #replacing 0 index item(coffee) with "sushi"
print(food)
food.insert(2,"Chicken Burger") #insert a value to a given index
print(food)
#food.sort()        #Will sort the list
#food.clear()       #Will clear everything in the list and will be empty