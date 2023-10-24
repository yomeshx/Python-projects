
#Not using get
count = dict()
name_list = ["Kaputu","Kaak","Kaak","Kaak","Basil","Basil","Basil","Basil","Kaputu","Kaak","Kaak","Kaak","Basil","Basil","Basil","Basil"]

for name in name_list:
    if name in count:
        count[name] = count[name] + 1
    else:
        count[name] = 1
print(count)

#Using get
colors = ["Red","Green","Yellow","Green","Brown","Red","Yellow","White","Green","Yellow","Orange","Black"]
count_r = dict()

for color in colors:
    count_r[color] = count_r.get(color,0) + 1

print(count_r)

#Counting Words in a String
sentence ="Hello Hello I cant Here Here you now now"
word_list = sentence.split()
word_dict = dict()
for word in word_list:
    word_dict[word] = word_dict.get(word,0) + 1
print(word_dict)