import random

array1 = [random.randint(0, 100) for _ in range(20)]

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
