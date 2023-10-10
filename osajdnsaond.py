# DECLARE num : INT
# DECLARE list_of_digits : ARR
# DECLARE bcd_digits : ARR
# DECLARE bcd_result : STR
# DECLARE bcd_input : STR
# DECLARE decimal_result : INT

while True:
    choice = input("Choose conversion:\n1. Decimal to BCD\n2. BCD to Decimal\nEnter your choice: ")

    if choice == "1":
        num = int(input("Input number to be converted: "))

        while num < 0:
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

    elif choice == "2":
        bcd_input = input("Input BCD representation (space to separate 4-bit groups): ")
        bcd_digits = bcd_input.split()

        decimal_result = 0

        def binary_to_decimal(binary_num):
            decimal_num = 0
            binary_num = binary_num[::-1]  
            for i in range(len(binary_num)):
                decimal_num += int(binary_num[i]) * (2 ** i)
            return decimal_num

        for bcd_digit in bcd_digits:
            decimal_num = binary_to_decimal(bcd_digit)
            decimal_result = decimal_result * 10 + decimal_num

        print("Reversed Decimal Number:", decimal_result)

    else:
        print("Invalid choice. Please choose 1 or 2.")

    continue_choice = input("Do you want to continue? (y/n): ")
    if continue_choice.lower() != 'y':
        break
