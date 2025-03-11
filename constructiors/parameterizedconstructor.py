#define all 3 types of constructors

# //parameterized constructor

class Box:
    def __init__(self,length,breadth,height):
        self.length = length
        self.breadth = breadth
        self.height = height
        
    def area(self):
        return self.length * self.breadth * self.height


objects = Box(5,5,5)

print(objects.area()) 