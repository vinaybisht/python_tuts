# Conditional statement tutorial


def check_number(num):
    if num % 2 == 0:  # checking if remainder is 0
        print("The number is even")
    else:  # if remainder is greater than 0
        print("The number is odd")


def max_num_checker(num1, num2, num3):
    if num1 > num2:
        print("Num1 %s is greater " % str(num1))
    elif num2 > num3:
        print("Num2 %s is greater " % str(num2))
    else:
        print("Num 3 %s is greater " % str(num3))


max_num_checker(10, 20, 30)
check_number(10)
check_number(9)
