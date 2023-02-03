import re

greedyR = re.compile(r'(Ha){3,5}')
greedyobj = greedyR.search('HaHaHaHaHa')
print('Greedy(longest):     ',greedyobj.group())

nongreedyR = re.compile(r'(Ha){3,5}?')
nongreedyobj = nongreedyR.search('HaHaHaHaHa')
print('NonGreedy(shortest): ',nongreedyobj.group())