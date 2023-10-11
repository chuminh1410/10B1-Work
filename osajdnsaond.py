# DECLARE num : INT
# DECLARE list_of_digits : ARR
# DECLARE bcd_digits : ARR
# DECLARE bcd_result : STR
# DECLARE bcd_input : STR
# DECLARE decimal_result : INT

while True:
    # User chooses conversion type
    choice = input("Choose conversion:\n1. Decimal to BCD\n2. BCD to Decimal\nEnter your choice: ")

    if choice == "1":  # Decimal to BCD conversion
        # Input number to be converted
        num = int(input("Input number to be converted: "))

        # Ensure the input number is non-negative
        while num < 0:
            num = int(input("Input number to be converted that is more than 0 : "))

        # Convert the number to a list of digits
        list_of_digits = [x for x in str(num)]

        # List to store BCD digits
        bcd_digits = []

        # Function to convert decimal digit to 4-bit binary
        def decimal_to_binary(num_convert):
            binary_num = ""
            for i in range(4):
                binary_digit = num_convert % 2
                binary_num = str(binary_digit) + binary_num
                num_convert //= 2
            return binary_num

        # Convert each digit to 4-bit BCD representation
        for i in range(0, len(list_of_digits)):
            if int(list_of_digits[i]) == 0:
                bcd_digits.append("0000")
            else:
                num_convert = int(list_of_digits[i])
                converted = decimal_to_binary(num_convert)
                bcd_digits.append(str(converted))

        # Join BCD digits and display the result
        bcd_result = ' '.join(bcd_digits)
        print("BCD Representation:", bcd_result)

    elif choice == "2":  # BCD to Decimal conversion
        # Input BCD representation as space-separated 4-bit groups
        bcd_input = input("Input BCD representation (space to separate 4-bit groups): ")
        bcd_digits = bcd_input.split()

        decimal_result = 0

        # Function to convert 4-bit binary to decimal
        def binary_to_decimal(binary_num):
            decimal_num = 0
            binary_num = binary_num[::-1]  # Reverse the binary number
            for i in range(len(binary_num)):
                decimal_num += int(binary_num[i]) * (2 ** i)
            return decimal_num

        # Convert each 4-bit BCD digit to decimal and concatenate the result
        for bcd_digit in bcd_digits:
            decimal_num = binary_to_decimal(bcd_digit)
            decimal_result = decimal_result * 10 + decimal_num

        # Display the reversed decimal number
        print("Reversed Decimal Number:", decimal_result)

    else:  # Invalid choice
        print("Invalid choice. Please choose 1 or 2.")

    # Ask the user if they want to continue
    continue_choice = input("Do you want to continue? (y/n): ")
    if continue_choice.lower() != 'y':
        break
