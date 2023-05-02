#shallow copy and deep copy
a=[[2,3,4,4],[3,4,5,7],[1,3,57,8],[2,6,9,2]]
b=a.copy() #b is a shallow copy of a

b[0][1] = 6
print(a)
print(b)

from copy import deepcopy
b=deepcopy(a)
b[0][1] = 6
print(a)
print(b)