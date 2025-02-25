d = {}
letter = ord("A")
for i in range(26):
    d[chr(i+letter)] = i

print(d)