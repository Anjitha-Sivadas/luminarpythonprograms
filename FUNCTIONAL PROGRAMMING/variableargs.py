# variable length argument method--here we can call by using many no of arguments
# *args
# here args type is tuple
def add(*args):
    sum=0
    for num in args:
        sum+=num
    return sum
res=(add(10,20,30))
print(res)

