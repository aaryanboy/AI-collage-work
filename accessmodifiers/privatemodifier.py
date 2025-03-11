class Employee:
  
    def __init__(self,name,salary):
      
        self.__name=name
        self.__salary=salary
        
    def __display(self):
        print ("age",self.__salary)
        
    def displayDETAILS(self):
        print ("name",self.__name)
        self.__display()
        
  
                
GaneshDJ=Employee("GaneshDJ",250)
GaneshDJ.displayDETAILS()