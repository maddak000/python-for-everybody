import re

fhand = open("textfile.txt")
for line in fhand:
    line = line.rstrip()
    if re.search("^this", line):
        print(line)
fhand.close()

print()

fhand = open("textfile.txt")
for line in fhand:
    line = line.rstrip()
    if re.search("^this.*,", line):
        print(line)
fhand.close()

x = "my 2 favorite numbers are 19 and 42"
y = re.findall("[0-9]+", x)
print(y)
y = re.findall(f"[AEIOUYaeiouy]+", x)
print(y)