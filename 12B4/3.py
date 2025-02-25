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
value = 10
def binary_search(value, array1):
    low = 0
    high = len(array1) - 1
    while low <= high:
        mid = (low + high) // 2
        if array1[mid] == value:
            return mid
        elif array1[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

binary_search(value,array1)