import re

def pattern_matching(text):
    pattern = '^[A-Z][a-z]+'

    if(re.search(pattern,text)):
        print("Match found")
    else:
        print("Match not found")
    
text = input('Enter the text to be searched: ')
pattern_matching(text)