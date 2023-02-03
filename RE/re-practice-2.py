import re

def pattern_matching(text):
    pattern = '^a.*?b$' # (.) matches all charecter except \n charecter
    if(re.search(pattern,text)):
        if(len(text) <= 5): 
            print('Match found')
        else:
            print('Match not found')

    else:
        print('Match not found')

text = input('Enter text to be Searched: ')
pattern_matching(text)