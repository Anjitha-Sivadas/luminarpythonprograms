# List comprehension offers a shorter syntax when you want to create a new list
# based on the values of an existing list.

lst=[1,2,3,4,5,6]
squares=[num**2 for num in lst]
print(squares)
even=[num for num in lst if num%2==0]
print(even)



