class Employee:
    cname="luminar technloabs"
    def __init__(self,id,name,age,salary):
        self.id=id
        self.name=name
        self.age=age
        self.salary=salary

    def printvalue(self):
        print(Employee.cname)
        print("id:",self.id)
        print("name:",self.name)
        print("age:",self.age)
        print("salary:",self.salary)


emp=Employee(101,"ram",23,23000)
emp.printvalue()

emp1=Employee(102,"sam",24,25000)
emp1.printvalue()