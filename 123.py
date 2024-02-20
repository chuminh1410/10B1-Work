input_str = input("enter a string separated by (;) : ")
result_str = ' '.join(word.capitalize() for word in reversed(input_str.split(';')))
print(result_str)

