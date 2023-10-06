#DECLARE num : INT
#DECLARE list_of_digits : ARR
#DECLARE bcd_digits : ARR
#DECLARE bcd_result : STR


num = int(input("Input number to be converted: "))

while num < 0 and num != int :
    num = int(input("Input number to be converted that is more than 0 : "))

list_of_digits = [x for x in str(num)]

bcd_digits = [] 

def decimal_to_binary(num_convert):
    binary_num = ""
    for i in range(4):
        binary_digit = num_convert % 2
        binary_num = str(binary_digit) + binary_num
        num_convert //= 2
    return binary_num


for i in range(0, len(list_of_digits)):
    if int(list_of_digits[i]) == 0:
        bcd_digits.append("0000")
    else:
        num_convert = int(list_of_digits[i])
        converted = decimal_to_binary(num_convert)
        bcd_digits.append(str(converted))

bcd_result = ' '.join(bcd_digits)
print("BCD Representation:", bcd_result)


       
