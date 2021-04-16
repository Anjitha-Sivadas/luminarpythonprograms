# used for pattern matching
# re-package for regular expression (pattern matching)
# mainly used for validation
# finditer  used for counting how many times of series
#must use package name for calling



import re
count=0
matcher=re.finditer("ab","abaabbab")
for match in matcher:
    print("match available at",match.start()) # to check in which position
                                               # match is available
    print("group:",match.group())  # to print the group name
    count+=1
print("count=",count)

