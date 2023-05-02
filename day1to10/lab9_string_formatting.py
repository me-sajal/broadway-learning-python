############## string formatting with %
# %s for string
# %d for integer
# %f for float

value = 'hello from %s. I\'m learning %s'%('tinkune','python')
print(value)




############ string fotmatting using format




#default values where 1 by 1 is inserted as a postions 
value = 'i am {} years old, and from {}'.format(23, 'siddhipur')
print(value)

# done by the given position by the programmer as a indexing 0 1 2 3
value = 'i am {1} years old, and from {0}'.format('siddhipur',23 )
print(value)

#by giving the value from the user
value = 'i am {age} years old, and from {add}'.format(add = 'siddhipur', age = 23 )
print(value)

# this is also valid where the keyword arguments should be at last
# indexing arguments should be at first

value = 'i am {age} years old, and from {0}'.format('siddhipur', age = 23 )
print(value)



name = str(input("Hello, \n   Enter your name"))

print("Welcome {name}, you are lucky for us!"\
      .format(name=name.capitalize()))
 
# we can not use default or an empty values in the {} when the others are defined
# position argument can not be given after a keyword argument in any python function


###################### f:string

#fstrings are also valid for triple coated string

name = 'ram'


print(f"Welcome {name}, you are lucky for us!")

m = f"""
I am {name}.
"""
print(m)