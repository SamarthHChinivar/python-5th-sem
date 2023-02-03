import re

z = re.compile(r'^[a-z]+_+[a-z]+')

string = input("Enter any string: ")
res = z.search(string)

if(res != None):
    print(res.group())
else:
    print('Not found')