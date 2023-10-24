#               <------------- Walrus Operator ':=' ------------->

#assign values to variables as part of a larger expression
#also known as assignment expression

#Normal way
#--------------------------------------------------------------------------
# food = list()
# while True:
#     food_i = input("What food do you like? : ").capitalize()
#     if food_i == "Stop":
#         break
#     food.append(food_i)
# print(food)
#--------------------------------------------------------------------------

#Using Walrus Operator
#--------------------------------------------------------------------------
foods  = list()
while food := input ("What you wanna eat? : ") != "q":
    foods.append(food)
print(foods) #I don't know why but this doesn't work properly
