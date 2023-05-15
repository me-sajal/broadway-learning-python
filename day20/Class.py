class A:
    a = 1    # class attribute
    def __init__(self,b):   # class constructor
        self.b = b      # object / instance attribute

obj = A(2)
print(obj.a)
print(obj.b)

