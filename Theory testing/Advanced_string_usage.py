email_addr ="gotagottago.ceo.icanthearyou_anymore.@get_this_part_out_ .mail.com"

starter_point = email_addr.find("@")
closing_point = email_addr.find(" ")

part_we_wanna_take = email_addr[starter_point +1 : closing_point]
print(part_we_wanna_take)

#----------------------------we can use split() method to break string into peaces ----------------------------------------------
name = input("Enter your name \n")
first_name,last_name = name.split(" ") #example 1
print(f"Hello {first_name}")

email = "helloworld100@gmail.com"
address,service = email.split("@") #example 2
print(f"Email service is {service}")