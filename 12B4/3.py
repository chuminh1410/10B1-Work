import time
def binary_search(value, array):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1

test_list = [9, 7, 5, 3, 1, 2, 4, 6, 8]

trials = 1000  
start_time = time.time()

for _ in range(trials):
    binary_search(test_list.copy())

end_time = time.time()

average_time = (end_time - start_time) / trials

print("Time Taken for {} trials: {:.6f} seconds".format(trials, average_time))
