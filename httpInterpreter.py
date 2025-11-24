#HTTP Status Code Interpreter
http = int(input("Enter a HTTP status code: "))
match http:
    case 200:
        print("HTTP 200 means OK.")
    case 404:
        print("HTTP 404 means Not Found.")
    case 500:
        print("HTTP 500 means Internal Server Error.")
    case _:
        print("Invalid HTTP status code.")
