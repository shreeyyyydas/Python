class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c
    def mult(self,a=1,b=1,c=1):
        return a*b*c

# Create object
calc = Calculator()

# Call method with different number of arguments
print("add():", calc.add())           # Output: 0
 
print("add(5, 12, 15):", calc.add(5, 12, 15)) # Output: 30

print("mult():", calc.mult())           # Output: 0

print("mult(5, 20, 15):", calc.mult(5, 20, 15))
