nlist = [62,56,45,78,12,18,17,548,8545,745,45,549,7854,155,487,665]

def val_stat ():
    print(f"\nStat is {stat} Current value is {value}")
stat = False

print("Program that shows 'True' or 'False' depending on it's value more or less than 100 ")
for value in nlist :
    if value > 100 :
        stat = True
        val_stat()

    else:
        stat = False
        val_stat()
