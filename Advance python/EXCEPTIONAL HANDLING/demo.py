"""
a=int(input("no1"))
b=int(input("no2"))
c=b/a
print(c)
"""
#when we give a 0 zero error will occur   zero division
#we use exceptional handling

#try....except
#at a tym only one block will work
"""
no1=int(input("no1"))
no2=int(input("no2"))
try:
    res=no1/no2
    print("result=",res)
except:
    print("exception occurs")
"""
#using list................................
# a=[1,2,3]
# print(a[7])
"""
a=[1,2,3]
try:
    i=int(input("index"))
    print(a[i])
except:                                  #except Exception as e:
    print("exception occurs")
finally:                                 #work in both case
    print("inside finally")
"""

#value error....................................
"""
try:
    a = int(input("enter your value"))
    print(a)
except:
    print("print a integer value")
   """

