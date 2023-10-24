import re
email ="from: whothehellareyou9300@gmail.com"
get_mail =  re.findall("^from: (\S.+@.+\s*)",email) ##You basically can separately define what things comes before the part you want to scrap by using "()"
print(get_mail)