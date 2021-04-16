class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b

obj=Calc(5,2)
print(obj.add())       #since we r using return, we want to use print while calling
print(obj.sub())
print(obj.mul())
print(obj.div())

