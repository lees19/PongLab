from cat import Cat

class Dog: 
    # pass

    kind = "corgi" #class variable

    #special method auto called during initialization 
    def __init__(self, name):
        self.name = name 

    #self: gives us access to attributes/methods in class
    #convention: first argument. call it whatever you like. 

    def ageset(self, age): 
        self.age = age #instance variables


d0 = Dog("Bingo")
#d0.name = "Bingo"
d0.ageset(1)
print(d0.name, d0.kind, d0.age)

d1 = Dog("Brutus")
# d1.name = "Brutus"
d1.ageset(2)
print(d1.name, d1.kind, d1.age)

c0 = Cat("Shrimp")
print(c0.name)