lst=[]
evenlst=[]
oddlst=[]
for i in range(50,201):
    lst.append(i)
    if(i%2==0):
        evenlst.append(i)
    else:
        oddlst.append(i)
print(lst)
print(evenlst)
print(oddlst)
