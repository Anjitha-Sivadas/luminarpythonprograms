"""
lst=[5,41,51,25,50,10,25,85]
print(lst[1:4])   #41 51 25
print(lst[3:7])   #25 50 10 25
print(lst[2:5])   #51 25 50
print(lst[2:])    #51 25 10 25 85
print(lst[:5])    #5 41 51 25 50
print(lst[-1])    #85          neg indexing(prints last element)
print(lst[-3:])   #10 25 85
print(lst[:-2])   #[5, 41, 51, 25, 50, 10]
"""
#create list 3 4 8              3+4+8=15
#create list1 12 11 7           15-3=12   15-4=11    15-8=7

lst=[3,4,8]
lst1=[]
for i in lst:
    j=sum(lst)-i
    lst1.extend([j])
print(lst1)


#lst  5 10 20         5+10+25=35
#lst1 30 25 15        35-5=30   35-10=25  35-20=15

lst=[5,10,20]
lst1=[]
for i in lst:
    j=sum(lst)-i
    lst1.extend([j])
print(lst1)