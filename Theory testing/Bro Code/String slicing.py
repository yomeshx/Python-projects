name = "Yasintha Yomesh Dissanayaka"

first_name = name[:8]
middle_name = name[9:15]
last_name = name[16:]#you can leave end point empty or 
                    #bigger index larger than the actual length it still works 
skip_funny = name[0:199:2] #0(start):199(end):2(skip pattern default comes as 1)
reverse_funny = name[::-1] #reverse everything

print(first_name)
print(middle_name)
print(last_name)
print(skip_funny)
print(reverse_funny)