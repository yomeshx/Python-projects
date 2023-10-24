#there is a new syntax called "match" in latest versions of python that implement same idea of a 'if' condition
#note: in other languages 'match' is called 'switch'
#Similar to if, elif, and else statements, match statements can be used to conditionally run code that matches certain values.

# Normal way (Using if )

#----------Longer version-------------
name = input("Enter your name : ").lower()

if name == "harry":
    print("Gryffindor")
elif name == "hermione":
    print("Gryffindor")
elif name == "ron":
    print("Gryffindor")
elif name == "draco":
    print("Slytherin")
else:
    print("Who?")
#----------shorter version-------------
name = input("Enter your name : ").lower()

if name == "harry" or name == "hermione" or name == "ron":
    print("Gryffindor")
elif name == "draco":
    print("Slytherin")
else:
    print("Who?")


#Using Match

#---Longer version---
name = input("Enter your name : ").lower()
match name:
    case "harry":
        print("Gryffindor")
    case "hermione":
        print("Gryffindor")
    case "ron":
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case _: #'case _' works like 'else' 
        print("Who?")
#---Shorter version---
name = input("Enter your name : ").lower()
match name:
    case "harry" | "hermione" | "ron" : #in match we use "|" symbol instead of "or"
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("Who?")

#note: 
# Notice the use of the _ symbol in the last case (this is called default case).cases doesn't match then this will be the default, resulting in similar behavior as an else statement.

# A match statement compares the value following the match keyword with each of the values following the case keywords.
#-In the event a match is found, the respective indented code section is executed and the program stops the matching.