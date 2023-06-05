# def addtion(a, b):
#     return a + b
#
# def addtion(a, b, c):
#     return a + b + c
# print(addition(2, 3)
# print(addition(2, 3, 5)
# The above given function overloading won't work in the python as above given

# We can give the feel of function overloading in following ways but it is not actually the overloading
def addition(a, b, c=0):
    return a + b + c


print(addition(2, 3))
print(addition(2, 3, 4))


def addition(*a):
    return sum(a)


print(addition(2, 3))
print(addition(2, 3, 4))
print(addition(2, 3, 4, 5))
print(addition(2, 3, 4, 5, 6))

# len() function is also one of the examples of polymorphism
print(len([1, 2, 3, 4, 5, 6]))  # for list
print(len((1, 2, 3, 4, 5, 6)))  # for tuples
print(len({1, 2, 3, 4, 5, 6}))  # for sets


# Method overloading example

class Shape:
    def area(self, l):
        return l*l
    def area(self, l, b = None):
        if not b:
            return l*l
        return l*b

square = Shape()
rect = Shape()
print(square.area(5))
print(rect.area(2, 3))


