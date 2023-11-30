#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    
    if (username.lower() == "sudo" or username.lower() == "admin" or username == "ADMIN") and password == 12345:
        print("Access Granted")
    else:
        print("Access Denied")
        
        

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        print("It's brisk out there!")
    if temperature == 40 and temperature < 65:
        print("It's a little chilly out there!")
    if temperature > 85:
        print("It's too dang hot out there!")
    else:
        print("It's perfect out there!")
hows_the_weather(100)

def fizzbuzz(number):
    # your code here
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number
fizzbuzz(56789)

for i in range(1, 16):
    print(fizzbuzz(i))



def calculator(operation, num1, num2):
    # your code here
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Division by zero!")
            return None
    else:
        print("Invalid operation!")
        return None


result_addition = calculator('+', 5, 3)
print(f"Addition result: {result_addition}")

result_invalid = calculator('%', 7, 2)
print(f"Invalid operation result: {result_invalid}")

result_division = calculator('/', 10, 2)
print(f"Division result: {result_division}")
