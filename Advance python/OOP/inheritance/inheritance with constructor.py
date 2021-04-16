class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printval(self):
        print("name",self.name)
        print("age",self.age)
class Student(Person):
    def __init__(self,rollno,mark,name,age):   #add superclass attributes to derived class while using construvtor
        super().__init__(name,age)    #to call superclass constructor(atributes)
        self.rollno=rollno
        self.mark=mark
    def print(self):
        print(self.rollno)
        print(self.mark)
cr=Student(2,34,"anju",22)
cr.printval()
cr.print()

