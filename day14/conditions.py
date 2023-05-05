# in if .... elif .... else ladder, if one of the condition is satisfied then the next
#blockes are nir executed. In contrast, in normal if ... if ...if ...else blocks, every conditions
# are checked and every satisfied blocks are executed.
# all the logical and relational operations can be used in conditon check.
# we can directly use truthy and falsy values without logical or relational values
a = int(input("enter a number"))
if a == 1:
    print("the value pf a is 1")
elif a == 2:
    print("the value pf a is 2")
else:
    print("the value is out of range i.e:", a)

#ternary if ... else
print("it is non empty") if a else print("it is empty")

# nested if
message = "hello world"
if message:
    if message == "hello":
        print(f"hello {message}")
    else:
        print(message)
else:
    print("empty string")