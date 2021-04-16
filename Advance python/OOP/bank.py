# static===variable for removing repetition (self)
# access using class name
# memory efficiency
# related to class==static variable
# instance variable==related to object
#                    variable using self

class Bank:
    def acCreate(self,acno,aname,bname):
        self.bname=bname
        self.acno=acno
        self.aname=aname
        self.minbalace=5000
        self.balance=self.minbalace

    def deposit(self,amnt):
        self.balance+=amnt           #here we are not using self.amnt=amnt bcoz amnt is varying variable
        print("your acnt has been credited with amnt",amnt)
        print("ur current balace=",self.balance)

    def withdrawal(self,amnt):
        if(amnt>self.balance):
            print("insufficient balance")
        else:
            print("account debited with",amnt)
            self.balance-=amnt
            print("available balance=",self.balance)

obj=Bank()
obj.acCreate(123,"abc","sbi")
obj.deposit(2500)
obj.withdrawal(1500)
