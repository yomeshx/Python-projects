#Lvl - 1
    #1. '.sort()' method  = used with lists
    #2. 'sorted()' function = used with iterables
#Lvl - 2
    #1. sorting a List of tuples by items in a tuple
    #2. sorting a tuple of tuples by items in a tuple


#lvl - 1
# ---------------- ex: #1. sort() method  = used with lists ----------------

students_list = ["Maya","Anna","Jake","Mike","Sam","Alex","Derick"]

# students.sort()                 #sort by alphabetic order
students_list.sort(reverse = True)   #sort by reverse alphabetic order

for i in students_list:
    print(i)

# -------------- ex: #2. sort() function = used with iterables --------------

#when your items are not in a list but in other form like tuple ,you can use sorted function
students_tuple = ("Maya","Anna","Jake","Mike","Sam","Alex","Derick")

sorted(students_tuple)
# sorted_stu = sorted(students_tuple,reverse= True)     #sort reverse
for i in students_tuple:
    print(i)

#-------------------------------------------------------------------------------------


# Lvl - 2

#1. sorting list of tuples by second item in tuples

students = [("Jake","F",30),
            ("Mira","C",45),
            ("Mia","A",90),
            ("Derick","B",70),
            ("Mike","S",40),
            ("Alex","F",20)]
    #sorting by grade
grade = lambda grades : grades[1]   #grade is function object via lambda function
students.sort(key=grade)

for i in students:
    print(i)

    #sorting by their age
print("\n------------------------------------\n")
age = lambda ages : ages[2]   #grade is function object via lambda function
students.sort(key=age,reverse = True)

for i in students:
    print(i)

#-------------------------------------------------------------------------------------
print("\n------------------------------------\n")
#2. sorting a tuple of tuples by items in a tuple
students = (("Jake","F",30),
            ("Mira","C",45),
            ("Mia","A",90),
            ("Derick","B",70),
            ("Mike","S",40),
            ("Alex","F",20))
            
    #sorting by their age
age = lambda ages : ages[2]
sorted_students = sorted(students,key=age)
for i in students:
    print(i)