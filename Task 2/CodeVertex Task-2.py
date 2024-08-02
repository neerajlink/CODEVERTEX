def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def main():
    print("Simple Calculator")

    while True:
        try:
            # Get user input
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            print("\nChoose an operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")

            operation = input("\nEnter your choice (1/2/3/4): ")

            if operation == '1':
                result = add(num1, num2)
                op_symbol = '+'
            elif operation == '2':
                result = subtract(num1, num2)
                op_symbol = '-'
            elif operation == '3':
                result = multiply(num1, num2)
                op_symbol = '*'
            elif operation == '4':
                result = divide(num1, num2)
                op_symbol = '/'
            else:
                print("Invalid operation choice.")
                continue

            print(f"\nResult: {num1} {op_symbol} {num2} = {result}")
        except ValueError:
            print("Invalid input. Please enter numerical values.")

        # Check if the user wants to perform another calculation
        another_calculation = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
