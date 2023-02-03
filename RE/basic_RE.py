import re

dob = re.compile(r'(\d\d)-(\d\d)-(\d\d\d\d)')

string = input('Enter any string with dob in dd-dd-dddd format: ')
mydob = dob.search(string)

if(mydob != None):
    print("DOB is ", mydob.group())
    print(mydob.groups())
    print(mydob.group(1))
    print(mydob.group(2))
    print(mydob.group(3))
else:
    print('Invalid Input')