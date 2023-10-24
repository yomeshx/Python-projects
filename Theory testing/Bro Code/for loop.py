print("Zero to 100 ")
for x in range (0,100+1): #Or 0,101
    print (x)
print("0 to 100 but skip one by one")
for y in range (0,100,2):
    print(y)
print("0 to 100 backward ")
for z in range (100,0,-1): #using -1 to the step will  count down
    print(z)

import time                     #Time module
for z in range (100,0,-1): #-1 makes it count-"down"
    print(z)
    time.sleep(1)