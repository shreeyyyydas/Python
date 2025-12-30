# Function to check number type
n=int(input("enter number:"))
def func(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# Calling the function
result = func(n)

# Printing the result
print("The number is:", result)
