num = int(input("Number of names: "))
name = []
for i in range (0,num):
    a = input("Name: ")
    name.append(a)
    
first_last = name[::len(name)-1]
middle = name[1:len(name)-1]
print("First name: ",first_last[0])
print("Middle name: ",middle)
print("Last name: ",first_last[1])
