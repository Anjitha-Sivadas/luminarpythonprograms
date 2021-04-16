class Mother:
    mother_name=""
    def mother(self):
        print(self.mother_name)

class Father:
    father_name=""
    def father(self):
        print(self.father_name)

class Son(Mother,Father):
    def parents(self):
        print("mother name:",self.mother_name)
        print("father name:",self.father_name)

s1=Son()
s1.mother_name="Usha"
s1.father_name="Father"
s1.parents()