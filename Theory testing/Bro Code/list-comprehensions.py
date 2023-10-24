#List Comprehensions are a way to make a list in less syntax than normal way
# this creates a list using an expression
#So you can skip writing loops and sextain lambda-functions

#STRUCTURE:
#1.source list = [Bla,bla bla,blu,bla]
#2.new_list = [i for in source_list if i <= value]

# Ex : 01
#-----------------------------------------------------------
#normal way
lst = []
for i in range(1,11):
    lst.append (i*i)
print(lst)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]        Output
#-----------------------------------------------------------

#Using list comprehensions
square = [i * i for i in range (1,11)]
print(square)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]        Output
#-----------------------------------------------------------

# Ex : 02   -  Adding values that are greater than or equal to 50 in to a list
#-----------------------------------------------------------
data = [80,45,100,67,32,98,12,56]

#normal way
processed_data = list(filter(lambda x : x >= 50 , data))
print(processed_data)

#Using list comprehensions
pro_data = [i for i in data if i>= 67]
print(pro_data)

# Ex : 03   #determine Fail or Pass by if marks are lower 35
#-----------------------------------------------------------
points = [14,45,67,23,89,45,23]
fail_pass = [(i,"Pass") if i>= 35 else (i,"Fail") for i in points]
print(fail_pass)