import re

name = input("Enter Your Name : ")
matches = re.search("^(.+), (.+)$",name)
if matches:
    last,first = matches.groups()
    name = f"{first} {last}"

print(f"Hello, {name}")