#file  operation
#read (to read a file)         r
#write (to write a file)       w
#append (to add/append)        a

#for every operation, first we want to create a file referance
# syntax for file referance
f=open("filepath","mode of operation")
#eg:
f=open("filepath","r")    # referance to read a file
f=open("file path","w")   # referance to write
f=open("file path","a")   # referance to append