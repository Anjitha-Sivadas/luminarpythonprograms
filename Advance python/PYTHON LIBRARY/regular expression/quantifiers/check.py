#1
"""
import re
x="a+"      #including group
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())

#2
import re
x="a*"  #count including zero no of a
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())

#3
import re
x="a?" #count a as each including zero no of a
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())

#4
import re
x="a{2}" #2 no of a position
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())

#5
import re
x="a{2,3}" #minimum 2 a and maximum 3 a
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())

#6
import re
x="^a" #check starting with a
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())

#7
import re
x="a$" #check ending with a
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
"""
