# range function in python
# rage returns an iterator which can be iterated through
first_ten_natural_numbers = range(1, 11)    # 1 2 3 4 5 6 7 8 9 10
for num in first_ten_natural_numbers:
    print(num)

for num in range(5):   # 0 1 2 3 4
    print(num)

for num in range(0, 10, 2):     # 0 2 4 6 8
    print(num)
for num in range(10, 0, -1):    # 10 9 8 7 6 5 4 3 2 1
    print(num)

# if we do not want the loop value inside the loop then we can use underscore _

for _ in range(5):
    print("hello world")    # this prints "hello world" 5 times

