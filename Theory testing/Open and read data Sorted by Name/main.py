namesList = []
with open("D:\\P\\Programing\\Python\\My Learning Projects\\Theory testing\\Open and read data Sorted by Name\\names.txt") as names:
    for name in names:
        namesList.append(name.rstrip())#appending lines of the text file into a list to sort it 

for sname in sorted(namesList):#sort by A-Z
# for sname in sorted(namesList,reversed=True): #sort by Z-A
    print(f"Hello {sname}")