#adv     using ref we can create many objects
class Employee:
    def setvalue(self,id,name,age,salary):
        self.id=id
        self.name=name
        self.age=age
        self.salary=salary

    def printvalue(self):
        print("id:",self.id)
        print("name:",self.name)
        print("age:",self.age)
        print("salary:",self.salary)

emp=Employee()
emp.setvalue(101,"ram",23,23000)
emp.printvalue()



