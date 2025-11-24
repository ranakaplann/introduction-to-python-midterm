#Simple Menu System
while True:
    print("\n=== Simple Menu ===")
    print("1. Say Hello")
    print("2. Add Two Numbers")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == '1':
        print("Hello! Nice to see you :)")

    elif choice == '2':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a + b)

    elif choice == '3':
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")
