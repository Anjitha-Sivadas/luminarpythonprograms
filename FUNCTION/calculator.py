#1.add
#2.sub
#3.mult
#4.div

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
print("select operations\n"
      "1.Addition\n"
      "2.substraction\n"
      "3.multiplication\n"
      "4.division\n")
select=int(input("select operations"))
number1=int(input("enter first number"))
number2=int(input("enter second number"))

if select==1:
    print(number1,"+",number2,"=",add(number1,number2))
elif select==2:
    print(number1,"-",number2,"=",sub(number1,number2))
elif select==3:
    print(number1,"*",number2,"=",mul(number1,number2))
elif select==4:
    print(number1,"/",number2,"=",div(number1,number2))
else:
    print("invalid input")




