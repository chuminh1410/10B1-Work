name = []
for i in range(0, 5):
    nameinput = input("Name: ")
    name.append(nameinput)

name.sort()

print("Last name:", name[-1])
