# enumerate() built in function

vowels = ["a", "e", "i", "o", "u"]

print(list(enumerate(vowels)))

enum_vowels = enumerate(vowels)

for index, values in enum_vowels:
    print(index, " at ->", values)


for i in range (len(vowels)):
    print("index:", i, " value:", vowels[i])

#enumerate() fun takes start argument, where we can gice the start count
for count, values in enumerate(vowels, start=1):
    print(count, " at ->", values)
