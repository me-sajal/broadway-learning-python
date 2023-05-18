try:
    a = int(input("Enter a 1st number"))
    b = int(input("Enter a 2nd number"))

except (TypeError, ValueError):
    print("error on the type or value")
else:
    print("the sum is ", a+b)
finally:
    print("thanks for using me to add numbers")

