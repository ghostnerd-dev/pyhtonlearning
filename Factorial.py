def Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n - 1)
    
# Example:
number = int(input("Enter a number to calculate its factorial: "))
result = Factorial(number)
print(f"The factorial of {number} is {result}.")