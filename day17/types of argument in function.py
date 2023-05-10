# types of arguments
# Positional arguments
# Keyword arguments
# Arbitrary arguments


# Positional arguments

def addition(a, b, c):
    return a + b + c


# res - addition(1) a, b, c are positional arguments i.e. they are compulsory arguments


# Keyword arguments / default arguments
def additions(a, b=1):
    return a + b


res = additions(1)
print(res)
#
def additions(a, b=1):
    return a + b


res = additions(1,4)
print(res)

# Arbitrary arguments

