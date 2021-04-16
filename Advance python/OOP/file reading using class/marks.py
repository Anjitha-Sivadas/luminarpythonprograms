class Student:
    def __init__(self,name,rollno,course,marks):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.marks=marks
    def printval(self):
        print("name:",self.name)
        print("rollno:",self.rollno)
        print("course:",self.course)
        print("marks:",self.marks)
f=open("marks","r")
for lines in f:
    data=lines.split(",")
    name=data[0]
    rollno=data[1]
    course=data[2]
    marks=int(data[3])
    stud=Student(name,rollno,course,marks)
    if(marks>190):
        stud.printval()

