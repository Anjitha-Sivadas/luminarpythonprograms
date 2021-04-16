class Student:
    def __init__(self,rollno,name,course,total):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name
s1=Student(10,"surya","BBA",250)
s2=Student(11,"anju","BCA",200)
s3=Student(12,"anu","BCA",240)

studentlist=[]
studentlist.append(s1)
studentlist.append(s2)
studentlist.append(s3)

studenttotal=list(map(lambda stud:stud.total,studentlist))
print(studenttotal)
print(max(studenttotal))
