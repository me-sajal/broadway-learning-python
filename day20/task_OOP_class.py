class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = 22 / 7 * self.radius * self.radius
        return area


c1 = Circle(23) # this is an object instantiation
print(c1.get_area())
