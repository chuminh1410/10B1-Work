
colors = []
for i in range(10):
    color = input("Enter a color: ")
    colors.append(color)

with open("colors.txt", "w") as f:
    for color in colors:
        line = color + "\n"  
        f.write(line)

with open("colors.txt", "r") as f:
    for line in f:
        color = line.strip() 
        print(color)
