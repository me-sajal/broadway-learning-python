def change_to_upper(fun):
    def inne_fun():
        #print(" HELLO WORLD")
        return fun().upper()
    return  inne_fun


@change_to_upper
def print_message():
    return "hello world"

print(print_message())

@change_to_upper
def hellome():
    return "hello sajal"
print(hellome())
