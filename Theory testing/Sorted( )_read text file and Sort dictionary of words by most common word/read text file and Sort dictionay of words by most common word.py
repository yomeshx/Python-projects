#Sorting by value max to min and min 2 max

#METHOD 1
import os
os.chdir("D:\P\Programing\Python\My Learning Projects\Theory testing\Sorted( )_read text file and Sort dictionary of words by most common word")

list_ = list()
list_2 = list()
dic_words = dict()
f_hand = open("Text x.txt") #opening the text file

for line in f_hand:
    line = line.rstrip()#deleting empty spaces
    line = line.split() #making list of words
    for word in line :
        dic_words[word] = dic_words.get(word,0)+1 #if word already present in the dictionary it will add +1 to the value ,if not it will word will be added as a key and value will be 1
print(f"_Test__ Word dic : {dic_words}")#for testing purposes

for k,v in dic_words.items():
    list_.append((v,k)) #append to a list as tuples but in value key order. 
print("sorted list by least common word: ",sorted(list_)) #sorted list by least common word(value key order)
print("sorted by Most common word : ",sorted(list_,reverse = True))#sorted by Most common word (value key order)

r_dic_words = dict(sorted(list_,reverse = True))#Converting sorted by Most common word in value key order to a dictionary
print("sorted dic of list : ",r_dic_words)

for v,k in r_dic_words.items():
    list_2.append((k,v))#adding back to a list to make finale version of dictionary but key value in right order
print("_Test__ list_2 : ",list_2)#testing purposes

sr_dic_words = dict(list_2) #converting finale ordered list in to a dictionary
print(f"Final sorted dictionary \n{sr_dic_words}") #sorted by value dictionary in key-value order..

#There is a another way to make do all the work above in a single code
#METHOD 2


print("\n\n<<---------BEST WAY_______>>\n\n")

price_board = {
    "Milk powder" : 1700,
    "Sugar" : 80,
    "Petrol" : 400,
    "Soup" : 250,
    "Tooth paste" :150
}                            #Dictionary


#The magic line that does sorting by value in method 1 in one single line
min2max = sorted ( [ (v,k) for k,v in price_board.items() ] ) #sorted by min to max
print(min2max)
max2min = sorted([(v,k) for k,v in price_board.items()],reverse = True) #sorted by max to min
print(max2min)