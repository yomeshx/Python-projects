# #NormalCode : Lets say we do input error checking in the beginning of the code 
# class Student:
#     def __init__(self,name,faculty):
#         if faculty not in ["medical","science","engineering","commerce","technology"]:
#             raise ValueError("Invalid Faculty")
#         self.name = name
#         self.faculty = faculty

#     def __str__(self):
#             return f"{self.name} from {self.faculty}"
        
# def main():
#     student = get_userInfo()
#     print(student)

# def get_userInfo():
#     name= input("Enter Name: ")
#     faculty = input("Your Faculty: ").lower()
#     return Student(name,faculty)

# if __name__ == '__main__':
#     main()

#---------------------------------------------------------------------------------------------
# #TheBug : everything is great until programmer set value of a variable accidentally somewhere like main().it will bypass User input validation.

# class Student:
#     def __init__(self,name,faculty):
#         if faculty not in ["medical","science","engineering","commerce","technology"]:
#             raise ValueError("Invalid Faculty")
#         self.name = name
#         self.faculty = faculty

#     def __str__(self):
#         return f"{self.name} from {self.faculty}"
        
# def main():
#     student = get_userInfo()
#     student.faculty = "Kasippu" #*** this bypass the user input validation above and will be accepted even value is invalid
#     print(student)

# def get_userInfo():
#     name= input("Enter Name: ")
#     faculty = input("Your Faculty: ").lower()
#     return Student(name,faculty)

# if __name__ == '__main__':
#     main()

#---------------------------------------------------------------------------------------------
#fix with property : we can make sure such mistakes are prevented by using property
    #(expected result of this is value error.because we use invalid faculty)

class Student:
    def __init__(self,name,faculty):
        self.name = name
        self.faculty = faculty #setter you created bellow will get called anytime 

    def __str__(self):
            return f"{self.name} from {self.faculty}"
    
    @property   #Getter (in java)
    def name(self):
        return self._name
    
    @name.setter    #Setter (In java)
    def name(self,name):
        if not name:
            raise ValueError("Missing name !")
        self._name = name


    @property               #Getter ( Java)
    def faculty(self):
         return self._faculty #Pro tip : programmers user _ before something to remind themselves don't change/mess with it
    
    @faculty.setter          #Setter (in java)
    def faculty(self,faculty):
        if faculty not in ["medical","science","engineering","commerce","technology"]:
            raise ValueError("Invalid Faculty")
        self._faculty = faculty

def main():
    student = get_userInfo()
    # student.faculty("Kasippu") #*** this will get detected by @Property and won't bypass the validation check now and will raised as a error when checking
    print(student)

def get_userInfo():
    name= input("Enter Name: ")
    faculty = input("Your Faculty: ").lower()
    return Student(name,faculty)

if __name__ == '__main__':
    main()

# Note :(I not sure about this, look into more about property(or getters and setters) on the internet.)
    # As i understood it help us make sure to not mess up the important parts of the code.
    # We can create these property and setters to detect when we try to set something and it will make sure it is done right way
    # in this example here we try to set student.faculty to wrong thing .but it detects we trying to set faculty in the @property and runs validation in @... .setter