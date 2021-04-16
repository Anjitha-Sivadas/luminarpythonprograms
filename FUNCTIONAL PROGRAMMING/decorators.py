# decorators--design pattern in python that allows a user to add new functionality to an existing object
#             without modifying its structure
#             are usually called before the definition of a function you want to decorate.

# return highest value - lowest value for all input
#normal method

# def sub(num1,num2):
#     if num1<num2:
#         (num1,num2)=(num2,num1)
#     return num1-num2
#
# res=sub(10,20)
# print(res)

def decorator_sub(fun): #1.sub(20,100)      accept fn parameter
    def inner(n1,n2): #4. (20,100)    # no of argnts in deco  == no of arg in normal fn
        if (n1<n2):  #5. (20<100)
            (n1,n2)=(n2,n1)  #6. (100,20)
        return fun(n1,n2)    #7. sub(100,20)
    return inner   #3

@decorator_sub   #1.sub(20,100)
def sub(num1,num2):
    return num1-num2

res=sub(20,100)
print(res)




