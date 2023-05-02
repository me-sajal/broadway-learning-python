# discard vs remove
# parameter pathau da xaina vane remove ma error aauxa vaney discard ma aaudaina
s = { 1, 2, 3, 4, 5}
s.remove(5) #removes 5 but if 5 is not available and throws exception
s.discard(5)

print(s)

print(s.pop()) # it randomly pops out the elements and return the element
print(s)
s.clear() #cleares the set and the set is an empty
print(s)

#copy
#difference  ,symbol : -
#intersection,symbol : &
#isdisjoint
#issubset
#issuperset
#symmetric_diffrence : complement of a intersection b, symbol : ^
#symmetric_diffrence_update :updates the value of set summetric_diffrence
    #doesnot gives any return type
#union,symbol : |
numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
a = {1, 3, 5, 7, 9, 0}
b = {2, 4, 6, 8, 0}
print(f'values of a are{a}, values of b are {b}' )
print('the diffrences of a and b is :', a.difference(b))
print('the intersection of a and b is :',a.intersection(b))
print('does a is disjoint of b:',a.isdisjoint(b))
print('is a is a subset of b:',a.issubset(numbers))
print('result for a union b:',a.union(b))
print('is a is a superset of b:',numbers.issuperset(b))
print('is a is a symmetric_diffrence of b:',a.symmetric_difference(b))
a.symmetric_difference_update(b)
print('is a is a symmetric_diffrence_update of b:',a)

c = a.copy()
print('items at a are:',c)

print(a|b) #uniom
print(a&b) #intersection
print(c-a) #diffrences
v = a^c #symmetric diff
print(v)
