phone_number ="078-4563925"

for digit in phone_number:
    if digit =="-":
        continue
    print(digit,end = "") #  #end=""  makes possible to print iterating items in one line 

#pass also like continue does nothing,it just act as a place holder

for l in range(0,11):
    if l == 7:
        pass
    else:
        print(l)