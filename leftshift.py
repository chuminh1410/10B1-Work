def arithmeticLeftShift(arr):
    shift = int(input("Enter times of shift: "))
    
    for i in range(shift, len(arr)):
        arr[i - shift] = arr[i]

    for x in range(len(arr) - shift, len(arr)):
        arr[x] = 0

    print(arr)

arr = [1, 0, 1, 1, 0, 0, 1, 1]
arithmeticLeftShift(arr)
