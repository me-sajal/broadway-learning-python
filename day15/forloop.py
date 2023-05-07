vowels = ['a', 'e', 'i', 'o', 'u']
for vowel in vowels:
    print(vowel)

nums = [1, 2, 4, 5]
new_nums =[]
for num in nums:
    value = num * 2
    new_nums.append(value)
    print(value)
print(new_nums)

# looping in tuple
a = (1, 2, 3, 4, 5)
for num in a :
    print(a)

# looping in string
message = "hello world"
for i in message:
    print(i)

# looping in set
aset = {"a", "e", "i", "o", "u"}
for word in aset:
    print(word)

#looping in dictionary

student = {
    "name":"sajal",
    "age":21,
    "dept":"BCA"
}

for key in student:
    print(key)
for values in student.values():
    print(values)

for items in student.items():
    print(items)
# unpacking of tuples using through for loop
for key,value in student.items():
    print(key,"     :    ",value)

