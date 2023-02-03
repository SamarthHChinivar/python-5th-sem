import re

z = re.compile(r'\W+')
string = '''***// Application Development Using Python// - 18CS55'''
res = z.findall(string)

print(res)