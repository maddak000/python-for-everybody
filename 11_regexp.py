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

x = "my 2 favorite numbers are 19 and 42 and email john@myemail.com thanks"
y = re.findall("[0-9]+", x)
print(y)
y = re.findall("[0-9]+?", x)
print(y)
y = re.findall(f"[AEIOUYaeiouy]+", x)
print(y)
y = re.findall(f"^my ([0-9]+)", x)
print(y)
y = re.findall(f"\\s+([0-9]+)\\s+", x)
print(y)
y = re.findall(f"^my.*@([^ ]+)", x) # [^ ] means non-blank
print(y)
