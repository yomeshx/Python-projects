# # # The function 'open()' gives permission to read or do things to the file, 
#     #***must put file name inside "" in the function brackets just like we do with strings, -->|
#         #ex : open("V.txt") 
# #Note:this examples uses functions and techniques in the strings because our file is a text document



# ##(1) One methode to read files is using a for loop(reading one line by line).

# print("\nFirst method to read a file\n")
# trx = open("Coldplay_Hymn for the Weekend lyrics.txt") #File

# count = 0

# for line in trx :
#     count += 1    
# print(f"Line count : {count}")


# #(2) another methode is to 'read the whole file' at once.Using 'read()' function


# print("\nSecond method to read a file\n")

# kill = open("Coldplay_Hymn for the Weekend lyrics.txt")

# red = kill.read()

#  #print(len(red))    #can use len() to know how much carrectors in the file


##########################################################################################


# #***Searching through a file***

# print("1example : Searching through a file")

# find_da_word = red.find("from me") #finding the index of 'from me'NOTE: this will show the index of  starting charrector in the string(in this ex'f' in from me)
# print(find_da_word)

####################

print("2example : Searching through a file")

f_handle = open("Coldplay_Hymn for the Weekend lyrics.txt")
for line in f_handle:
    line=line.rstrip() #to delete extra empty line created by print function

#(1)one methode to read a line
    if line.startswith("When"): #will print all the lines starts with "when"
        print(line)
    elif line.endswith("sky"):
        print(line[17:])
    else:
        continue
#(2)Another methode to search and print a
    if not line.startswith("W"): #print all the lines starts with W
        continue
    else:
        print(line)