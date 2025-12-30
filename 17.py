try:
    # Ask for two inputs
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    
    # Perform division
    result = a / b
    print("Result:", result)

    # Try accessing a list element
    my_list = [1, 2, 3]
    print("Element:",my_list[2])

except ValueError:
    print("ValueError: Please enter numbers only.")

except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")

except IndexError:
    print("IndexError: Index is out of range.")

except Exception as e:
    print(f"Other error occurred: {e}")
