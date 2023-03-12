d = {'bangalore':30, 'chennai':23}
print(d)

d.update({"mysore":20,"LA":21, "chennai":27})
print(d)

print(d.setdefault("Mumbai"))
print(d.setdefault("mysore"))
print(d)

print(d.setdefault("kolkata",29))
print(d.setdefault("Mumbai",29))
print(d)