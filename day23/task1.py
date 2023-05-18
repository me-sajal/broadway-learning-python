class Person:
    def __init__(self, name, age):
        self. name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, age: {self.age} "



class Employee(Person):
    def __init__(self, name, age, salary, deg):
        self.salary = salary
        self.deg = deg
        super().__init__(name,age)

    def get_details(self):
        print(super().get_details())
        return f"Name: salary :{self.salary}, degination : {self.deg} "

p1 = Employee("saja",21,1200,"trainee")
print(p1.get_details())