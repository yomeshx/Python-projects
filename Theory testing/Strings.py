from tokenize import String

#Useful string functions
Name = "Yasintha Yomesh Dissanayaka"

print(type(Name))   #can use to check the the type
print(Name.find("Y"))   #Index of the letter or start of the string you are looking for,if theres no match it will return negative value
print(Name.capitalize()) #make first character in the sentence capital
print(Name.upper())    #Make everything uppercase
print(Name.lower())     #Make everything Lowercase
print(Name.isdigit())   #Check the type and if the type is digit Give boolean value True ,if not return False 
print(Name.replace("s","$"))    #Replace 's' with '$'
print(Name.count("s"))          #Count how many 's' in the string
print(Name*3)               #prints Name 3 times

#Strings are immutable,You can make new modified string using the old one but original one cant be changed 
    #Ex:
        # word = "I Am the thinking tank"
        #word.replace("I","Z")  ##wont work because of immutability,
                                ##word = word.replace("I",Z) will work because it doesn't make changes 2 the original one
                                ##-only replacing the whole string with the modified one.just like the line below
        # modified_word = word.replace("i","a") #Will work because of it is and copy not the original

        # print(x)

word = 'Knowledge'

print(f"The character is '",word[2],"'")

print("Length of the word is ",len(word))



#Using loops to look at a string

a_word = "Wizard"
reps = len(a_word)

for i in a_word :
    print(i)
    print(f"\nreps no: {reps}\n")
    reps -= 1


word = "State of art technology"
print(word[2])
print(word[-1]) #LAST LETTER #Minus numbers will index backward (Right to left)


# we can specify what part of the string we should target. by using ':' and index numbers


# word [:18] -this will specify every thing untill 18th index,but not 18 because of 0
#even there are no 18 charectors in your string it will show the full string 
print(word[:18])

#This will specify everything after index 2
print(word[2:])

#this will specify everything inside the string
print(word[:])



name = "Yomesh Dissanayaka"



#'.find' function helps you to find index of the thing you want

print(name.find("D"))



#you can replace a specific part of a string with replace function.
# ,in order to do that you need to give it what you wanna replace as the first
#  and the new string part you wish to replace with as your second .ex:("s","S"))

print(name.replace("s","S"))


#".startswith function help you to target a string if it start with what we gave .. expect answer to be true because its a bool

print(name.startswith("Yome"))

test_n = "                Tropical paradise                 "

name.lstrip #this will clear all the empty space in the left side
name.rstrip #this will clear all the empty space in the right side
name.strip #this will clear the empty space in the beginning and at the end of the string .this doesnt mean it clear spaces middle of the string
print(test_n.strip())
print(test_n.rstrip())
print(test_n.lstrip())