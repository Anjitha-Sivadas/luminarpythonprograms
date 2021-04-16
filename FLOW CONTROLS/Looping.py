#FOR loop  WHILE Loop

#loop-used for continous execution
#initialization,condition,incr/decre

#to print Hello............................................................
#..........................
"""
i=1
while(i<=10):
    print("Hello")
    i+=1
"""
#to print 1 to 10.........................................................
"""
i=1
while(i<=10):
    print(i)
    i+=1
"""
#to print from 10 to 0 in decrement order.................................
"""
i=10
while(i>=0):
    print(i)
    i-=1
"""
#to print multiplication table of a given number upto 10....................
"""
num=int(input("enter the number"))
i=1
while(i<=10):
    result=i*num
    print(i,"*",num,"=",result)
    i+=1
"""

#to print 1 to n.............................................................
"""
num=int(input("enetr the number"))
i=1
while(i<=num):
    print(i)
    i+=1
"""

#to print from lower limit to upper limit.....................................
"""
lowerlimit=int(input("enter thr lower limit"))
upperlimit=int(input("enter the upper limit"))
while(lowerlimit<=upperlimit):
    print(lowerlimit)
    lowerlimit+=1
"""

#from lower limit to upper limit and print only even numbers b/w them.........
"""
lower=int(input("enter the lower limit"))
upper=int(input("enter the upper limit"))
while(lower<=upper):
    if(lower%2==0):
     print(lower)
    lower+=1
"""

#FOR LOOP
#initialization condition inc or dec
"""
for i in range(0,10):   ##uoerlimit=uperlimit-1
    print(i)            #default it will increment by 1
"""
"""
for i in range(0,11,2):
    print(i)
"""
#print from 10 to 0........................................................
"""
for i in range(10,-1,-1):
    print(i)
"""
#from lowerlimit to upperlimit........................................
"""
lower=int(input("enter the lowerlimit"))
upper=int(input("enter the upperlimit"))
for i in range(lower,upper+1):
    print(i)
"""
#from lower to upper print even nos....................................
"""
lower=int(input("enter the lower limit"))
upper=int(input("enter the upper limit"))
for i in range(lower,upper+1):
    if(i%2==0):
        print(i)
"""
#evensum nd oddsum.................................................
"""
lower=int(input("enter the lower limit"))
upper=int(input("enter the upper limit"))
evensum=0
oddsum=0
for i in range(lower,upper+1):
    if(i%2==0):
        evensum+=i
    else:
        oddsum+=i
print("evensum is",evensum)
print("oddsum is",oddsum)
"""
#to check prime number
"""
num=int(input("enter a number"))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=1
        break
    else:
        flag=0

if(flag>0):
    print("not prime")
else:
    print("prime")
"""
#lower to upper, print prime nos

lower=int(input("enter a lower limit"))
upper=int(input("enter a upper limir"))
flag=0
for i in range(lower,upper):
    for num in range(2,i):
        if(i%num==0):
            flag=1
            break
        else:
            flag=0
    if(flag==0):
        print(i)






