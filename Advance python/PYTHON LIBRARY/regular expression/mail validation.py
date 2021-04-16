import re
rule="([a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+[.][a-zA-Z0-9]+$)"
mail_id=input("enter your mail id")
match=re.fullmatch(rule,mail_id)
if match is not None:
    print("valid")
else:
    print("invalid")
