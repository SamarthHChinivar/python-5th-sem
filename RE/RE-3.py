import re

quote = re.compile(r'\"\w*\s*\w*\"')

text = input('Enter the text to be searched: ')
myquote = quote.search(text)

if(myquote != None):
    print(myquote.group())
else:
    print("Invalid Input")