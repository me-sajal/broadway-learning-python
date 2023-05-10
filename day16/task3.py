# from the given list of integer create a number whose digits are the elements of the list
a = [4, 2, 3, 1, 2, 5]
new_str = ""
for i in a:
    new_str += f"{i}"
print(new_str)
num = a[0]

for index, value in enumerate(a):
    try:
        num = num * 10 + a[index + 1]
    except IndexError:
        break
print(num)
