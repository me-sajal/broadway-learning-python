# can be used in string, list, tuples, dictionaries
# are an object which can be iterated through
# are those object which can be converted to iterator object

a = [1, 2, 3, 4, 5]
iter_a = iter(a)
itb = iter(a)

print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
#print(next(iter_a)) gives error


while True:
    try:
        print(next(itb))
    except StopIteration:
        break

