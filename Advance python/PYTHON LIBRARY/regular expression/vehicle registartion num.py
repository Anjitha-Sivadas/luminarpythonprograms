import re
valid=[]
rule="[a-zA-Z]{2}\d{2}[a-zA-Z]{2}\d{4}"
f=open("vehicle reg num","r")
for num in f:
    number=num.rstrip("\n")
    matcher=re.fullmatch(rule,number)
    if matcher!=None:
        valid.append(number)
print(valid)
