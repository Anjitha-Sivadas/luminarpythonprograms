

class Person:
    def setVal(self,name,age):
        self.age=age       # to define these attributes are inside the class itself
        self.name=name

    def printvalue(self):           # printvalue fn used to print
        print("name",self.name)
        print("age:",self.age)

obj=Person()
obj.setVal("ram",23)
obj.printvalue()