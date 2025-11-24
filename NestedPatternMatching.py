#Nested Pattern Matching

print("You can use the following commands:")
print("add")
print("subtract")
print("multiply")
print("divide")
user_input = input("Enter a command (i.e add 4 5): ")

parts = user_input.split()

command = (parts[0], (int(parts[1]), int(parts[2])))

match command:
    case ("add", (x, y)):
        print("Result:", x + y)
    case ("subtract", (x, y)):
        print("Result:", x - y)
    case ("multiply", (x, y)):
        print("Result:", x * y)
    case ("divide", (x, y)):
        print("Result:", x / y)
    case _:
        print("Unknown command!")
