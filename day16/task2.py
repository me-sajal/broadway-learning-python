#using for loop
count = 0
for i in range(0, 200):
    if count < 50 and i % 2 == 0:
        print(i)
        count += 1

# using while loop
count = 0
val = 0
while count < 50:
    if val % 2 == 0:
        print(val)
        count += 1
    val += 1