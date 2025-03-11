#define all 3 types of constructors

# //nonparameterized constructor

class Box:
    def __init__(self):
        self.length = 0
        self.breadth = 0
        self.height = 0
        
    def area(self):
        return self.length * self.breadth * self.height


objects = Box()

print(objects.area()) #prints 0