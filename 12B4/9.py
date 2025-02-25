names = []
last_names = []

for i in range(0, 5):
    nameinput = input("Name: ")
    names.append(nameinput)

for name in names:
    last_name = name.split()[-1]
    last_names.append(last_name)

