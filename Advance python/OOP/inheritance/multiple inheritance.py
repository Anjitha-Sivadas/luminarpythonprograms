#multiple inheritance--child class inherited from more than one parent class
# one child class can inherit from multiple parent classes.
class Parent:
    parent_name = "Arun"

    def m1(self, age):
        self.age = age
        print("my name is ", Parent.parent_name)
        print("my age is", self.age)
class Mobile:
    def mob(self):
        print("i have one plus")


class Child(Parent,Mobile):  # inheritance--while sung inheritance, we must give
                             # parent class name
    def m2(self, cage):
        self.cage = cage
        print("my parent name is", Parent.parent_name)
        print("my parent age is ", self.age)
        print("child age is ", self.cage)


c = Child()
c.m1(23)  # we must call m1 first and m2 next
c.m2(16)  # as in python line by line interpretation,so we must give value first
c.mob()   # then we can call