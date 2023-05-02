#true and false are the boolean data types
# all the relational logical identiy and membership operations 
# gives boolean data type
a = 5
b = 4
# relational operations
print("is equal to ",a == b)
print("a grater than b ",a > b)

# logical operation 
print (bool(a) and bool(b))
print(bool(a) and bool(b))

#identity operation
print(a is b)
print(a is not b)

# membership operation
print(2 in [1,3,4,5,62,2])
print(2 not in [1,3,4,5,62,2])

#boolean is sub class of integer where true+ true is 2 because true is 1 where false is 0

print(True+1)
print(False*70)
#concept of truthy and falsey
#any non empty list, string,  tupple, set, dictionary is a truthy value i.e 1
#in contrast all the empty list string tupple set dictionary is a falsy value including 0 for integer

print(bool(1))
print(bool(0))
print(bool([1,2,3]))
print(bool([]))
print(bool(None))
print(bool(True))
print(bool(False))
