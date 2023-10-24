#Tuples are immutable . once you create them you cant make any changes to them,only can retrive things from them .
#You can't use .sort() , .append() or .reverse() functions in tuples that we used in lists.
#1.you can give two variable inside a tuple as the left side and assign 2 values to em #ex: (x,y) = (4,"nicole") ----> x will be 4 and y will be "nicole".
#2.Tuples are comparable ! .The comparison operators work with tuples are other sequences.if the first item is equal python goes on to the next element,and so on until it finds elements that differ.
   #this is a cool feature only python offers
#3.but why use tuples instead of a list? the answer is tuples are simple so they are faster,if you want to multiple items that should not be change by
 #mistake, you should use a tuple.another reason is to make a temporary list of items to test something.
#point 1

(x,y) = (9," is cool")
print(f"x --> {x}")
print(f"y --> {y}")
print(x,y)

#point 2

a = (1,200,20) > (1,200,16) #python will skip equal valued couples until find value couple with difference.in this example python will skip 1s and 200s until 20 and 16 . 
print(a)                    #this will comepare 20 > 16 and will give a boolien value as "True" because 20 is bigger than 16

b = (30,10,5) < (30,4,17000) # will skip 30 and campare 10 < 4  and give output as "false" because 10 is larger than 4. wont campare 5 < 17000 
print(b)

c = ("Aruna","Bimal","Jehan") < ("Aruna","Ishi","Nims")#will skip "Aruna" and will campare "Bimal" < "Ishi"  and will give output as "True" because of ABCD...Z order 
print(c)
                                                    # *Note: simple letters consider bigger than capitals in python
                                                    # D =   "a" > "A"
                                                    # print(f" a > A is {D}")

d = ("Jones","Sally") > ("Jones","Sam") # will skip "Jones" then compare "Sally" > "Sam". in this "S" and "a" will be skipped and will campare "l" > "m" and output will be 'false' 
                                        #-because of "m" comes after the "l" in the ABC..Z order.
print(f"d is '{d}'")

#You can turn a dictionary to a list of tuples like this 

dic = {"Coffee":40,"Cappuccino":60,"Green Tea":20} 
print("Original : ",dic.items()) #Output dict as a list: dict_items[("Coffee",40),("Cappuccino",60),("Green Tea",20)]
print("Sorted : ",sorted(dic.items())) #Sorted dict as a list.
#You can sort the dict like above and convert it again to a dictionary
print("Convert Back 2 a Dict : ",dict(sorted(dic.items())))