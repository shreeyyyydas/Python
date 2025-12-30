# Define a simple custom exception
class InvalidAge(Exception):
    pass

# Function to check age
def check_age(age):
    if age < 18 or age > 100:
        raise InvalidAge("This  Age is not allowed")
    else:
        print("Age is valid.")

# Try-Except block
try:
    age = int(input("Enter the age: "))
    check_age(age)

except InvalidAge as e:
    print("Error:", e)

except ValueError:
    print("Please enter a valid number.")
