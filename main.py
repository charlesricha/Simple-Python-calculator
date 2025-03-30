# Requesting Input from user

x = float(input("Enter the first Number: "))  # Convert input to a number
y = float(input("Enter the second Number: ")) # Convert input to a number
operand = input("Enter the operator (+, -, /, *): ")  # Read the operator

# Perform the calculation based on the operator
if operand == "+":
    print(x + y)
elif operand == "-":
    print(x - y)
elif operand == "*":
    print(x * y)
elif operand == "/":
    if y != 0:
        print(x / y)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operator!")

