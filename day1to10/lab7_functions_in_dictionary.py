#all([])
#any([])
#len()
#sorted()
#type()
#str()

s = {
    'name' : 'sajal',
    'email' : 'sajalrokka321@gmail.com',
    'address' : 'sanagaun'
}

##################### all()

#all() built in fun . this fun takes iterable (sequence) as a 
#parameer and returns true value if the elemet of the sequece are truthy.
# in the case of dictionary it checks the key of the dictionary

print(all(s))

#the python accepts the "" value as id only in a dictionary
a = {
    "":1
}
print(all(a)) # this returns false value because of "" false key

print(all([])) #this is an exceptio in the all () Function
#because it returns True



###################################   any()
# any built in fun also takes iterable(Sequence) as a parameter,
#but it returns if at least one of the elements is Truthy

b = {0:'hello', 1:"world"}
print(any(b)) #this returns the true because the one key is truthy,
#but if all the key are falsy then it returns false

b = {0:'hello', '':"world"}
print(any(b)) #this returns the true because the one key is truthy,
#but if all the key are falsy then it returns false


########## sorted

# It sorts te key of the items on the alphabet order and provides list
print(sorted(s))
datas = sorted(s)
print(datas)

#######str

print(str(s)) # gives str


############type
print(type(s))