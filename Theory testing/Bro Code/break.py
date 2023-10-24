#Break is to stop a loop from iterating further
list_ = [7,4,2,6,1,8,2,6,9,12,2,3,1,4,6]

for i in list_:
    if i == 12: #this loop will break when i became 12
        break
    else:
        print(i)