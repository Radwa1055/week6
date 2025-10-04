# File Handling with FileNotFoundError
#Instructions:
#Write a program that attempts to open and read data from a file specified by the user.
#Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.
  
  
  
try:
    filename = input ("enter the file name: ") 
    with open(filename, "r") as file:
         print(file.read())    
except fileNotFoundError:
    print("error this file not found")
    
  