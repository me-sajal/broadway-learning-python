# Error handling
# In python there are  three types of errors
# 1. Syntactical error
# 2. Logical error
# 3. Exception / Runtime error

try:
    num = int(input("Enter a number"))
except ValueError:
    print("error occured")
except ZeroDivisionError:
    print("You stupid do not divide by 0 !")
else:
   print(f"the value is true so num is {num}")
finally:
    print("Thankyou! for running me")

# Common errors in the python
# valueerror, TypeError, KeyError, AttributeError, ZeroError, IndexError, StopIteration.

