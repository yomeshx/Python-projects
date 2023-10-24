p_id_list = [4040,4041,4042,4043,4044]        #Registered Patients database
que = 0        #The patient queue to meet the doctor

print("Welcome to Navaloka Hospital\n")
status=int(input("Are you a registered patient ?\ntype  1. YES / 2. NO\n")) # to know if the patient is registered and has a record in patient DB or need to register as a new patient

if status == 1 : # he is a registered patient
    p_id = int(input("Enter you patient ID :\n ")) #p_id means patients ID
    res_no = int(input("Enter your reservation number :\n")) #res_no means reservation number

    if p_id in p_id_list : #checking if patients is registered
        que += 1

        if que == 1:
            num_compliment = "st"
        elif que == 2:
            num_compliment = "nd"
        elif que == 3:
            num_compliment = "rd"
        elif que >= 4 and que < 21 :
            num_compliment = "th"
        else:
            print("Sorry the queue is too long and no more patient can be channeled today !\nYou have to channel the doctor next day\n")
            exit() #queue must be less than 21 patients(only 20 patient maximum). if queue is longer than that, must print message above and stop the program from running further.

        print("You are " + str(que) + num_compliment + " in the queue") #informing the patient about his place in the queue
    else:
        print("Invalid Patient ID !!! ,check and retry again !")

elif status == 2: # he is not a registered patient
    reg_req = int(input("\nYou must be registered first !\nWould you like to register now ?  1. Yes / 2. No\n")) #reg_req means registration request
    if reg_req == 1:
        info_confo =2
        while info_confo == 2:
            name = input("Enter your name with inertial :\n")
            nic = input("Enter your NIC :\n")
            address_1_line = input("Enter your Address first line : ")
            address_2_line = input("Enter your Address second line : ")
            birth_year = int(input("Date Of Birth \nYear : ")) #getting birth day of the patient
            birth_month = int(input("Month : "))
            day_of_birth  = int(input("Day of birth : "))

            dob = str(birth_year) + "/" + str(birth_month) + "/" + str(day_of_birth) #generating date of birth
            address = address_1_line +" ,\n" + address_2_line
            
            print("\n\n\n"+"Name : "+ name + "\n" +"NIC : "+ nic +"\n" +"Address : \n" + address + "\n" + "Date of birth : " + dob + "\n\n\n")
            info_confo = int(input("Confirm information above are correct :   1.Yes / 2.No \n"))

        print("Registration process successful !")
        
    else:
        print("Consider restering another time. , Have a healthy day... !")
else:
    print("invalid answer !!! , try again ! ")