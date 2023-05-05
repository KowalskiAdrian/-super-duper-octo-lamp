names =  [("name", "Adrian"), ("occupation", "Coder")]
d = {}
for key, value in names:
    d[key] = value
print(d)
# print(type(d))


d = {key: value for key, value in names}
print(d)

d = dict(names)
print(d)