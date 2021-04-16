f=open("numbers","r")
lst=[]
for num in f:
    lst.append(int(num.rstrip("\n")))
print(lst)
print(sum(lst))


#\n  represents newline
#rstrip fn used to delete last character like \n
#lstrip fn used to delete first character

