a = 1, 2, 3, 4 
print(a)
#note there is no small bracket but still crates tupple 
#and called tupple packing
#the element in the rhs are asigned ti each variables in the lhs. This 
# is
#called tuple
#unpacking
a, b, c = 1, 2, 3
print(a, b, c)

#we can swap the variables in python withoout using the third variable 
#eg:
a = 2
b = 4
print("the value before swapping is:")
print("a = ", a)
print("b = ", b)
a, b = b, a
print("the value swapping swapping is:")
print("a = ", a)
print("b = ", b)

#tupple slicing
#new 
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a[:]) # This gives all the elements in the tuples

# This traverse through all the elements
#in the tuple but return the element in the jump of 1
print(a[::2]) 

# Negative step slicing
a = (0, 1, 2, 3, 4, 5, 6, 7)
print(a[-1: -6: -1]) # this gives  6 5 4 3 
print(a[::-1]) # this reverse the tuples 7 6 5 4 3 2 1
print(a[::-2]) #this gives reverse with the jumping by 1 variable


#to delete tupples
del a

