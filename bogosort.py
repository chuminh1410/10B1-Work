import random

def bogoSort(a):
    shuffle_count = 0
    while not is_sorted(a):
        shuffle(a, shuffle_count)
        shuffle_count += 1

def is_sorted(a):
    n = len(a)
    for i in range(n-1):
        if a[i] > a[i+1]:
            return False
    return True

def shuffle(a, shuffle_count):
    n = len(a)
    for i in range(n):
        r = random.randint(0, n-1)
        a[i], a[r] = a[r], a[i]
    print(f"Shuffle count: {shuffle_count}, Array: {a}")

a = [10,9,8,7,6,5,4,3,2,1]
bogoSort(a)
print("\nSorted array:")
for i in range(len(a)):
    print("%d" % a[i])
