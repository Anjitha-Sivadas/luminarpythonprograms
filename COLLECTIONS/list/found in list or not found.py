#LINEAR SEARCH
#Drawback=Complexity increases
lst=[10,20,30,40,50,60]
num=int(input("enter an element to search"))
flag=0
for i in lst:
    if(i==num):
        flag=1
        break
    else:
        pass

if(flag>0):
    print("element found")
else:
    print("element not found")
