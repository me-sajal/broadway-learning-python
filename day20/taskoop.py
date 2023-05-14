class circle:
    def __init__(self,redius):
        self.redius = redius
    def get_area(self):
        area = 22/7*self.redius*self.redius
        return area
c1 = circle(23)
print(c1.get_area())
