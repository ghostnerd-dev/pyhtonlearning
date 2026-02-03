import math

def is_prime(n):
    # 1. Handle base cases
    if n <= 1: return False
    if n <= 3: return True  # 2 and 3 are prime
    
    # 2. Eliminate multiples of 2 and 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # 3.Check divisors up to √n
    # We only check numbers in the form 6k ± 1: This is the golden rule for primes
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True

# Example:
num = 997  # Largest 3-digit prime
if is_prime(num):
    print(f"{num} is a prime number!")
else:
    print(f"{num} is not prime.")
