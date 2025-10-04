#: Handling ZeroDivisionError
#Instructions:
#Write a program that takes two numbers as input from the user and divides the first number by the second number.
#Handle the ZeroDivisionError exception to inform the user if they attempt to divide by zero.
try:
    
    num1 = float(input("enter the first num:"))
    num2 = float(input("enter the second num"))
    result = num1 / num2
    print("the result is", result)
    
except ZeroDivisionError:
    print("error we cannot divide by 0")
    
    