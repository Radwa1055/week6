class student:
    def __init__(self, name, age):
       self.name = name 
       self.age = age 
       
    def display_info(self):
        print(f"student name: {self.name}, age: {self.age}")
         
student1 = student("radwa", 28) 
 
student2 = student("omar", 25)  
     
student1.display_info()
student2.display_info()
