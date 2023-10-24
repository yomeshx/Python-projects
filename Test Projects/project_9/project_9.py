import os
os.chdir("D:\P\Programing\Python\My Learning Projects\Test Projects\project_9") #To change directory to project folder

open_req = None
di = dict()             #Dictionary
a = None
def whole_text(name): #{to print whole text file
    name = open(name)
    for line in name:
        print (line)  #             }
while True:
    open_req = input("Input file name : \n# ")
    if open_req == "stop" or open_req == "STOP" or open_req == "Stop":          #Termination
        break
    elif len(open_req) < 1 :
        open_req = "clown.txt"    #default file if user doesn't input a file to run
    file = open(open_req)           #Opening the file
    for line in file:
        line = line.rstrip()        #to remove additional white space in the right side
        line = line.split()         #puting words in the line of text in to a list
        for word in line:           #iterating word by word in side the list
            di[word] = di.get(word,0) +1    #Getting current value and adding if word is repeating , If the word is new get() will add it as a new item to the dict and give value as 1

            # if not word in di:          #{
            #     di[word] = 1
            # else:                       #     Does the same Thing above
            #     di[word] += 1           #                                     }
    print("\n")
    whole_text(open_req)
    print(f"count :\n{di}")
    print(di)

    #finding the most common word in the dictionary (text file)

    L_value = 0 
    L_key = None
    for key,value in di.items() : #Will find out what word is the most used in the text file
        print("\n",key,value)
        if L_value < value: 
            L_value = value
            L_key = key
        
            
    print(f"Most common word in the  text file is '{L_key}'.it used {L_value} times in the text.")