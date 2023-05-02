
"""
this is multi line comment

"""
a=4
b=8
#Arithemetic Operator
print("Arithemetic Operator")
#add
c = a + b
print(c)
#diff
c = a - b
print(c)
#mul
c = a * b
print(c)
#div
c = a / b
print(c)
#mod
c = a % b
print(c)
#exponent
c = a ** b
print(c)
#floor division
c = a // 2
print(c)


""""
comprasion operators
"""
print("comprasion operators")
#equals to
print(a == b)
#not equals to
print(a != b)
#grater than
print(a > b)
#less than
print(a < b)
#grater than or equal to
print(a >= b)
#less than or equal to
print(a <= b)
""""
logical operators
"""
print("logical operators")
a = True
b = False
#and
print(a and b)
#or
print(a or b)
#not
print(not a)
print(not b)
"""
identety operator
"""
print("identety operator")
a = 1
b = 1
c = 3
print(a is b)
print(a is not b)
print(a is c)
print(a is not c)
"""
membership operator
"""
print("membership operator")
a = [2,3,4,5,6]
print(2 in a)
print(8 in a)
"""
assignment operator
"""
print("assignment operator")
a = 2
print(a)
a += 1
print(a)

"""
precedence and associativity 
"""
print(3 * 5 // 5)#associativity left to right 
print (3 ** 2 ** 2)#associativity right to left

#syntax examples
a = 1
b = 1
if a == b:
    print(" a is equal to b")
    print("the value is :",a)
else:
    print("the value is not equal .i.e: a =", a , "b =",b)
