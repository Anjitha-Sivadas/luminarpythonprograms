#FUNCTIONS
#normal syntax
"""
def functionname(arguments):
    function defination

function call   #by using fn name
"""
#three methods
#1 Fn without an arguments and no return type.....................................
"""
def add():
    num1=int(input("enter numb1"))
    num2=int(input("enter a numb2"))
    sum=num1+num2
    print(sum)
add()
"""
"""
def sub():
    num1=int(input("enter numb1"))
    num2=int(input("enter numb2"))
    sub=num1-num2
    print(sub)
sub()
"""
"""
def mul():
    num1=int(input("enter numb1"))
    num2=int(input("enter numb2"))
    mult=num1*num2
    print(mult)
mul()    
"""
#2 Fn with arguments and no return type....................................................
"""
def addition(num1,num2):
    sum=num1+num2
    print(sum)
addition(30,50)  #give values of arguments


def substraction(num1,num2):
    sub=num1-num2
    print(sub)
substraction(20,10)

def multiN(num1,num2):
    mult=num1*num2
    print(mult)
multiN(2,2)

"""
#3 Fn with arguments and return type................................................................
"""
def sumN(num1,num2):
     sum=num1+num2
     return sum
 data=sumN(50,25)
 print(data)


def subN(num1,num2):
    sub=num1-num2
    return sub
data=subN(20,10)
print(data)


def mulN(num1,num2):
    mul=num1*num2
    return mul
data=mulN(5,5)
print(data)

"""