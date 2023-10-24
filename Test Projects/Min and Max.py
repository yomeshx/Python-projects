nlist = [ 3 , 41 , -20 , 12 , 500 , -6 , 9 , 74 , -2 , 1 , -50 ,15 ,89]
largstnum = 0
mini = 0

for n in nlist :
   if n > largstnum :
      largstnum = n


print(f"\n\nLargest number is {largstnum}")


for k in nlist :
   if k < mini :
      mini = k
 

print(f"\n\nMinimum number is {mini}\n\n")