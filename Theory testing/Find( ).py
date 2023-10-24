#Find() is case sensitive
# The find() method finds the first occurrence of the specified value(Position of the first character),and if theres no result it returns -1 kinda like 'False'
    #so you can do things like 'if line.find("Email:") >= 0: ..bla..bla...bla '
#***** you can give second additional parameter inside the find function

#EX : 01
fas = "Tear Gas is harmful for eyes"

if fas.find("Gas")>=0:
    print("\nWord Found")
else:
    print("\nWord Not Found")

#EX : 02
email_addr ="gotagottago.ceo.icanthearyou_anymore.@get_this_part_out_ .mail.com"

starter_point = email_addr.find("@")
closing_point = email_addr.find(" ")

part_we_wanna_take = email_addr[starter_point +1 : closing_point]
print(part_we_wanna_take)

#EX 3
fas = "123456789x"
strt = fas.find("1")
end = fas.find("x")-1
take_away = fas[strt:end]
print(take_away)

#EX 4
print("\n------------>| EX 04 |<------------\n")
data = "for ultimate_wind_maker|Mifin100@gmail.com sat 29 2022 offline"
start_l = data.find("ult")
print(start_l) #test  #should give starting position of 'ult'
end_l = data.find("maker",start_l)+5                                #***** you can give second additional parameter 'start_l' inside the find function
print(end_l)#test  #should give end position of 'ultimate_wind_maker'
user = data[start_l:end_l]
print(f"User ---> | \n{user}")