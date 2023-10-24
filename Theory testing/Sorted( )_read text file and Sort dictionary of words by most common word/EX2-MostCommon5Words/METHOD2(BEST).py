
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
MCW = sorted([(v,k) for k,v in word_count.items()],reverse=True)
Most_used_5_words = MCW[:5]
print(f"Most Used 5 Words Are {Most_used_5_words}")