def addition(*args):
    print(args)
    return sum(args)


print(addition(1, 2, 3, 4, 5))
addition(1, 2, 3, 4, 5)


def addition(**kwargs):
    print(kwargs)
    return sum(kwargs.values())


addition(a=1, d=99, b=2)
print(addition(a=1, d=99, b=2))


def summ(a, b, c, d, e=23, f = 33, *args, **kwargs):
    print(a, b, c, d)
    print(e,f)
    print(args)
    print(kwargs)




summ(1, 2, 3, 4, 5, 6, 7, 8, 9, p = 10, q = 11)