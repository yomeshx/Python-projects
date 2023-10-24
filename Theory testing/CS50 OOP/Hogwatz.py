# #this is lesson we modify the code stage by stage making updates to the code in different stages with the video lesson

# #STAGE - 01 ---------------------------------------------------------------------------------------------------------------------------
# class Student:
#     ...         # 3 dots is a valid place holder

# def main():
#     student = get_student() #assigning the return value (updated class with new attributes) of the 'get_student' function to a variable called 'student'             
#     print(f"{student.name} from {student.house} .") #calling class attributes to retrieve stored data 

# def get_student():
#     student=Student()                       #assigning 'Student' class into an variable
#     student.name= input("Your Name : ")     ## creating new attributes inside the class and assigning values to them
#     student.house= input("Your House : ")   #   (this is how you add new attributes to the class)
#     return student                            #returning updated class with new attributes

# if __name__ == '__main__':                   #FAILSAFE: making sure this is the main script
#     main()

# # STAGE- 02 ---------------------------------------------------------------------------------------------------------------------------
# class Student:
#     def __init__(self,name,house): ## __init__ is a instance method. you define this method when you want to initialize contents of a object from a class
#         self.name = name                #self give you access to the current object you just created
#         self.house = house
        

# def main():
#     student = get_student() #assigning the return value (updated class with new attributes) of the 'get_student' function to a variable called 'student'             
#     print(f"{student.name} from {student.house} .") #calling class attributes to retrieve stored data 

# def get_student():
#     name = input("Name : ")
#     house = input("house : ")
#     return Student(name,house)       #more standardize way to pass arguments/data to the class than stage -1
# if __name__ == '__main__':                   #FAILSAFE: making sure this is the main script
#     main()

# # STAGE- 03 ---------------------------------------------------------------------------------------------------------------------------
# class Student:
#     def __init__(self,name,house): ## __init__ is a instance method. you define this method when you want to initialize contents of a object from a class
#         if not name:
#             raise ValueError("Missing Name!")
#         if house not in ["gryffindor","hufflepuff","ravenclaw","slytherin"]:
#             raise ValueError("Invalid House")
#         self.name = name                #self give you access to the current object you just created
#         self.house = house
        

# def main():
#     student = get_student() #assigning the return value (updated class with new attributes) of the 'get_student' function to a variable called 'student'          
#     print(f"{student.name} from {student.house}") #calling class attributes to retrieve stored data 

# def get_student():
#     name = input("Name : ")
#     house = input("house : ").lower()
#     return Student(name,house)       #more standardize way to pass arguments/data to the class than stage -1
        
# if __name__ == '__main__':                   #FAILSAFE: making sure this is the main script
#     main()

# # STAGE- 04 ---------------------------------------------------------------------------------------------------------------------------
# class Student:
#     def __init__(self,name,house,spell): ## __init__ is a instance method. you define this method when you want to initialize contents of a object from a class
#         if not name:
#             raise ValueError("Missing Name!")
#         if house not in ["gryffindor","hufflepuff","ravenclaw","slytherin"]:
#             raise ValueError("Invalid House")
#         self.name = name                #self give you access to the current object you just created
#         self.house = house
#         self.spell = spell      
          
#     def __str__(self):
#         return f"{self.name} from {self.house}"

# def main():
#     student = get_student() #assigning the return value (updated class with new attributes) of the 'get_student' function to a variable called 'student'          
#     print(student)

# def get_student():
#     name = input("Name : ")
#     house = input("House : ").lower()
#     spell = input("Spell : ")
#     return Student(name,house,spell)       #more standardize way to pass arguments/data to the class than stage -1
        
# if __name__ == '__main__':                   #FAILSAFE: making sure this is the main script
#     main()


# # STAGE- 05 ---------------------------------------------------------------------------------------------------------------------------
# class Student:
#     def __init__(self,name,house,spell): ## __init__ is a instance method. you define this method when you want to initialize contents of a object from a class
#         if not name:
#             raise ValueError("Missing Name!")
#         if house not in ["gryffindor","hufflepuff","ravenclaw","slytherin"]:
#             raise ValueError("Invalid House")
#         self.name = name                #self give you access to the current object you just created
#         self.house = house
#         self.spell = spell      
          
#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     def charm(self):
#         match self.spell:
#             case "Dog":
#                 return "Bgruhh..Bgrruu"
#             case "Lion":
#                 return "grrraaaaaaah"
#             case "Cat":
#                 return "meeoow"
#             case _:
#                 return "Spell unknown"
# def main():
#     student = get_student() #assigning the return value (updated class with new attributes) of the 'get_student' function to a variable called 'student'          
#     print("Expecto Patronum!")
#     print("student.charm()")

# def get_student():
#     name = input("Name : ")
#     house = input("House : ").lower()
#     spell = input("Spell : ")
#     return Student(name,house,spell)       #more standardize way to pass arguments/data to the class than stage -1
        
# if __name__ == '__main__':                   #FAILSAFE: making sure this is the main script
#     main()


# # STAGE- 06 -------Learning about property--------------------------------------------------------------------------------------------------------------------
# class Student:
#     def __init__(self,name,house): ## __init__ is a instance method. you define this method when you want to initialize contents of a object from a class
#         self.name = name                #self give you access to the current object you just created
#         self.house = house
          
#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
#     @property
#     def name(self):
#         return self._name
#     @name.setter
#     def name(self,name):
#         if not name:
#             raise ValueError("You didn't enter the name!")
#         self._name = name
        
#     @property
#     def house(self):
#         return self._house
    
#     @house.setter
#     def house (self,house):
#         if house not in ["gryffindor","hufflepuff","ravenclaw","slytherin"]:
#             raise ValueError("Invalid House")
#         self._house = house

# def main():
#     student = get_student() #assigning the return value (updated class with new attributes) of the 'get_student' function to a variable called 'student'          
#     # student.house = "Lama" #this is the mistake that will detect by @property
#     print(student)

# def get_student():
#     name = input("Name : ")
#     house = input("House : ").lower()
#     return Student(name,house)       #more standardize way to pass arguments/data to the class than stage -1
        
# if __name__ == '__main__':                   #FAILSAFE: making sure this is the main script
#     main()


# STAGE- 07 -------Making the code tidy by putting everything related to the student into the class , like user inputs in this case using class method ------------------------
class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house
          
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod    #class method
    def get(cls):
        name = input("Name : ")
        house = input ("House : ")
        return cls(name,house)
    
def main():
    student = Student.get()
    print(student)


if __name__ == '__main__':                   #FAILSAFE: making sure this is the main script
    main()
