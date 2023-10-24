import csv

name = input("What is your name : ")
home = input("Where are you from (City or District): ")

with open("student.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])#we pre write two items in the first line (as variables) in the CSV file to work as rows#in this case name,home

#----------------- Another way -------------------------
import csv

name = input("What is your name : ")
home = input("Where are you from (City or District): ")

with open("student.csv","a") as file:
    writer = csv.DictWriter(file,fieldnames=["name","home"])#we pre write two items in the first line (as variables) in the CSV file to work as fields#in this case name,home
    writer.writerow({"home":home, "name":name})