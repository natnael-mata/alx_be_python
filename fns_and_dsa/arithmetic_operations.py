# arithmetic opertion 

def perform_operation(num1: float, num2: float, operation: str):
    
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 == 0:
              print("invalid devisor")   
              return None
            return num1 / num2
        else: print("Invalid Operator")
        
print(perform_operation(10.0,0.0,"divide"))