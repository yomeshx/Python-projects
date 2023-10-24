#part 1. : Making and using functions 

print("\n\n\nDate and time calculator\n\n\n") #another way to concatenate different types of data with a string. 'f' stands for 'format' 

calculation_to_units = 24
name_of_units = "hours"




def days_to_units(num_of_days): #function- 'def' = define ,'days_to_units' = name of the function , '(parameter)'
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}\n" # 'f' - format | '{}' - to concatenate different data types together without having to converting to same data type and '+' signs.


def check_execute():

    try:

        if user_input.isdigit():
            if user_input > 0 :
                print(calculated_value)
            elif user_input == 0:
                print("You entered 0. '0' is not valid.\n")
            else:
                print("You may have entered negative value.Negative values are not valid\n")
        else:
            print("This is not a number.words are not acceptable !!!\n")

    except ValueError:
        print("Something went wrong please try again !\n")


while True:
    user_input = int(input("Enter a number of days we will convert it to hours !\n\n"))
    calculated_value = days_to_units(user_input)
    check_execute()