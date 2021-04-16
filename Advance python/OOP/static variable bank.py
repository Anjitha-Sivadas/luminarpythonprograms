#static variable is initialised inside a class not inside a method( in instance variable)
#static variable is accesed using classname.variablename
# instance variable---related to objects
# static variable---related to class
# adv of static variable  memory efficiency (repetition is removed)
class Bank:
    bname="sbi"          #static variable
    def acCreate(self,acno,aname):
        self.acno=acno
        self.aname=aname
        self.minbalace=5000
        self.balance=self.minbalace

    def deposit(self,amnt):
        self.balance+=amnt
        print("your",Bank.bname,"acnt has been credited with amnt",amnt)  #classname.varname
        print("ur current balace=",self.balance)

    def withdrawal(self,amnt):
        if(amnt>self.balance):
            print("insufficient balance")
        else:
            print("account debited with",amnt)
            self.balance-=amnt
            print("available balance=",self.balance)

obj=Bank()
obj.acCreate(123,"abc")
obj.deposit(2500)
obj.withdrawal(1500)