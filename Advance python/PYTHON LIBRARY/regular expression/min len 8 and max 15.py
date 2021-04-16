import re
response=input("enter your response")
rule="(^[a-zA-Z]{7,15}$)"
match=re.fullmatch(rule,response)
if match is not None:
    print("valid")
else:
    print("invalid")
