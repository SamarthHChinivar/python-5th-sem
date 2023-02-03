import re

string = '''Its not who I am underneath, but what I do that defines Bat me - Batman , Batman Begins
Hes the hero Gotham deserves, but not the one it needs right now. So well hunt him Because he can take it Because hes not our hero. 
Hes a silent guardian, a watchful protector A dark knight - Jim Gordon , The Dark Knight'''

modstring = re.sub('Bat','BATS',string)

print(modstring)