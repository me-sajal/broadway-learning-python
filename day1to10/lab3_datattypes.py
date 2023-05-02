#to check the type of data type ofdata we use type() built in fun
#for Eg
'''
Numbers
'''
a = 2e3
print(a)
print(type(a))
print(2345432e1234432123)#gives infinity output
print(1e-2)
b = 3 + 4J
#b is complex data type
print(b)
print(type(b))
'''
Lists is mutuable
'''
a = [ 1 , 2 , 3 , 4 , 5 ]
a[2] = 9
print(a[2])# gives an item at index n+1
c=["sdasd",123,"asdsd"]
print("the vale at -1 is:",a[-1])
print("the size of c list is:",len(c))

'''
Tuple is immutable
'''
a = ( 1 , 2 , 3 , 4 , 5 )
#a[2] = 9
print(a[2])

