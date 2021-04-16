# to identify an object using an attribute
class College:
    collegename="LT"
    def __init__(self,name,roll):
        self.roll=roll
        self.name=name
    def printdetails(self):
        print("college name=",self.collegename)
        print("name of student",self.name)
        print("rollno",self.roll)
    def __str__(self):
        return self.name+" "+str(self.roll) # in 2string method we want
                                # to give in string format. for that str() used
    # +--concatinate
ob=College("anju",4)
print(ob)

