def run_length_encoding(input_string):
    encoded_string = ""
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded_string += input_string[i - 1] + str(count)
            count = 1  
    encoded_string += input_string[-1] + str(count)
    return encoded_string

def run_length_decoding(encoded_string):
    decoded_string = ""
    i = 0
    while i < len(encoded_string):
        char = encoded_string[i]
        count = ""
        i += 1
        while i < len(encoded_string) and encoded_string[i].isdigit():
            count += encoded_string[i]
            i += 1
        decoded_string += char * int(count)
    return decoded_string

input_string = input("Enter the string to be encoded: ")
print("Original string:", input_string)
encoded_string = run_length_encoding(input_string)
print("Encoded string:", encoded_string)
decoded_string = run_length_decoding(encoded_string)
print("Decoded string:", decoded_string)
