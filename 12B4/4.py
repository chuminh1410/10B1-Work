import time

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

test_list = [9, 7, 5, 3, 1, 2, 4, 6, 8]

trials = 100000
start_time = time.time()

for _ in range(trials):
    insertion_sort(test_list.copy())

end_time = time.time()

# Calculate the average time taken
average_time = (end_time - start_time) / trials

# Print the average time taken
print("Time Taken for {} trials: {:.6f} seconds".format(trials, average_time))
