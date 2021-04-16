# parent class  base class superclass
# child class derived class
#single inheritance- A class inherits properties from a single class......................................................

class Parent:
    parent_name = "Arun"

    def m1(self, age):
        self.age = age
        print("my name is ", Parent.parent_name)
        print("my age is", self.age)

class Child(Parent):  # inheritance--while using inheritance, we must give
                      # parent class name
    def m2(self, cage):
        self.cage = cage
        print("my parent name is", Parent.parent_name)
        print("my parent age is ", self.age)
        print("child age is ", self.cage)


c = Child()
c.m1(23)  # we must call m1 first and m2 next
c.m2(16)  # as in python line by line interpretation,so we must give value first
          # then we can call

