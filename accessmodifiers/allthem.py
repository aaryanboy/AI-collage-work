#access modifiers

class Student:
    def publicaccess(self):
        print("Accessing public method")
    
    
    def _protectedaccess(aelf):
        print("Accessing protected method")
    
    
    def __privateaccess(self):
        print("Accessing private method")
        

student = Student()

student.publicaccess()

student._protectedaccess() 
student.__privateaccess() 

    