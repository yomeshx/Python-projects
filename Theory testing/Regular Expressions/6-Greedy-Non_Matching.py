import re

#*****EX 01

Line = "Bend off: Anti :grown"
greedy = re.findall("^B[B,A,C,e]+.*:",Line)#'^B'=anything that starts with 
                                    # '[B,A,C,e]+' = one or more character or characters comes after B that given in the list
                                    #  '.*' = any character zero or many times
                                    #':' = if theres ':' it's the end point of the parameter
print(greedy)#result will be #  ['Bend off: Anti :']
        #Result will show first ':' is skipped and the last ':' is the end point.

#The reason is to call greedy ,because this consider the lengthiest end point is the match even there's a ':' before the end ':' in this string
#In order to make Non-Greedy you just add a '?' symbol as the last symbol before end point.(Ex:02)

#*****EX 02
non_greedy = re.findall("^B[B,A,C,e]+.*?:",Line)
print(non_greedy) #result #['Bend off:']