list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8,]

for i in range(0,len(list2)-1):
    for x in range(0,len(list1)-1):
        if list1[x] == list2[i]:
            list1.pop(x)
print(list1)
