import re
n=input("enter your response")
x="(^a[a-zA-Z0-9\w]*b$)"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
    