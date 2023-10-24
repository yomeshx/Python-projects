k_list = [100,45,5000,12,23,3,5,445,45,87,89,10000,500,1200,89]

largest = None

for value in k_list :
    if largest is None:
        largest = value
    elif value > largest :
        largest = value
    else:
        largest = largest
print(f"Largest is {largest}")