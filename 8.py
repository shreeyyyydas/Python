# Global variable
a = "Hello,Thanks for choosing Global Air India."
b= "We welcome you!"

def func():
    # Local variable
    a = "Hello, Welcome to the local Board."
    b= "How can i assist you?"
    print("Local scope:", a,b)

# Calling the function
func()

# Printing global variable
print("Global scope:", a,b)
