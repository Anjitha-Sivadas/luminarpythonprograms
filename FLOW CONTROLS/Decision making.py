#write a prgm for voting..............................................................
"""
age=int(input("eneter your age"))
if(age>=18):
    print("u can vote")
else:
    print("u can't vote")
"""

#to check wheather the number is + or -.................................................
"""
num=int(input("enter the number"))
if(num>0):
    print("number is +ve")
elif(num==0):
    print("number is  0")
else:
    print("number is -ve")
"""

#program to check given num is even or odd...............................................
"""
num=int(input("enter a number"))
if(num%2==0):
    print("even")
else:
    print("odd")
"""

#to chechk which number is greater......................................................
"""
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
if(num1>num2):
    print("greatest number is",num1)
else:
    print("greatest number is",num2)
"""

#max of 3 numbers.......................................................................
"""
num1=int(input("enter 1st number"))
num2=int(input("enter the 2nd number"))
num3=int(input("enter the 3rd number"))
if(num1>num2)&(num1>num3):
    print(num1,"is the greatest number")
elif(num2>num1)&(num2>num3):
    print(num2,"is the greatest number")
else:
    print(num3,"is the greatest number")
"""
#print second largest elemt...........................................................
"""
num1=int(input("enter 1st no"))
num2=int(input("enter 2nd no"))
num3=int(input("enter 3rd no"))
if((num1>num2)&(num1>num3)):
    if(num2>num3):
        print(num2)
    else:
        print(num3)
elif((num2>num1)&(num2>num3)):
   if(num1>num3):
       print(num1)
   else:
       print(num3)
elif((num3>num1)&(num3>num2)):
    if(num1>num2):
        print(num1)
    else:
        print(num2)

"""
#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of services and print the net bonus amount.
"""
salary=int(input("enter your salary"))
experience=int(input("enter your year of experience"))
if(experience>5):
    print("bonus is",0.05*salary)
else:
    print("no bonus")
"""

#A student will not be able to sit in the exam if his/her attendance is less than 75%.
# Take following input from the user
#no of classes held
#no of classes attended
#and print perc of class attended
#is student is allowed to sit in xam or not
"""
classheld=int(input("no of class held"))
classattended=int(input("no of class attended"))
perc=(classheld/classattended)*100
if(perc>75):
    print("allowed")
else:
    print("not allowed")
"""
#to calculate age................................................................
"""
bdate=int(input("enter birth date"))
bmonth=int(input("enter birth month"))
byear=int(input("enter birth year"))

cdate=int(input("enter today date"))
cmonth=int(input("enter today month"))
cyear=int(input("enter today year"))

if(cdate>=bdate):
    if(cmonth>=bmonth):
        age=cyear-byear
    else:
        age=(cyear-byear)-1
else:
    if(cmonth>=bmonth):
        age=cyear-byear
    else:
        age=(cyear-byear)-1
print("age:",age)
"""
