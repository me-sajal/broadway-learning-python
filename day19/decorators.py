# def decorator_name(fun):
#     def inne_fun():
# write logics
#         return fun()
#     pass
#     return inne_fun

import time
def change_to_upper(fun):
    def inne_fun():
        #print(" HELLO WORLD")
        return fun().upper()
    pass
    return inne_fun

def execution_time(fun):
    def inner_fun():
        start_time = time.time()
        a=fun()
        end_time = time.time()
        print("the time taken to execute is ", end_time - start_time)
        return a
    pass
    return inner_fun