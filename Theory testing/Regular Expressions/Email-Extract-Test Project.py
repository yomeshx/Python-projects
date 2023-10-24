#Extracting email
import re
data = "for ultimate_wind_maker:Mifin100@gmail.com sat 29 2022 offline"

find_mail = re.findall("^for .*:([^ ]+)",data) #'[^ ]' = '\S' can use same thing to say "non whitespace characters" 
print(f"EMail: {find_mail}")#findall extract email in a list 'EMail: ['Mifin100@gmail.com']'
plain_txt_mail = find_mail[0] #To print just the email.not as a list
print(f"Email: {plain_txt_mail}")