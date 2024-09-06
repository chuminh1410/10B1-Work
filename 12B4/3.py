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
    
print(array1)
value = 2
def binary_searach(value,array1):
    length = len(array1)
    mid = length//2
    while array1[mid] != value:
        if array1[mid] > value:
            length = length - mid
            mid = (length // 2) + mid
        elif array1[mid] > value:
            length = length - mid
            mid = mid - (length //2)
        else:
            return mid
    return -1

binary_searach(value,array1)