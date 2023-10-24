count = 0
total = 0

while True:
    inp = input("\nEnter Value : ")
    if inp == "z" : break
    con_inp = float(inp)
    total += con_inp
    count += 1

avg = total / count
print(f"Average is : {avg}\n\n")