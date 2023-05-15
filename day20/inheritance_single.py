# # Types:
#     Single
class Vehical:
    def __init__(self, color, doors):
        self.color = color
        self.doors = doors


class Car(Vehical):
    def get_car_info(self):
        return f"The car has color {self.color} and has {self.doors} doors."


rover = Car("red", 4)
print(rover.color)
print(rover.doors)
print(rover.get_car_info())


######################################################################################################
class Vehical1:
    def __init__(self, capacity, doors):
        self.capacity = capacity
        self.doors = doors

    def get_car_info(self):
        return f"hello from vehical to car where capacity is {self.capacity} and {self.doors} doors"


class Car1(Vehical1):

    def __init__(self, capacity, doors, mileage, colors):
        self.mileage = mileage
        self.colors = colors
        super().__init__(capacity, doors)

    def get_car_info(self):
        print(super().get_car_info())
        return f"The car has color {self.colors} has {self.doors} doors with the seat capacity{self.capacity} and mileage {self.mileage}."


rover = Car1(5, 4, 24, "blue")
print(rover.colors)
print(rover.doors)
print(rover.get_car_info())

#     Multiple
#     Multilevel
#     sd
#     asd
