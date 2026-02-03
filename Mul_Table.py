def Mul_Table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


# Example:
num = int(input("Enter a number to display its multiplication table: "))
Mul_Table(num)
