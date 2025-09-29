# match case calculator

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
opr = input("Choose the operation (+, -, *, /): ")
result =0

match opr:
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
        print("invalid Oprator")
        exit()
print(f"The result is {result}")
    