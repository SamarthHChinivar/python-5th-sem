import re

z = re.compile(r'[aeiou]',re.I) #vowels
res = z.findall("Mysore is a beautiful city")

print(res)