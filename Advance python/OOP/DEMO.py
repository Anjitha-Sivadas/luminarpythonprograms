#class          design pattern
#object         real world entity
#reference      name that refers a memory location of a object
#referances     to do operations on object, provide memory locations

#eg:
#class: tv
#object: samsung lg etc
#reference: remote

class Person:      # first letter of a class name should be cap letter
    def walk(self):    # using fn we create methods    self: it says t is inside the class(point to current instance)
        print("person is walking")     # variables using self is known as instance
                                       #walk run jumping are methods
    def run(self):
        print("person is running")

    def jumping(self):
        print("person is jumping")


obj=Person()     # reference name obj,  we using reference by specifying class name
obj.walk()       # using refe name we call methods
obj.run()
obj.jumping()

ab=Person()         #2ndobject suing ab reference
ab.walk()

