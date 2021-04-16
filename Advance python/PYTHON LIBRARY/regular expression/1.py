import re
n="helloo"
x="\w{6}"  #6--letters
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")

# when 2 strings are matched,value will stored in match variable
# otherwise match will be null
