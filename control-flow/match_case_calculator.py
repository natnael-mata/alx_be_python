num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Make sure to use 'match opr:' exactly
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            exit()
        result = num1 / num2
    case _:
        print("Invalid operator.")
        exit()

print(f"The result is {result}")