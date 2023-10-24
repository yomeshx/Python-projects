data = "for ultimate_wind_maker|Mifin100@gmail.com sat 29 2022 offline"
word_list = data.split()
user_and_email = word_list[1]
splitter = user_and_email.split("|")
user = splitter[0]
mail = splitter[1]
print(f"User name : {user}\nEmail : {mail}")
