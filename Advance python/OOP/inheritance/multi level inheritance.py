#multi level inheritance-- A class inherits properties from a class
                           # which again has inherits properties.
class Family:
    def show_family(self):
        print("This is our family:")

#father class inherited from family
class Father(Family):
    fathername=""
    def show_father(self):
        print(self.fathername)

#mother class inherited from family
class Mother(Family):
    mothername=""
    def show_mother(self):
        print(self.mothername)

#son class is inherited from father and mother
class Son(Father,Mother):
    def show_parent(self):
        print("Father:",self.fathername)
        print("Mother:",self.mothername)

s1=Son()
s1.fathername="Sivadasan"
s1.mothername="Usha"
s1.show_family()
s1.show_parent()

