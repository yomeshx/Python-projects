#<---Easy Way--->
with open("D:\\P\\Programing\\Python\\My Learning Projects\\Theory testing\\File IO\\Read\\SampleText.txt","r") as lyrics:
    for line in lyrics:
        # print(line)#there is a gap between lines when just printing them because of '\n'
        print(line.rstrip())#or print(line,end ="")
# #---dumb way---
# with open("D:\\P\\Programing\\Python\\My Learning Projects\\Theory testing\\File IO\\Read\\SampleText.txt","r") as lyrics:
#     lines =lyrics.readlines()
#     # print(lines) #Test       
#     for line in lines :
#     #     print(line)           #2.you can see readlines() makes a list with \n at the end of each item.,because of that there is a gap between lines when just printing them because of '\n'
#         print(line.rstrip())    #3. to fix the issue we can strip empty space at the end of the line like this or we can say 'print(line,end="")'