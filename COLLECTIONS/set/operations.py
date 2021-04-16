
#operations of set..................
#union
set1={1,2,3,4,5,6}                       #remove dulpicate value
set2={5,5,6,7,8,9,10}
set3=set1.union(set2)
print(set3)
#intersection
set1={1,2,3,4,5,6}
set2={5,5,6,7,8,9,10}
set4=set1.intersection(set2)
print(set4)
#difference                                 #element should be in set1 but must not be there in set2
set1={1,2,3,4,5,6}
set2={5,5,6,7,8,9,10}
set5=set1.difference(set2)
print(set5)
set6=set2.difference(set1)
print(set6)

lst=[1,2,3,4,5,6]
#raed an elemnt from console eg 6
#return sum pairs      #(2,4)
#5    (1,4) (2,3)
#2 for lopp or  #binary search

num=int(input("enter a number"))
for i in range(0,6):
    for j in range(i+1,6):
        if(lst[i]+lst[j]==num):
            print("(",lst[i],",",lst[j],")")



#OR



#for loop
#ls\ess dan list den 2 for loop
#lower set upeer set
#read elemnt=

