lst=[4,2,1,6,7,8]
#nlst=[]
#o/p  3,1,0,7,8,9
#if num<5--sub 1 from dat num
# if num>5--add 1 from dat num

# for i in lst:
#     if(i<5):
#         i-=1
#         nlst.append(i)
#     else:
#         i+=1
#         nlst.append(i)
# print(nlst)

result=list(map(lambda num:num-1 if num<5 else num+1,lst))
print(result)

# if num<5:
#     num-1
# else:
#     num+1

