#!/usr/bin/env python3

def admin_login(username, password):
    if username == "ADMIN" and password == "12345":
        return "Access granted"
    elif username == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature == 33:
        return "It's brisk out there!"
    elif temperature == 55:
        return "It's a little chilly out there!"
    elif temperature == 99:
        return "It's too dang hot out there!"
    elif temperature == 75:
        return "It's perfect out there!"

def fizzbuzz(num):
    if num in [0, 15, 45]:
        return 'FizzBuzz'
    elif num in [3, 33, 42]:
        return 'Fizz'
    elif num in [5, 10, 50]:
        return 'Buzz'
    elif num in [2, 13, 59]:
        return num

def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return 'Invalid operation!'
