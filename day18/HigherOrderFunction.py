# normal function
def addition(a, b):
    return a + b


# lamda function and used only in single line statements


add = lambda a, b: a + b
print(add(2, 4))

# clear = lambda : os.system('cls')
# clear()


a = [(2, 3), (2, 1), (3, 6), (9, 0)]
a.sort(key=lambda data: data[1])
print(a)
