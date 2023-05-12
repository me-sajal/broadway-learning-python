def decorate_me(fun):
    def inne_fun():
        print(" name")
        return fun()
    return  inne_fun
# @decorate_me
def ordinary():
    print("hellp")

#ordinary()

result = decorate_me(ordinary)
result()