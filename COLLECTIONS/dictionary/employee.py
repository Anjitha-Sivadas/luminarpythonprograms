#employee
#id, name,designation,salary  (key value)
#1.name return
#1.check company
#1.add company
#company luminar
#1.salary+15000
#1.print all keys value pair

employee={"id":101,"ename":"anju","designation":"software engineer","salary":1000,"id":102}

print(employee["ename"])
print("cname" in employee)
employee["cname"]="luminar"
employee["salary"]+=15000
for i in employee:
    print(i,":",employee[i])
    
print(employee["id"])
