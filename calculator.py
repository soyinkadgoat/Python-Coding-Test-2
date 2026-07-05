def Add(num1, num2):
    return num1 + num2

def Subtract(num1, num2):
    return num1 - num2

def Multiply(num1, num2):
    return num1 * num2

def Divide(num1, num2):
    return num1 / num2

try:

    operation = int(input("1 = Add\n2 = Subtract\n3 = Multiply\n4 = Divide\n\nChoose your operation: "))

    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    if operation == 1:
        print(str(number1), "+", str(number2), "=", Add(number1, number2))
    elif operation == 2:
        print(str(number1), "-", str(number2), "=", Subtract(number1, number2))
    elif operation == 3:
        print(str(number1), "*", str(number2), "=", Multiply(number1, number2))
    elif operation == 4:
        print(str(number1), "/", str(number2), "=", Divide(number1, number2))

except ValueError:
    print("That is not a number!")

except ZeroDivisionError:
    print("You cannot divide by zero!")