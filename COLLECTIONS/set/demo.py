"""
set1={1,2,3}                  #to create set use curly bracket nd insert values(must)
print(type(set1))
# to create empty set use set fn
set2={}                 #using empty curlly bracket it will become dict
print(type(set2))

set={6,2.5,"sabir",True}       #supports hetrogenous value
print(set)
set={1,2.5,"sabir",2.5,1}     #do not support duplicate value
print(set)
set={5,6,1,2.5,"sabir"}        #insertion order not preserved
print(set)
                               #mutable
#to make a lst in to set
lst=[10,10,20,20,25,25,85,41,41,25,58]
lst1=set(lst)
print(lst1)
"""

set={1,2,3}
set.add(4)                     #to add an element  use add() fn
set.add("luminar")
print(set)

set.update([10,50,"sabir"])     #to add multiple values    update() fn  and by suing square bracket
print(set)

