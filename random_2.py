num = int(input("Enter a number greater than 1: "))
while num < 1:
    num = int(input("Enter a number greater than 1: "))
x = 2 
count = 0 
while num >1:
    multi = False
    while (num % x)  == 0:
        if not multi:
            print(x)
        count +=1
        multi = True
        num = num // x
    x += 1 
print(count)