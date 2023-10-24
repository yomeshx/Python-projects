#*************************************************_Matching and_EXTRACTING DATA__*************************************************
#'re.search' will only return True or false value so it's great with something like if statements,but findall stores value so can be assigned to a variable.
#Instead of yes no if we actually want to capture the matches and save them in to a list (Extract to a list) we can use "re.findall()"
import re
#Ex 01

x = "I bought 2 of new iPhone 13 Pro and felt not worth the money after all considering not much difference compared to iphone 12 that i already own ."

vc = re.findall('[0-9]+',x) #This code consider any one or more number as a mach [0-9] is the parameter of the single digit
print(vc)

#Ex 02

y =re.findall("[A,E,I,O,U,T]+",x) #This code says if any character one or more in a same word it is a MATCH
print(y)# 'I' will be printed as the result