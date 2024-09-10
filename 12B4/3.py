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

binary_search(12, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
