import random
array1 = [None] * 20
for i in range(0,20):
    num = random.randint(0,100)
    array1[i] = num
    
pointer = len(array1) - 1
while pointer > 0:
    swapped = False
    for a in range(pointer):
        if array1[a] > array1[a + 1]:
            array1[a], array1[a + 1] = array1[a + 1], array1[a]
            swapped = True
    if not swapped:
        break
    pointer -= 1
    
pointer = len(array1) - 1
while pointer > 0:
    swapped = False
    for a in range(pointer):
        if array1[a] > array1[a + 1]:
            array1[a], array1[a + 1] = array1[a + 1], array1[a]
            swapped = True
    if swapped == False:
        break
    pointer -= 1

print(array1)