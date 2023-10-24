print() #Creates empty new line .mostly used as a separator to keep things nice and tidy

print("Helo\nMy\nIs\nYomesh") # \n also makes new lines and you can use them to break one line to multiple lines

print("Hello my name is Yasintha Yomesh Dissanayake \
and i am from Kurunegala.Kurunegala is a beautiful city situated in North western province \
of Sri Lanka.It is one of the big and wellknown city .\
there are many interesting things to see in Kurunegala") # \ doesn't change the output of the print.it is used when you
#-want to print long paragraph.it tells  python that the print line is not a single line 

# \ not only in strings you can also use this in long lines of codes 

def winCheck (user,computer):#rock > scissors , scissors > paper , paper > scissors
    if (user == "r" and computer == "s") or (user == "s" and computer == "p") \
    or (user == "p" and user == "s"):
        return True