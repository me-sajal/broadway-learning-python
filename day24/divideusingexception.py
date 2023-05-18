try:
    a = float(input("Enter a 1st number"))
    b = float(input("Enter a 2nd number"))
    print("the Diffrences is ", round((a / b),2))
except (ZeroDivisionError, ValueError):
    print("error on the Zero Division or Value")
finally:
    print("thanks for using me to divide numbers")