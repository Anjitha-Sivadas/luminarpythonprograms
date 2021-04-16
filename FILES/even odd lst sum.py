f=open("numbers","r")
elst=[]
olst=[]
for num in f:
    if(num%2==0):
        elst.append(num.rstrip("\n"))
        #flag=1
    else:
        olst.append(num.rstrip("\n"))
        #flag=0
print(elst)
print(olst)
print(sum(elst))
print(sum(olst))

