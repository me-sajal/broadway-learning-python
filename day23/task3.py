# Create a class Circle with an attribute radius. Create two objects of circle c1 and c2. Add the radius of the circles and print the result.
# Do the above task using a method and then a magic method.
# Compare the size of the circle and print the result using magic method.
class Circle:
    def __init__(self,red):
        self.red = red

    def totalred(self,redi):
        return self.red +redi.red

    def __add__(self, other):
        return self.red+other.red


    def __gt__(self, other):
        if(self.red<other.red):
            return f"{self.red} is greater "
        else:
            return f"{self.red} is greater"


c1 = Circle(21)
c2 = Circle(23)
print(c2.totalred(c1))
print(c1 > c2)