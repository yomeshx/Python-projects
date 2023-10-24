x = [7 , 12 , 45 ,20 ,16 ,34 ,100 ,90 ,80,12, 45, 67]

count =0
avg = 0
total = 0

for i in x :
    total += i
    count += 1

avg = total / count
print(f"\nTotal = {total}\nAvarage = {avg}\n\n")