
# Concept of making attributes private, protected and public.
# _ is used for protected.
# __ is used for private.
class Vehicle:
    def __init__(self, color, doors, mileage):
        self.color = color  # This is public attribute
        self._door = doors  # This is protected attribute
        self.__mileage = mileage  # This is private attribute
    def get_mileage(self):
        return self.__mileage
    def set_mileage(self,mileage):
        if mileage > 60:
            self.__mileage = 60
        else:
            self.__mileage = mileage
car = Vehicle("blue",4,23)
print(car.color)
car.color = "red"
print(car.color)

# protected attributes can also be accessed from outside the class but not recommended
print(car._door)
car._door = 5
print(car._door)


# Accessing the private attribute is not possible outside the class
# print(car.__milege)

print(car.get_mileage())
car.set_mileage(98)
print(car.get_mileage())

# But we can access private attributes from the outside the class in some way
print(dir(car))
# On printing above line we can see "_Vehicle__mileage attribute". so we can also access the private attributes from
# outside the class

print(car._Vehicle__mileage)    # This is also termed as name_mangling

