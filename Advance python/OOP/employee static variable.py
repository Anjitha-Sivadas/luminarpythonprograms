class Employee:
    cname="luminar technloabs"
    def setvalue(self,id,name,age,salary):
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


emp=Employee()
emp.setvalue(101,"ram",23,23000)
emp.printvalue()

emp1=Employee()
emp1.setvalue(102,"sam",24,25000)
emp1.printvalue()