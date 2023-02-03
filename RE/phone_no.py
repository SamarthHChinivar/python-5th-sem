import re

phone = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

text = input('Enter text: ')
myphone = phone.findall(text)

if(myphone != []):
    print("American Phone Numbers: ",myphone)
else:
    print("Invalid Input")