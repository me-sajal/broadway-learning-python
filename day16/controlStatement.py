# break statement breaks the loop without completing the loop
a = [1, 3, 5, 2, 7]
for num in a:
    if num % 2 == 0:
        break
    print(num)

counter = 2
while True:
    print(counter)
    counter += 1
    if counter == 5:
        break

# continue
word = "PYTHON"
for c in word:
    if c.lower() in ['a', 'e', 'i', 'o', 'u']:
        continue
    print(c)
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)


# pass
# placeholder for future code