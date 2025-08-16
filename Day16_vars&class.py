class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Tusu", 20)
print(vars(p))

#vars creates a dictionary out of all the attributes that belong to that object