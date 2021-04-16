"""
for i in range(1,4):
    for j in range(1,4):
        print(i)
"""

#1 1 1
#2 2 2
#3 3 3
"""
for i in range(1,4):
        for j in range(1,4):
            print(i,end="  ")
        print() #to go to next line
"""

#1 2 3
#1 2 3
#1 2 3
"""
for i in range(1,4):
    for j in range (1,4):
        print(j,end=" ")
    print()
"""

#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
"""

#10 9 8 7 6 5 4 3 2 1
#9 8 7 6 5 4 3 2 1
#8 7 6 5 4 3 2 1
#7 6 5 4 3 2 1
#6 5 4 3 2 1
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1
"""
for i in range(11,0,-1):
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()

#OR
for i in range(0,10):
    for j in range(10-i,0,-1):
        print(j,end=" ")
    print()
"""
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5
for i in range(0,6):
    for j in range(0,i):
        print(i,end=" ")
    print()
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
"""

#5 5 5 5 5
#4 4 4 4
#3 3 3
#2 2
#1
"""
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
"""
#1 1 1 1 1
#2 2 2 2
#3 3 3
#4 4
#5
"""
for i in range(1,6):
    for j in range(i,6):
        print(i,end=" ")
    print()
"""

#5 5 5 5 5
#5 5 5 5
#5 5 5
#5 5
#5
"""
for i in range(1,6):         # (5,0,-1)
    for j in range(i,6):     #(0,i)
        print("5",end=" ")
    print()
 """

#0 1 2 3 4 5
#0 1 2 3 4
#0 1 2 3
#0 1 2
#0 1
"""
for i in range(6,0,-1):
    for j in range(0,i):
        print(j,end=" ")
    print()
"""