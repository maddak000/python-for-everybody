n = 0

print("while loop")
while n < 5:
    print(n)
    n += 1

print("for loop")
for i in [2, 1, 5]:
    print(i)

smallest = None
li = [9, 4, 15, 234, 5, 1]
print(li)
for i in li:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i
print("smallest: ", smallest)
