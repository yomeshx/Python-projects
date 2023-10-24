import random

x = random.randint(1,6)
# y = random.random()

my_list = ["Rock","Paper","Scissors"]
random.shuffle(my_list) #you can shuffle using random.shuffle 
z = random.choice(my_list)

print(z)