import re

z = re.compile(r'\d+\s\w+')
res = z.findall('99 apple, 45 orange_, 4 mango')

print(res)