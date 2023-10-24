import os
os.chdir("D:\P\Programing\Python\My Learning Projects\Test Projects\Open file and count how many words")

da_file = input("Enter the file name \n")
f_handle = open(da_file)
count_words = dict()
for line in f_handle:
    words_list = line.split()
    for word in words_list:
        count_words[word] = count_words.get(word,0) + 1
print(count_words)

#code to find the biggest value in the dictionary
big_key = None
big_value = None

for key,value in count_words.items():
    if big_value is None or value > big_value:
        big_value = value
        big_key = key

print(f"{big_key} : {big_value}")