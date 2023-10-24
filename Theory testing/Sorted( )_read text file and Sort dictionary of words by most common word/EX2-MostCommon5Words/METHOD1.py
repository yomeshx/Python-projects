#Finding most used 5 word in a text file 
import os

from numpy import append
os.chdir("D:\P\Programing\Python\My Learning Projects\Theory testing\Sorted( )_read text file and Sort dictionary of words by most common word")

txt_file = open("Coldplay.txt")
word_count = dict()
lst = list()
lst_r_o = list()
for line in txt_file:
    line = line.rstrip()
    line = line.split()
    for word in line:
        word_count[word] = word_count.get(word,0)+1
print(f"TEST#1-->{word_count}")
for k,v in word_count.items():
    lst.append((v,k))
print(f"TEST#2-->{lst}")
lst_r = sorted(lst,reverse=True)
print(f"TEST#3-->{lst_r}")
for v,k in lst_r:
    lst_r_o.append((k,v))
print(f"TEST#4-->{lst_r_o}")
Most_used_5_words = dict(lst_r_o[:5])
print(f"Most Used 5 Words Are {Most_used_5_words}")

