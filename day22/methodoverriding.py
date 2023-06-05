class Shape:
    def area(self, l):
        return l*l
    def area(self, l, b = None):
        if not b:
            return l*l
        return l*b


class Sqr(Shape):
    def area(self, l):
        return l * l

class Rect(Shape):
    def area(self, l, b = None):
        if not b:
            return l*l
        return l*b

sqrtable = Sqr()
print(sqrtable.area(25))

recttable = Rect()
print(recttable.area(25, 11))

########################################################################################################################

class Parent:
    def __init__(self, name, age):
        self. name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, age: {self.age} "


class Child(Parent):
    def __init__(self, name, age, fact, batch):
        self.fact = fact
        self.batch = batch
        super().__init__(name, age)

    def get_info(self):
        print(super().get_info())   # this helps to get all the values at the super class
        return f"name :{self.name}, age: {self.age}, faculty : {self.fact} and batch : {self.batch}."

childobj = Child("ram",23 , "cs", 2019)
print(childobj.get_info())