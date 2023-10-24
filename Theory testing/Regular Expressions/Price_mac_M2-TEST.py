import re
line = "Apple released their newest Macbook air M2 starting from $1600 ,but i think M1 macbook pro still outperform M2 Macbooks"
price_inList = re.findall("^Apple[\S,\s]+from (\$[0-9]+)",line)
price = price_inList[0]
print(f"\nApple M2 Macbook Air\nPrice: {price}")