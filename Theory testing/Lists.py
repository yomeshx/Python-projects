name = ["Gota","Jonniya","Basil","Ranil","Chamal"]

lists = [5,7,"Harvey",45,"john","medusa"]

#L = name[2] +" "+"hora"
for x in name:
    print(f"{x} hora")

#list slicing
for t in name[2:]:
    print(t)


#adding new thing in to the list

lists.append(6)
print(type,print(lists[-1]))

name.append("Amarabandu")
print(name)

name.remove(name[2]) #removing "Basil" an item from the list
print(name)

#you can also do this ,
items = ["Sun glasses","Hats","Shoes","Socks","Underwear"]
print("first 3 items ",name[:3]) #this will only show first 3 items(index 0 ,1 ,2 ) until it met index 3(will not get index 3)



#ex -------- Make a list that asks 5 names and print them sorted by name

names = []

for _ in range(5):
    names.append(input("Enter Name : "))

print(names)

for i in sorted(names):
    print(i)