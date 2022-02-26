fhand = open("textfile.txt")
counter = dict()
for line in fhand:
    words = line.replace(",", "").split()
    for word in words:
        counter[word] = counter.get(word, 0) + 1

lst = sorted([(v, k) for k, v in counter.items()], reverse=True)
for v, k in lst[:5]:
    print(k, v)
