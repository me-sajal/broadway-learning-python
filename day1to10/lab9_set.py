###### set type
# set is an unordered data type in python
# set is mutable but its values must be immutable
# we create set using curly braces for eg: {0,2,3,4,'hello'}
# creatin empty set
# a = set()
# {} => this is an empty dictionary and not an empty set

s = {1, 2, 3} #non empty set
a = set() #empty set
#a = { [1, 2, 3] } # this is invalid because it has multable type list

# adding and removing set items

s.add(4) # this adds  4 in set at arbitrary positiom
s.update([4,5,6,7]) # this adds  5, 6, 7 in the set at random sequence
print(s)