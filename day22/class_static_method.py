class Person:
    __age = 30
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
    @classmethod
    def set_age(cls,age):
        cls.__age = age
    @classmethod
    def get_age(cls):
        return cls.__age
#print(Person.__age)
print(Person._Person__age)
Person.set_age(44)
print(Person.get_age())


########################################################################################################################
from datetime import datetime
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @classmethod
    def from_dob(cls, name, year):
        return cls(name, datetime.today().year-year)



p = Person.from_dob("ram", 2002)
print(p.age)


########################################################################################################################

class Distance:
    def __init__(self, in_kms):
        self.in_kms = in_kms

    @classmethod        # this is called factory method
    def (cls,inmiles):
        return cls(inmiles * 1.6)   # converts the given miles into the kilometers
    @staticmethod
    def message (dis)
        if d < 20:
            return "It was too short distance"
        return "It was way too long"

dis =Distance.from_miles(32)
abc = Distance
abc.message(dis)
print(dis.in_kms)
