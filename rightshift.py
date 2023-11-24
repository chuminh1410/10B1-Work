def arithmeticRightShift(arr):
    shift = int(input("Enter times of shift: "))
    
    for i in range(len(arr) - 1, shift - 1, -1):
        arr[i] = arr[i - shift]

    for x in range(shift):
        arr[x] = arr[0]

    print(arr)

arr = [1, 0, 1, 1, 0, 0, 1, 1]
arithmeticRightShift(arr)
