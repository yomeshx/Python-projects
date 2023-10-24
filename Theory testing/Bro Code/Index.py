#index operator "[]" = gives access to a sequence's element (Str,list,Tuples) 



name = "Yomesh Dissanayaka"
# name = name.upper()
if name[1].islower():
    print("Yes it's the letter is lower")
else:
    print("Yes it's the letter is Upper")
fname = name[0:7].upper()
print(fname)