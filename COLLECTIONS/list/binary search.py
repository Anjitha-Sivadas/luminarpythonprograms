#BINARY SEARCH
#to reduce the complexity of linear search we use binary search
#binary search is a type of sorting

#ALGORITHM....................................................................................................
#1. sorting of array/list
#     sort fn.....lst.sort()
#2. define a variable low=0
#   set a variable upper on last of the prgm    upp=len(lst)-1
#3. calculate mid
#     mid=(low+upp)//2
#4. check three conditions
#   a. if the elemnt we are searching    if(elemnt>lst[mid])
#       low=mid+1
#   b. if(elemnyt<lst[mid])
#        upp=mid-1
#   c. if(elemnt==lst[mid])
#       print("elemnt found")

lst=[2,1,3,5,4,6,8,7]
lst.sort()
low=0
upp=len(lst)-1                                      #7
num=int(input("enter an element to search"))        #6
flag=0
while(low<=upp):                                    #(0<=7)
    mid=(low+upp)//2                                #3

    if(num>lst[mid]):
        low=mid+1
    elif(num<lst[mid]):
        upp=mid-1
    elif(num==lst[mid]):
        flag=1
        break

if(flag>0):
    print("element found")
else:
    print("element not found")
