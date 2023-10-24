pin_list = [4560,4561,4562,4563,4564,4565,4566,4567,4568,4569,4570]
list_options = ["1. Withdrawal money","2. Make a payment","3. Check your balance","4. Return Your card"]
chances = 3
balance = 5000 # Static value because of this is a simple test programme
print("\n***** Welcome to AWS Bank ATM *****\n")

def exit_reqst (): #asking to terminate the program
    exit_req = input("\nEnter 'E' or 'e' to exit. !\n")
    if exit_req =='E' or exit_req =='e':
        print("\nProgram ternimated !\nHave a nice day !!!\n\n")
        exit()
while chances != 0 :
    pin_req = input("\nEnter you PIN :") #pin_req = users PIN
    if int(pin_req) in pin_list: #Validation of the pin
        
        for opt  in  list_options: # printing all the options to the user 
            print(f"\n{opt}")

        user_option=(input(f"\nPlease enter the number of the service you wish to get.\n\n"))
        while user_option.isdigit() and int(user_option) < 5 and int(user_option) > 0:
            if int(user_option) == 1 :
                exit_req = ""
                while exit_req != ("E","e"):
                    amount = input("\nEnter the amount you wish to withdrawal\n")
                    conf_req = input(f"Confirm to withdraw Rs: {amount}       (Y).Yes / (N).No  : ") #amount confirmation request
                    new_balance = balance - int(amount)
                    print(f"\nWithdrawal amount Rs: {amount} | Current balance is Rs: {new_balance}\n")
                    exit_reqst()

            elif int(user_option) == 2 :
                ac_no_recever = input("\nEnter the account number of the recever: \n")
                pay_amount = input("\nEnter the paying amount: \n")
                conf_pay = input(f"Are you sure you want to pay Rs: {pay_amount} to {ac_no_recever} ?  (Y). Yes / (N). No  : ") #Asking for the conformation of the payment

                if conf_pay in("Y","y","yes","YES"): 

                    print(f"\nPayment of Rs : {pay_amount} to {ac_no_recever} was successful !!!\n") #payment confirmation message
                    exit_reqst()

            elif int(user_option) == 3 :
                print(f"\nYour current account balance is  Rs: {balance} \n")
                exit_reqst()

            elif int(user_option) == 4 :
                print("\nCard ejected !")
                exit_reqst()
        else:
            print(f"\n{user_option} is invalid !!!\n")
    else:
        print("PIN is not valid !!!")
        chances -= 1
else:
    print("\nNo more chances available\n")
