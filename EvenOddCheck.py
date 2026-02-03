def EvenOddCheck(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# Example:
number = int(input("Enter a number to check if it is Even or Odd: "))
result = EvenOddCheck(number)
print(f"The number {number} is {result}.")