#Slot Machine Game
import random

MAX_LINES = 3 #Maximum no of lines #this is a global constant
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" :2,
    "B" :4,
    "C" :6,
    "D" :8
}
symbol_value = {
    "A" :5,
    "B" :4,
    "C" :3,
    "D" :2
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0],[lines]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:   #you can use else statements with for loops
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols): #this randomly decides which symbols to put in each column
    all_symbols = []# to store symbols
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):#this append a symbol multiple times depending on the value of the key of the dictionary
         # _ is a anonymous variable.if you dont care about iteration value you can use this   
            all_symbols.append(symbol)  #ex : A:2 - 2 As will be added to the all_symbols list
    
    columns = []
    for _ in range (cols):#to generate values inside the column
        column = []
        current_symbols = all_symbols[:]#putting 'listName[:]' make copy of a given list.in this case we assign copy of the all_symbols list to variable named current_symbols
            # [:] is called slice operator
  #we only want a each one of the symbol one time in a column.we dont want to same symbol multiple times
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)# we remove the symbol so it dont add same symbol multiple times
            column.append(value)

        columns.append(column)
    return columns
#if this part is confusing to you please watch the explanation of the tutorial 28:22 --> 29:51

def print_slot_machine (columns): #Giving user the output
    for row in range(len(columns[0])):    #this is called transposing - items in a list as a drop down or something
        for i,column in enumerate(columns):
            if i != len (columns) -1 : #this avoid "|" at the end
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()#new line character (empty line)
#Getting the deposit amount
def deposit():
    while True:
        amount = input("How Much Do You Want To Deposit : $")
        if amount.isdigit():
            if int(amount) > 0:
                break
            else:
                print("Deposit amount must be more than '0'")
        else:
            print("You entered text or symbols.please try again!")
    return amount

#Getting the no of lines
def get_no_of_lines():
    while True:
        lines = input("How Many Lines (1-"+str(MAX_LINES)+") : ")
        if lines.isdigit():
            lines = int(lines)
            if 0 < int(lines) <= MAX_LINES:
                break
            else:
                print("You entered '0' or exceeded the no of lines")
        else:
            print("You entered text or symbols.please try again!")
    return lines

#Getting the bet
def get_bet():
    while True:
        bet_in = input("How Much Do You Want To Bet On Each Line? : $")
        if bet_in.isdigit():
            bet_in = int(bet_in)
            if MIN_BET <= bet_in <= MAX_BET:
                break
            else:
                print(f"Deposit amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("You entered text or symbols.please try again!")
    return bet_in

def spin(balance):

    n_of_lines= get_no_of_lines()
    while True:
        bet = get_bet()
        total_bet = n_of_lines * bet
        if total_bet > int(balance):
            print(f"You do not have enough money to bet that amount.Your current balance is ${balance}")
        else:
            break

    print(f"Balance: {balance} | Number of lines: {n_of_lines} | Single line bet: {bet} | Total Bet: {total_bet}")


    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)#calling the function and spinning the slot machine
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots,n_of_lines,bet,symbol_value)
    print(f"You Won ${winnings}.")
    print(f"You Won On Lines:", *winning_lines)#known as "Splat" or "unpack" operator
    return winnings - total_bet

#main function that triggers all the functions
def main ():
    balance = deposit() #tips - storing a function call inside a variable triggers the function
    balance = int(balance)
    while True:
        print(f"Current Balance is ${balance}")
        answer = input("Press Enter To Play.(Enter 'q' to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")
main()