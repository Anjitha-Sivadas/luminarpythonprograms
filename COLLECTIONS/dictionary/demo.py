dic={}     #using curly bracket
#key value pairs to store values

#roll no-1001
#name-arun
#age=25

#key:roll,name,age
#1001,arun,25    # values
student={"roll":1001,"name":"arun","age":25}       #it support hetrogenous data
print(student)
student1={"roll":1001,"name":"arun","age":25,"age":30,"cpp":25}   #doesnot support duplicate key
print(student1)                                                   #support duplicate values
                                                                  #insertion order is preserved
                                                                  #mutable
print(student1["age"])    #if we want to fetch value, we have to use corresponding key

#roll"1001
#name:arun
#age:25
#cpp:25

for i in student1:
    print(i,":",student1[i])   #if we want to fetch key along with value

#to update a value...........................................
student1["name"]="arjun"
print(student1)
student1["age"]=50
print(student1)
student1["cpp"]+=10
print(student1)

#to delete a value and key
#del
del student1["cpp"]
print(student1)

#to add total as key and 150 as value
print("total" in student1)          #to check whether der is a total as key or not
student1["total"]=150               #added a key nd value
print(student1)
