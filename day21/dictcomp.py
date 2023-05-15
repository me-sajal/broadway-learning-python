# dictionary comprehension
a = [('name', 'john'), ('age', 23), ('dept', 'cs')]
d = {k: v for k, v in a}
print(d)
d = {i: i for i in range(5)}
print(d)
