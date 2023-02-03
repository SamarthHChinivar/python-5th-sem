import re

def pattern_matching(text):
    pattern = 'ab*'
    if(re.search(pattern,text)):
        print("Match Found")
    else:
        print('Match not found')

text = input("Enter text to be searched: ")
pattern_matching(text)