# Making a calculator


def my_calculator():
    input_num1 = float(input("Enter a number : "))
    input_operator = input("Enter a operator : ")
    input_num2 = float(input("Enter second number : "))

    if input_operator == "+":
        print(input_num1 + input_num2)
    elif input_operator == "*":
        print(input_num1 * input_num2)
    elif input_operator == "-":
        print(input_num1 - input_num2)
    elif input_operator == "/":
        print(input_num1 / input_num2)
    else:
        print("Invalid operator")


my_calculator()
