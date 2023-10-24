#You should import 'functools' to use reduce
#It's like we create a finish product from raw materials
import functools
#------------------------------------------------------------------------
#Ex 01
letters = ["H","E","L","L","O"] #Row materials in this case

word = functools.reduce(lambda x,y: x+y , letters)
#Code line above will do this,
    # H+E
    # HE+L
    # HEL+L
    # HELL+O
    # HELLO         #until list items reduced to nothing 
print(word)

#------------------------------------------------------------------------
#Ex 02
numbers = [20,20,20,20,20]

dsum = functools.reduce(lambda x,y : x+y, numbers)
#Code line above will do this,
    #20+20
    #40+20
    #60+20
    #80+20 ----> 100
print(dsum)

#------------------------------------------------------------------------
#Ex 03
nlist = [2,5,10,10]

factorial = functools.reduce(lambda c,y : c * y , nlist)
#Code line above will do this,
    #2*5
    #10*10
    #100*10 --> 1000
print(factorial)

#------------------------------------------------------------------------