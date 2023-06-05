# closures can be higher order function in the python
# criteria for closures are:
# 1. Closure function must define another nested function
# 2. The parameter passed inside the closure function must be used inside the nested function
# 3. the clouser must return the nested function


def decorateME(func):
    def innerME(a,b,c):

        return func(a,b,c)

    return innerME

def additon (a, b, c):
    return a + b + c


a = int(input("enter a 1st number"))
b = int(input("enter a 1st number"))
c = int(input("enter a 1st number"))

res = decorateME(additon)
print(res(a,b,c))
