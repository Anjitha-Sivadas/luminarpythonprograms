# 1   create a child class bus that will inherit
#     all of the variables and methods of vehicle class
"""
class Vehicle:
    bus_name=""
    def no_of_veh(self):
        print("one")
class Color:
    veh_color=""
    def clr(self):
        print("color of vehicle:",self.veh_color)

class Bus(Vehicle,Color):
    def cbus(self):
        print("Bus name:",self.bus_name)
        print("Vehicle color:",self.veh_color)

obj=Bus()
obj.bus_name="ABC"
obj.veh_color="Blue"
obj.cbus()
"""

# 2 Create an example for three types of inheritance in one program
#   by using Person as main class?
"""
class Person():
#single
    person_name="ANIL"
    def m1(self,age):
        self.age = age
        print("my name is",Person.person_name)
        print(self.age)
class Sub(Person):
    def m2(self,page):
        self.page=page
        print("name is", Person.person_name)
        print(self.page)
        print(self.age)
op=Sub()
op.m1(25)
op.m2(30)
#multiple
class Child(Sub,Person):
    def m3(self,cage):
        self.cage=cage
        print("parent name is",Person.person_name)
        print(self.cage)
        print(self.page)
        print(self.age)
obj=Child()
obj.m1(35)
obj.m2(68)
obj.m3(5)
#multilevel
class Subchild(Sub):
    def m4(self):
        print("inside subchild class")
m=Subchild()
m.m4()
m.m1(78)
m.m2(85)
"""
# 3 Create a Book class with instance Library_name, book_name, author, pages?
"""
class Book():
    def __init__(self,library_name,book_name,author,pages):
        self.library_name=library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def printval(self):
        print(self.library_name,self.book_name,self.author,self.pages)
opj=Book("ABC","SECRET","Rhonda",100)
opj.printval()
"""
# 4 Create an Animal class using constructor and build a child class for Dog?
"""
class Animal():
    animal_name="dog"
    def __init__(self,num):
        self.num= num
    def name(self):
        print(" name is",Animal.animal_name)
        print(self.num)
class Dog(Animal):
    def nameis(self):
        print("animal name is", Animal.animal_name)
        print(self.num)
op=Animal(2)
op.name()
boj=Dog(3)
boj.nameis()
"""
""""
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printval(self):
        print("name",self.name)
        print("age",self.age)
class Dog(Animal):
    def __init__(self,color,name,age):
        super().__init__(name,age)
        self.color=color
    def print(self):
        print(self.color)
cr=Dog("brown","chottu",2)
cr.printval()
cr.print()
"""
# 5 What is method overriding give an example using Books class?
"""
class Books:
    def color(self):
        print("Blue color book ")
class Book(Books):
    def color(self):
        print("Green color book")
obj=Book()
obj.color()
"""
# 6 Create objects of the following file and print the details of student
#   with maximum mark? anu,1,bca,200 rahul,2,bba,177 vinod,3,bba,187 ajay,4,
#   bca,198 maya,5, bba,195
"""
f=open("student","r")
class student():

    class student():
        def __init__(self, rno, name, department,mark):
            self.rno = rno
            self.name = name
            self.department = department
            self.mark = mark

        def __str__(self):
            return self.name + " " + str(self.mark)

    students = []
    for lines in f:
        rno, name, department,mark = lines.rstrip("\n").split(",")
        students.append(student(rno, name, department, mark))
    for data in students:
        print(data)
    marks= []
    for stud in students:
        marks.append(stud.mark)
    print(max(marks))
"""
# 7 Create a valid phone numbers file from the following file?
#    +915678905432 +914567890321 765432167 123450987765 +919976532456
"""
from re import *
f=open("pnum","r")
lst=[]
rule='[+]91[0-9]{10}'
for lines in f:
    variablename=lines.rstrip("\n")
    matcher = fullmatch(rule, variablename)
    if matcher != None:
        print('valid',variablename)
        lst.append(variablename)
    else:
        print("invalid variable name",variablename)
print(lst)
"""
# 8 When is the finally block executed.Explain with example?
"""
no1=int(input("enter num1"))
no2=int(input("enter num2"))
try:
    res=no1/no2
    print(res)
except Exception as e:
    print("exeception occured",e.args)
finally:
    print("database is created")
"""
# 9 Write a Python program to find the sequences of
#    one upper case letter followed by lower case letters?
"""
from re import *
rule='[A-Z]+[a-z]+$'
variable_name=input("enter variable name")
matcher=fullmatch(rule,variable_name)
if matcher!=None:
    print("valid variable name")
else:
    print("invalid variable name")
"""
# 10    Write a Python program that matches a string that has an 'a'
#       followed by anything, ending in 'b'?

from re import *
pattern="a.*?b$"

string="addddhhhhrrrsssb"
matcher=finditer(pattern,string)
cnt=0
for match in matcher:
    print(match.start())
    print(match.group())
    cnt=1
if cnt==1:
    print(' found a match')
else:
    print('not matched')