# Recursive function to find factorial
def fact(n):
    if n == 0 or n == 1:
        return 1  # Base case
    else:
        return n * fact(n - 1)  # Recursive case

# Input from user
num = int(input("Enter a number: "))

# Checking for valid input
if num < 0:
    print("No Factorial for negative numbers.")
else:
    result = fact(num)
    print(f"Factorial of {num} is {result}")
