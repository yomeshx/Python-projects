#what if the you need to take a address of a person from a CSV file that is also has ","
#   there is a library called CSV to make handling csv file easy.and has a method specially to solve this situation
import csv

dList = list()
with open("data.csv") as file:
    reader = csv.reader(file)
    for name,address,phone in reader:
        dList.append({"Name":name,"Address":address,"Phone":phone})

for person in sorted(dList,key = lambda person: person["Name"],reverse=True):
    print(f"{person['Name']} is from {person['Address']}")