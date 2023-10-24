Number_1 = 12.345552
#floating point number with any amount of floating points 
print ("number with two floating points is : {:.2f}".format(Number_1)) # .2f means two floating points

Number_2 = 100000000
print("Number divided with ',' by every thousands s : {:,}".format(Number_2)) #Number divided with ',' by every thousands s 

print("Number in Binary : {:b}".format(Number_2)) #Turn numbers(Decimals) to Binary
print("Number in Octal : {:o}".format(Number_2)) #Turn numbers(Decimals) to octal
print("Number in Hex : {:X}".format(Number_2)) #Turn numbers(Decimals) to hex (with capital letters)
print("Number in Hex : {:x}".format(Number_2)) #Turn numbers(Decimals) to hex (with simple letters)
print("Number in Scientific notation : {:E}".format(Number_2)) #Turn numbers(Decimals) to Scientific notation (with Capital letters)
print("Number in Scientific notation : {:e}".format(Number_2)) #Turn numbers(Decimals) to Scientific notation (with Simple letters)