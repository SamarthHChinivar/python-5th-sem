names = ['apple','google','yahoo','amazon','facebook','instagram','microsoft']

names.append(['netflix', 'walmart', 'kroger'])
print(names)
names.extend(['netflix', 'walmart', 'kroger'])
print(names)

names = ['apple','google','yahoo','amazon','facebook','instagram','microsoft']

names.sort(reverse=True)
print(names)

s = "Hi welcome to python"
print(list(s)) #letter
print(s.split()) #word