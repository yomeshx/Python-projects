#Use to filter stuff in a list or some shit like that
#commonly use map and lambda functions in this

a = [11,20,31,40,53,61,73,82,90,101]

list_in = list(filter(lambda x: x%2 == 0 ,a))
print(list_in)

#ex 4

c = [20,94,75,16,46,12,34,90,33,11]

lst_less_than_30 = list(filter(lambda x : x < 30 , c))
print(lst_less_than_30)


#ex
b = [11,20,31,40,53,61,73,82,90,101]

lshift = list(filter(lambda x : x>50,b))

print(lshift)



rshift = list(filter(lambda y : y>70,b))
print(rshift)

n_shift = list(filter(lambda z : z<50 ,b))
print(n_shift)