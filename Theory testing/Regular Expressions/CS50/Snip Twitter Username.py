import re
url = input("Input URL:").strip()
username = re.sub("https://twitter.com/","",url)
print(f"Username: {username}")