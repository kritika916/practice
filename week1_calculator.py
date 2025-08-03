print("Welcome to Python CLI Calculator!")

while True:
    print("\nOptions: +, -, *, / or type 'exit' to quit")
    op = input("Enter operation: ")

    if op.lower() == 'exit':
        print("Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if op == '+':
        print("Result:", num1 + num2)
    elif op == '-':
        print("Result:", num1 - num2)
    elif op == '*':
        print("Result:", num1 * num2)
    elif op == '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero!")
    else:
        print("Invalid operator")
