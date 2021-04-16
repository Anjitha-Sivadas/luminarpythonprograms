#same method name for parent class nd child class
#child class method override parent class method
#work child class method

class Parent:
    def properties(self):
        print("10 lakhs rs,2car")
    def marry(self):
        print("with ram")

class Child(Parent):
    def marry(self):
        print("with arun")

c=Child()
c.marry()
