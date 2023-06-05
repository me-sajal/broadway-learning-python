# without recursion
fact = 1
for i in range(1,6):
    fact *= i
print(fact)
count = 0
num=1
# using recursion


def mes():
    global count
    count += 1
    global num
    num *= count
    if count == 5:
        return
    mes()


mes()
print(num)
