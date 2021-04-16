lst=[10,20,21,22,23,24]
#result
#10**1=
#20**2                         #find len....nd repeat for loop till len
#21**3
#22**4
#23**5
#24**6

len(lst)
for i in lst:
    for j in range(1,len(lst)):
        result=i**j
        print(i,"**",j,"=",result)

# for i in range(0,len(lst)):
#     print(lst(i,"**",i+1,"=",lst(i**i+1)))



