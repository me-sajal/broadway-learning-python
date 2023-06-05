# normal function
def addition(a, b):
    return a + b


# lamda function and used only in single line statements
# lamda paxad ko laai normally paramenters vanxa

add = lambda a, b: a + b
print(add(2, 4))

# clear = lambda : os.system('cls')
# clear()


a = [(2, 3), (2, 1), (3, 6), (9, 0)]
a.sort(key=lambda data: data[1])
print(a)

# map function

a = [1, 2, 3, 4, 5]


def get_mul_of_two(data):
    return data * 2


res = map(get_mul_of_two, a)
print(list(res))

print(list(map(lambda data : 2 * data, a)))

# list comprehension
a = [1, 2, 3, 4, 5]
changed_a = [i * 2 for i in a]
print(changed_a)


#filter function
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#this is normal comprassion evens = [i for i in a if i % 2 == 0]

resultes = filter(lambda data: data % 2 == 0,a)
print("the result is ", list(resultes))


# redce function
from functools import reduce
a = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x+y, a)
print(result)


