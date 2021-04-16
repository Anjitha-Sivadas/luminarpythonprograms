#sum of n numbers
"""
num=int(input("enter the number"))
i=1
sum=0
while(i<=num):
    sum=sum+i
    i+=1
print(sum)
"""
num=int(input("enter number"))
sum=0
for i in range(0,num+1):
    sum+=i
print(sum)
#to print the number in reverse order
"""
num=int(input("enter a number"))
result=0
while(num!=0):
    digit=num%10
    result=(result*10)+digit
    num=num//10
print(result)
"""

#read 4 sub mark, total mark 200 nd calculate perc, perc above 90 aplus, 80-83 a, 70-79 bplus,60-69 b, 50-59 c+, 40-49 c, 30-39-d+
"""
sub1=int(input("enter mark1"))
sub2=int(input("enter mark2"))
sub3=int(input("enter mark3"))
sub4=int(input("enter mark4"))
total=sub1+sub2+sub3+sub4
perc=(total/200)*100
if(perc>=90):
    print("A+")
elif(perc>=80)&(perc<=89):
    print("A")
elif(perc>=70)&(perc<=79):
    print("B+")
elif(perc>=60)&(perc<=69):
    print("B")
elif(perc>=50)&(perc<=59):
    print("C+")
elif(perc>=40)&(perc<=49):
    print("C")
elif(perc>=30)&(perc<=39):
    print("D+")
else:
      print("fail")

"""
