import re

def validate(email):
   
    pattern = r'^\w+@\w+\.\w+$'
    
    if re.match(pattern, email):
        return True
    else:
        return False

# --- Test ---
email = input("Enter email: ")

if validate(email):
    print("Valid email!")
else:
    print("Invalid email.")
