# after creating a class while we creating object we use constructor
# __init__
# to initialise instance variables constructor is used
# construct autoamatically invoke while calling class


class Person:
    def __init__(self,name,age):
        self.age=age
        self.name=name

    def printvalue(self):
        print("name:",self.name)
        print("age:",self.age)

obj=Person("anju",23)    # pass attributes at the time of creating class object
obj.printvalue()

