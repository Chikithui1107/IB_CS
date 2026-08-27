def calculator():
    operation = input("Enter operation (+, -, *, /): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero")
            return calculator()
    else:
        print("Invalid operation")
        return calculator()

    print(f"The result of {num1} {operation} {num2} is: {result}")

    again = input("Do you want to perform another calculation? (y/n): ")
    if again.lower() == 'y':
        return calculator()
    else:
        print("Thank you for using the calculator!")
        return

calculator()
