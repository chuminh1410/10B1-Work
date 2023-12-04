original = ['Red', 'Green', 'Blue', 'White', 'Black']
original_reverse = []
for i in range(0,len(original)):
    temp = original[i]
    original_reverse.append(temp[::-1])
print(original_reverse)
