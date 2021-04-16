#create a new list which contains salary of all employees
#normal fn

class Employee:
    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary

    def printVal(self):
        print(self.ename)

e1=Employee(1000,"varun","developer",25000)
e2=Employee(1001,"vivek","engineer",24000)
e3=Employee(1002,"vinod","qa",27000)
e4=Employee(1003,"vineeth","arkt",28000)
employees=[]
employees.append(e1)
employees.append(e2)
employees.append(e3)
employees.append(e4)
# sal=[]
# for emp in employees:
#     sal.append(emp.salary)   #to append salary
# print(sal)

#anonymous fn
sal=list(map(lambda emp:emp.salary,employees))
print(sal)
#to find highest salary
msal=max(list(map(lambda emp:emp.salary,employees)))
print(msal)






