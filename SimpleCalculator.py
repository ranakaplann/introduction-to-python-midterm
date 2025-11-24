#Simple Calculator
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
get = int(input("Welcome to calculator, Please choose the operation you want to use:"))
match get:
    case 1:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result:", a + b)
    case 2:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result:", a - b)
    case 3:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result:", a * b)
    case 4:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result:", a/b)
