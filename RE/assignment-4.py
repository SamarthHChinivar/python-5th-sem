import re

obj = re.compile(r'^\w+')

text = input('Enter text: ')
myobj = obj.search(text)

if(myobj != None):
    print(myobj.group())
else:
    print('not found')