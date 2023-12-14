def calculate(expression):
    i = 0
    current_num = ""
    current_op = ""
    result = 0

    while i < len(expression):
        temp = expression[i]
        if temp.isnumeric() or temp == '.':
            current_num += temp
        elif temp in ['+', '-', '*', '/']:
            if current_op:
                if current_op == '+':
                    result += float(current_num)
                elif current_op == '-':
                    result -= float(current_num)
                elif current_op == '*':
                    result *= float(current_num)
                elif current_op == '/':
                    try:
                        result /= float(current_num)
                    except ZeroDivisionError:
                        print("Error: Division by zero")
                        return
                current_op = temp
                current_num = ""
            else:
                result = float(current_num)
                current_num = ""
                current_op = temp

        i += 1

    if current_op:
        if current_op == '+':
            result += float(current_num)
        elif current_op == '-':
            result -= float(current_num)
        elif current_op == '*':
            result *= float(current_num)
        elif current_op == '/':
            try:
                result /= float(current_num)
            except ZeroDivisionError:
                print("Error: Division by zero")
                return

    print("Result:", result)

user_input = input("Enter expression (e.g., 2+3*4/2): ")
calculate(user_input)
