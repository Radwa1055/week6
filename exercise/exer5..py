#Custom Exception
#Instructions:
#Create a custom exception class called ValueTooHighError that inherits from the Exception class.
#Write a program that takes a number as input and raises a ValueTooHighError exception if the number is greater than 100.

class ValueTooHighError(Exception):
    pass
try:
        num1= float(input("enter the number"))
        if num1 > 100:
            raise ValueTooHighError("error: greater than 100")
        else:
            print("the num is ", num1)
except ValueTooHighError as e:
      print(e)

    
         
         
