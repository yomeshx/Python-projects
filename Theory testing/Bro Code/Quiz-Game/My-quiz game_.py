#--------------------------------------------------------------------
def  new_game():
    guess_list = list()
    correct_guesses = 0
    ques_no = 1

    print("<***---Quiz Game--->***\n")

    for q in questions:         #Iterating questions and getting inputs
        print(q)
        for choices in options[ques_no -1]:     #to iterate choice groups in options
            print(choices)
        user_ans = input("\nEnter Answer A,B,C or D :# ").upper()
        guess_list.append(user_ans)
        correct_guesses += check_answer(questions.get(q),user_ans)
        ques_no += 1
    display_results(correct_guesses,guess_list)
#-------------------------------------------------------------------
def check_answer(answer,user_ans):
    if user_ans == answer:
        print("CORRECT!\n------------------------------------")
        return 1
    else:
        print("WRONG!\n--------------------------------------")
        return 0
#--------------------------------------------------------------------
def play_again():
    re_run_req = input("\nWould you like to play again ? (Yes or No): ")
    re_run_req = re_run_req.upper()

    if re_run_req == "YES":
        return True
    else:
        return False
#--------------------------------------------------------------------
def display_results(correct_guesses,guess_list):

    print("Answers : ",end = "")

    for k,v in questions.items():
        print(v,end = "") #,end = ""
    #----------------------------------------
    print()
    print("Guesses : ",end = "")

    for i in guess_list:
        print(i,end = "")
    print()#empty line
    #----------------------------------------

    score_percentage = int((correct_guesses/len(questions))*100)
    print(f"--------------------------------------\nYour Score : {score_percentage}%")
#---------------------------------------------------------------------
questions ={
    "What is the largest county in the world ?":"A", #russia
    "What is highest mountain in Sri Lanka ?":"C", #Piduruthalagala
    "When Sri Lanka became independent ?":"B" ,#February 4, 1948
    "What is the capital of Canada ?":"D",#Ottawa
    "When did the Soviet Union collapsed?":"C"#December 25, 1991
}

#Answer Options
options=[
["A. Russia","B. China","C. India","D. Germany"],
["A. Kikilimana","B. Kirigalpoththa","C. Pidurangala","D. Sri Pada"],
["A. March 2 1938","B. February 4, 1948","C. June 12 1898","D. May 8 1843"],
["A. Washington DC","B. Canberra","C. Helsinki","D. Ottawa"],
["A. September 5, 1879","B. August 19, 1978","C. December 25, 1991","D. July 8, 1969"]
]
#-----------------------------------------------------------------------

new_game()
while play_again() is True:
    new_game()