# CSV -Comma Separated Values
#CSV is a file format that store data like Excel sheet in separated by commas
with open("data.csv") as CSVfile:
    for line in CSVfile:
        person = line.rstrip().split(",") #split function split strings by given symbol and stores parts inside a list
        # print(person) #Test -this will print the lists containing of persons data
        print(f"Name: {person[0]} | Gender: {person[1]} | Phone: {person[2]}")

#----------- Alternative for code above -----------#
print()#new line

with open("data.csv") as CSVfile:
    for line in CSVfile:
        name,gender,phone = line.rstrip().split(",") #Variable will be assigned with splitted values by order you gave them
        print(f"Name: {name}  Gender: {gender}  Phone: {phone}")

#----------- More advanced sorted version ------------
print()#newline

dataList = []
with open("data.csv") as CSVfile:
    for line in CSVfile:
        name,gender,phone = line.rstrip().split(",")
        student ={"Name":name,"Gender":gender,"Phone":phone}
        dataList.append(student)

def SortBy(student):
    return student["Gender"]#you can sort things by different values, try "Name" or "Phone"

for student in sorted(dataList,key = SortBy):
    print(f"{student['Name']} is {student['Gender']}. Phone: {student['Phone']}")#attention - note that we use single quotes(') inside and ("") in the out of the f


#--------------------Using lambda instead of creating sort function-----------------------
print()
dList = list()
with open("data.csv") as file:
    for line in file:
        data=line.rstrip().split(",")
        lib = {"Name":data[0],"Gender":data[1],"Phone":data[2]}
        dList.append(lib)

for person in sorted(dList,key = lambda person: person["Name"],reverse=True):
    print(f"{person['Name']} is a student of OUSL {person['Phone']}")