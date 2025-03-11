class Student:
    _id=None
    _name=None
    _age=None

    def __init__(self,id,name,age):
        self._id=id
        self._name=name
        self._age=age
        
    def _display(self):
        print ("id no",self._id)
        print ("name",self._name)
        print ("age",self._age)
        
class studentdemo(Student):
    def __init__(self,id,name,age):
        Student.__init__(self,id,name,age)
        
        
    def displayDETAILS(self):
        print("name",self._name)
        self._display()
        
GaneshDJ=studentdemo(101,"GaneshDJ","25")
GaneshDJ.displayDETAILS()