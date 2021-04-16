employee=[[1001,"arun",15000],       #nested list
          [1002,"arjun",20000],
          [1003,"vinu",25000],
          [1004,"binu",10000]]
print(employee)

for i in employee:                 #to collect seperate employee details
    print(i)

for i in employee:
   print(i[1])

#print employee name whose salary greayer than 17000

for i in employee:
    if(i[2]>=17000):
        print(i[1])

#to print total salary
sum=0
for i in employee:
    sum=sum+i[2]
print(sum)