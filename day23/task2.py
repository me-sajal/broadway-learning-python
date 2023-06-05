#Create a class Department with parameters name and number_of_students. Create a method total students, which takes object as a parameter and return the total number of students from all departments.
class Dept:
    name = ""
    numbers = 0
    n = 0


    def __init__(self,nameofdept, noofstudents):
        self.namedept = nameofdept
        self.noofstudent = noofstudents

    def __add__(self, other):
        return self.namedept+other.namedept,self.noofstudent+other.noofstudent

    def totalsudent(self,*a):

        return self.noofstudent + sum([i.noofstudent for i in a])


dept1 = Dept("science", 21)
dept2 = Dept("mgmt", 21)
dept3 = Dept("hum", 21)
print(dept3.totalsudent(dept1, dept2))
print(dept3+dept1)