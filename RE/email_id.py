#importing regular expression module
import re

#regular expression for finding the email-id:
email = re.compile(r'[a-z0-9_.]+@[a-zA-Z]+.[a-zA-Z.]+')

text = input('Enter text: ')
mail = email.findall(text)

if(mail != []):
    print("Mail-id's: ", mail)
else:
    print("Invalid Input")