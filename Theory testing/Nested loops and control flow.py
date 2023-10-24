print("\n Nested loops\n")
things = ["Life" , "Music" ,"Coffee "]
akg = ["Sucks" , "is great" , "is hot"]

for t in things:
    for ak in akg:
        print(t,ak)



print("\n Control flow of loops\n")


print("\nusing 'break' in 'for loop' to prevent mika and names comes after mika in the list from printing\n")

names = ["Yomesh" ,"Ryan" ,"Mika" ,"Sadesh"]

for x in names:
    if x == "Mika" :
        break                 #if specific condition became true.. ,"break" stop the loop from running further.
    print(x)


print("\nusing 'continue' in 'for loop' to skip letter 'm' from printing in the word of 'Yomesh'\n")


x = "Yomesh"
for xi in x :
    if xi == "m":
        continue                #'continue' use for skipping something from happening if specific condition became true and continue running other things bellow that..!
    print(xi)