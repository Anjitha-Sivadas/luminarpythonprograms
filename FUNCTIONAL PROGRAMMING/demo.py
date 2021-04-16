#camellin notation--used in java,js
#addTwonumbers()

#snake notation--python
#add_twonumbers()

#normal function.....
"""
def add(num1,num2):
    return num1+num2
"""
#lambda fn--anonymous fn
add=lambda num1,num2: num1+num2
print(add(100,200))


sub=lambda num1,num2:num1-num2
print(sub(50,20))

cube=lambda num:num*3
print(cube(5))

#map()--condition that affect all the values
#filter()--extract some specific condition---condition that  dosnt affect all the values
#reduce()--reduce and provide a single value
# these are predefined fns


#map()
# pass 2 arguments
# 1.which fn we should apply for each object
# 2.on which object we want to apply the fn


#calculate square of each num
lst=[10,20,30,21,22]
# squ=[]
# for num in lst:
#     res=num**2
#     print(res)
#     squ.append(res)
# print(squ)
"""
def squ(no):
    return no**2
squares=list(map(squ,lst))
print(squares)
"""
squares=list(map(lambda no:no**2,lst))
print(squares)

cubes=list(map(lambda no:no**3,lst))
print(cubes)

#filter()......................................................................................
#filter(fn,iterables)
even=list(filter(lambda num:num%2==0,lst))
print(even)

lst=["akhil","akshay","varun","vipin","aravind","ram"]
anames=list(filter(lambda name:name[0]=="a",lst))
print(anames)

#reduce()
lst=[10,20,30,50,80]
from functools import reduce

#map() and filter() are located builtin fn.
#reduce is located in functools
total=reduce(lambda no1,no2:no1+no2,lst)
print(total)

#terminary operator
# if (no1>no2):
#     return no1
# else:
#     return no2

# n1 if n1>n2 else n2


#highest elemnt.....................................................................
max=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(max)

min=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(min)

lst=[1,2,3,4]

squares=[num**2 for num in lst]
print(squares)
