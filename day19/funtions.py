from day19.decorators import change_to_upper
from day19.decorators import execution_time
import time

@change_to_upper
def print_message():
    return "hello world"

print(print_message())

@change_to_upper
def hellome():
    return "hello sajal"
print(hellome())

# @change_to_upper
# def newfun():
#     values = input("enter a name to make upper case")
#     return values
# print(newfun())

@execution_time
def timecal():
    for i in range (100000000):
        continue
    return "done"
print(timecal())