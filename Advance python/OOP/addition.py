class Addition:
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def printval(self):
        print("sum of two numbers=",self.num1+self.num2)

obj=Addition()
obj.add(2,4)
obj.printval()

#OR

class Addition:
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("sum of 2 numbers=",self.num1+self.num2)

obj=Addition()
obj.add(2,4)
