print("\n\n*** Days to Hours calculator ***\n\n")


def main_calc(user_in): #'user_in' is just a name for the parameter,it assigned by user_input when calling the function.
    h_in_1days = 24 #hours in a day.
    hs_in_qdays = h_in_1days * int(user_in) #hs_in_qdays = user input * 24
    return f"\n{user_input} days are {hs_in_qdays} hours.\n" #using 'return' instead of print allows you to use this function to assign as a value to a variable outside the function.Ex: testvariable = main_calc(20)

def validation_and_run():
    if user_input.isdigit(): #'is_digit' is a built in function to check if input is digit
        if int(user_input) > 0 :
            calculated_value = main_calc(user_input) #value for the parameter name of the 'main_calc' function assigned by the user_input.
            print(calculated_value) #printing the result of number of days user entered converted to hours
        elif int(user_input) == 0 :
            print("\nYou entered '0' , 0 is not valid.\n")
                #else is not needed .
    else:
        print("\nThis is not a valid number.you may entered negative number or words...!\n")
 
def termination():
    ter_req =input("\nEnter 'E' or 'e' to exit. Enter any other key to calculate again. !\n\n")
    if ter_req == "E" or ter_req == "e" :
        print("\n\n|||<-----|PROGRAM TERNIMATED|----->|||\n\n")
        exit()

while True:
    user_input=input("\nEnter number of days.! I will convert it to hours !\n\n")
    validation_and_run()
    termination()