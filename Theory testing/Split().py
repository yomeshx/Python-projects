sentence = "I love my country Sri Lanka, nobody can convince me to believe it's not the best county for me"
word_list = sentence.split() # when you assign split to a single variable its stored in list format
print(word_list)

country = "Sri Lanka"
first,last = country.split(" ") #when you know how many parts your string gonna be split into you can assign those peaces to multiple variable
### split() function can split strings in to peaces by empty spaces . and it's a built in method to string data type
### and store those words inside of a list
### split function split string by spaces by default,but you can split by anything you want
        #ex: 
            #line = "Sorekblak fafafakjloiok"
            #listW = line.split("k")
            #print(listW)

            #*****--OUT PUT--*****#

            #["Sore","bla","fafafa","jloio"]
