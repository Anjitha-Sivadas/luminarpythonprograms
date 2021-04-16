#list properties.......................................................................
"""
lst=[]   #emplty list    #square bracket
st=list()         #using fn
print(type(lst))
print(type(st))


lst1=[10,10.5,"luminar","python",True]     #it support hetrogenous data
print(lst1)

lst2=[10,10,10.5,10.5,"sabir","sabir"]     #it allows duplicate value
print(lst2)

lst3=[True,0,1,False,"sabir",10.5]         #insertion order preserved
print(lst3)

lst=[10,8,7,9,1,2,100,45,"sabir"]          #index value 0 to n-1
print(lst[2])
print(lst[5])                              #list is mutable (by using index value)
lst[1]=50
print(lst)
lst[8]="luminar"
print(lst)

"""
#list iteration........................................................................
lst=[10,20,21,22,23,24]
for i in lst:
    print(i)