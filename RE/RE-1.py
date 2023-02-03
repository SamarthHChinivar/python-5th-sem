import re

usn = re.compile(r'(\w\w\w)(\w\w)(\w\w)(\w\w\w)')

myusn = input('Enter USN:')
res = usn.search(myusn)

print('College code: ', res.group(1))
print('Year of Admission: ', res.group(2))
print('Branch: ', res.group(3))
print('Roll number in the branch: ', res.group(4))


print('USN: ',res.group())
print(res.groups())