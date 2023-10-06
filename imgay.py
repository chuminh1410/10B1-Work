def decimal_to_binary(num_convert):
    binary_num = ""
    for i in range(4):
        binary_digit = num_convert % 2
        binary_num = str(binary_digit) + binary_num
        num_convert //= 2
    return binary_num
def decimal_to_binary(num_convert):
    binary_num = ""
    for i in range(4):
        binary_digit = num_convert % 2
        binary_num = str(binary_digit) + binary_num
        num_convert //= 2
    return binary_num
