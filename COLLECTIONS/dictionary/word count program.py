line="hai hello hai hello hai"
#count no of word   hai 3, hello 2.......................................

#to covert line by line datas to word by word data   split
print(line)
words=line.split(" ")
print(words)


#create empty dic
#check whether der is a word in dic, if not add to dic and keep value as 1
line="hai hello hai hello hai"
words=line.split(" ")
print(words)
dic={}
for i in words:
    if(i not in dic):
        dic[i]=1
    else:
        dic[i]+=1
print(dic)

