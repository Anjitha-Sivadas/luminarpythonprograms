class Employee:
    cname="luminar technloabs"
    def emp_det(self,id,name,age,salary):
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

    def __str__(self):
        return str(self.id)


emp=Employee()
emp.emp_det(101,"ram",23,23000)
print(emp)
