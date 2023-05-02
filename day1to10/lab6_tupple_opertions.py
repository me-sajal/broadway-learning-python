import os
clear = lambda:os.system('cls')
clear()

a = (1, 2, 3)
b = (4, 5, 6)
print( a + b ) # this give a third tupple a + b
print( a * 3 ) # this gives 3 times a 
print("1" in a) # this gives false
print(1 in a) # this gives true
print("5" in a) # this gives false
# there are only two methods in the index count and index 
# eg:
print(a.count(2)) # this gives 1 because it has 1 2
print(a.index(2)) # this gives 1 because it lies in index 2
# a.index(1,1,4) this is for to search 1 in range between 1 to 4

import os
clear = lambda:os.system('cls')
clear()

a=(1, 2, 3, 1, 9,  4, 5)
print(sum(a)) # this gives sum of all elements in a tupple
print(max(a))
print(min(a))
print(sorted(a))
print(list(reversed(a)))
print(list(reversed(sorted(a))))
