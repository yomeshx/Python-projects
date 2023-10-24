#                <---------------| map Function |--------------->

#map function used to apply a function to each item in a iterable 
    #   map (function , iterable)

#ex 01
#---------
store =[("Shirt",20.00),
        ("Pants",25.00),
        ("Jacket",50.00),
        ("T-shirt",15.00)]      #Iterable

to_euros = lambda data: (data [0],data [1]*0.82)    #function

store_dollars = list(map(to_euros, store))      # using map () and storing it in a list 

for i in store_dollars:
    print(i)

# ex2
# ---------

a = [1,2,3,4,5,6,7,8,9]

newList = list(map(lambda x: x+3 ,a))
print(newList)

#ex 3
#----------

b = [11,20,31,40,53,61,73,82,90,101]

list_in = list(filter(lambda x: x%2 == 0 ,b))
print(list_in)

#ex 4

c = [20,94,75,16,46,12,34,90,33,11]

lst_less_than_30 = list(filter(lambda x : x < 30 , c))
print(lst_less_than_30)