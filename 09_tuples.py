d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k, i) in d.items():
    print(k, i)

print(dir(d))
print(dir(tuple(d)))

a = 10
b = 20
tup = (a, b)
print(tup)
a = 99
print(tup)

d = {"a": 10, "b": 76, "c": 3}
print(d.items())

for k, v in sorted(d.items(), reverse=True):
    print(k, v)

l = sorted([(v, k) for k, v in d.items()],reverse=True)
print(l)
