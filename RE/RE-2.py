import re

str = re.compile(r"Mysore is a beautiful city|Mysore is a cleanest city")
obj = str.search("Mysore is a cleanest city")
print(obj.group())