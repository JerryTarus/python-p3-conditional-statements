#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    
   
    
    if (username.lower() == "sudo" or username.lower() == "admin" or username == "ADMIN") and password == 12345:
        print("Access Granted")
    else:
        print("Access Denied")
        
admin_login("Jerry", 12345)

def hows_the_weather(temperature):
    # your code here
    pass

def fizzbuzz(num):
    # your code here
    pass

def calculator(operation, num1, num2):
    # your code here
    pass
