# else statement in for
nums = [1, 2, 3, 4]
for i in nums:
    print(i)
else:
    print("the for loop completed!!!")

# else statement in while
counter = 0
while counter <5:
    print(counter)
    counter += 1
else:
    print("the while loop completed!!!")
counter = 0
while counter <5:
    print(counter)
    counter += 1
    if counter == 4:
        break

else:
    print("the while loop completed!!!")
