import re

z = re.compile(r'\d{1,5}')
string = "Application Development using Python 11 , 12 , 13 , 14 , 15 are important"

res = z.findall(string)
print(res)