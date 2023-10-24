#"a" allow you to write strings multiple times to the same file .it adds things to the file but doesn't override the file you writing unlike 'w' when running the code multiple times

fileD = open("D:\\P\\Programing\\Python\\My Learning Projects\\Theory testing\\File IO\\Write\\data_a.txt","a")

for _ in range(5):
    name = input("Enter Name :| ")
    fileD.write(f"{name}\n")
fileD.close()