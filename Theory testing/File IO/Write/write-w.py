                                                                                        #note: "w" creates a file and allows you to write into it.but it overrides the file and create a new one next time when you run the code again
sheet = open("D:\\P\\Programing\\Python\\My Learning Projects\\Theory testing\\File IO\\Write\\data_w.txt","w") #'w' is saying we are opening this file for writing, you can type 'r' for only reading
for _ in range(5):
    sheet.write(input("Enter Name : ")+"\n")

sheet.close()