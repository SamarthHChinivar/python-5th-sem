import re
text = input("Enter any string: ")
data = re.compile(re.escape('php'), re.I)
new_data = data.sub('php','CSS')

if(new_data != None):
    print(new_data)
else:
    print('not found')