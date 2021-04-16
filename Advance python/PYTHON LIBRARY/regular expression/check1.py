"""
#1

import re

x="[abc]"  #either a or b or c
matcher=re.finditer(x,"abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())

#2
import re

x="[^abc]"  #except a b c
matcher=re.finditer(x,"abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())

#3
import re

x="[a-z]"  #from a to z      for caps x="[A-Z]"   For both X="[a-zA-Z]"
matcher=re.finditer(x,"abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())

#4
import re

x="\s"  #to check space
matcher=re.finditer(x,"abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())

#5
import re

x="\w"  #all words except special character
matcher=re.finditer(x,"abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())


#6
import re
x="\W"  #for spcl character
matcher=re.finditer(x,"abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())

#7
import re #check digits
x="\d"
matcher=re.finditer(x,"abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())
"""
#8
import re
x="\D"   #except digits
matcher=re.finditer(x,"abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())





