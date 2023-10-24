#Sorted() allow you to sort items in a list or items in a Tuple.
#Even there's no sorted() method in dictionaries you can make list of tuples and then sort it and convert back to and dictionary.like the ex below

dic = {"Coffee":40,"Cappuccino":60,"Green Tea":20} 
print("Original : ",dic.items()) #Output dict as a list: dict_items[("Coffee",40),("Cappuccino",60),("Green Tea",20)]
print("Sorted : ",sorted(dic.items())) #Sorted dict as a list.
#You can sort the dict like above and convert it again to a dictionary
print("Convert Back 2 a Dict : ",dict(sorted(dic.items())))

print("<<_____________________Next_____________________>>\n")

####second ex: ####

v_dict = dict()

v_dict["Goal"] = 20
v_dict["Nail"] = 5
v_dict["Whale"] = 79
v_dict["Bear"] = 89
v_dict["Julia"] = 69

print(v_dict)

vl_dict = v_dict.items() #list of items in V_dict as tuples
print(f"Not sorted vl_dict is {vl_dict}")
vls_dict = sorted(vl_dict)#sorted list of items in V_dict as tuples
print(f"Sorted vl_dict is {vls_dict}")
vlsd_dict = dict(vls_dict) #Converting vls_dict back into an dictionary
print(f"Sorted and converted final result {vlsd_dict}")

print("<<<----------NEXT---------->>>\n\n")

## how 2 sort values instead of keys.

dic = {"Hello":10,"Bye":20,"aloona":12,"Ok":17,"Aloha":80}
lit = list()
for k,v in sorted(dic.items()):
    lit.append((v,k))
print(lit)#original lit
print(sorted(lit)) #Sorted to min to max
print(sorted(lit,reverse = True)) #Sorted to max to min                         #You can reverse the order with ',reverse = True'inside the function