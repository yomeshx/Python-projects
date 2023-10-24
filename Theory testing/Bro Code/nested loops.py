rows = int(input("Number of rows : "))
columns = int(input("Number of columns : "))
symbol = input("Enter the symbol : ")

for i in range(rows):
    for x in range(columns):
        print(symbol,end ="")
    print()