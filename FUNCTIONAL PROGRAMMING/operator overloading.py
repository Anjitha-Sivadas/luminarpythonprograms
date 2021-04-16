
class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):              #overloading
        return self.pages+other.pages

b1=Book(100)
b2=Book(200)
#b3=Book(300)  #300+b3  (int+book type)--error
print(b1+b2)


class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):  # overloading
        return Book(self.pages + other.pages)

    def __str__(self):    #while priting an object 2 string method works
        return str(self.pages)


b1 = Book(100)
b2 = Book(200)
b3=Book(300)
print(b1 + b2 + b3)    #book(300)+book(300)

#sub
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __sub__(self, other):  # overloading
        return Book(self.pages - other.pages)

    def __str__(self):    #while priting an object 2 string method works
        return str(self.pages)


b1 = Book(100)
b2 = Book(200)
b3=Book(300) 
print(b1 - b2 - b3)    #book(300)-book(300)

#mul
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __mul__(self, other):  # overloading
        return Book(self.pages * other.pages)

    def __str__(self):    #while priting an object 2 string method works
        return str(self.pages)


b1 = Book(100)
b2 = Book(200)
b3=Book(300) 
print(b1 * b2 * b3)    #book(300)*book(300)

#div
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __truediv__(self, other):  # overloading
        return Book(self.pages + other.pages)

    def __str__(self):    #while priting an object 2 string method works
        return str(self.pages)


b1 = Book(100)
b2 = Book(200)
b3=Book(300) 
print(b1 / b2 / b3)    #book(300)/book(300)
