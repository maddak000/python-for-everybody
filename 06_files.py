fhand = open("textfile.txt")
print(fhand)
# inp = fhand.read()
for i in fhand:
    i = i.rstrip()
    print(i)
fhand.close()

fhand = open("textfile.txt")
for i in fhand:
    if i.startswith("this"):
        print(i)
fhand.close()

fhand = open("textfile.txt")
for i in fhand:
    if i.startswith("this"):
        continue
    print(i)
fhand.close()
