"ABCDBCA"
#{}
#A  1
#B  1
#C   1
#D   1

line="ABCDBCA"
dic={}
for i in line:
    if(i not in dic):
        dic[i]=1
    else:
        break
print("First recurssive character",i)
