f=open("data","r")
dic={}
for lines in f:
    words=lines.rstrip("\n").split(" ")
for i in words:
    if(i not in dic):
        dic[i]=1
    else:
        dic[i]+=1
print(dic)


