# Count how many letters in a string

letters = "AbcdheAcdaAdadaeeeaaaEEAAR"

dik = dict()

for letter in letters:
    if letter not in dik:
        dik[letter] = 1
    else:
        dik[letter] +=1
print(dik)
print()
for key,value in dik.items():
    print(f"There are {value} , '{key}'s")