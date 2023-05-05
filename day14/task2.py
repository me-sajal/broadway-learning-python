n = int(input("enter number"))
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz", n, "is the number")
elif n % 5 == 0:
    print("Buzz")
elif n % 3 == 0:
    print("Fizz")
else:
    print("the number is neither divided by 3 or 5")
