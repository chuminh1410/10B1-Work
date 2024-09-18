text = input("Enter some text: ")
words = text.split()
count = 0
indicies = []
for word in words:
    if 'owl' in word.lower():
        count += 1
        indicies.append(i)

print("There were", count, "words that contained 'owl'.")
print("They occured at indicies: ",indicies)
