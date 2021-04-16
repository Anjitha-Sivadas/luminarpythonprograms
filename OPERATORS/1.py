#arithmatic operators
# (+,-,*,/,**-power operator,%-mod,//-floor divison to discard decimal part)
#while we using input() fn, it will always read as a string

num1=int(input("enter the first number"))
num2=int(input("enetr the second number"))
sum=num1+num2
print("sum of 2 numbers=",sum)

#relational operators
#(>,<,<=,>=,==,!=)
#for comparing
#output will be either true or false

#true-1
#false-0
#true>false=true

#logical operators
#(&-AND,|-OR,^XOR)
# AND           OR              XOR
#........................................................................................
# 00  0        00    0          00   0
# 01  0        01    1          01   1
# 10  0        10    1          10   1
# 11  1        11    1          11   0

num1=5
num2=6
print(num1&num2)

#2-0010
#4-0100
#...............
#2&4=0000

#COMPOUND ASSIGNMNET OPERATORS

#num+=1  increment operator (num=num+1)
#num-=1
