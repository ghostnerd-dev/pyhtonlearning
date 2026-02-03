def Calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero."
    else:
        return "Error: Invalid operation."
    
# Example:
print ("\nEnter numbers below to perform calculation:")
num1 = int (input("Enter first number: "))
num2 = int (input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")
result = Calculator(num1, num2, op)
print(f"The result is: {result}")