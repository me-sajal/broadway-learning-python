"""
Write a program to prompt for a score between 0.0 and 1.0. If the score is between 0.0 and 1.0, print a grade using the following table:
A for >=0.9
B for >=0.8
C for >=0.7
D for >=0.6
F for <0.6

If the user enters a value out of range, print a suitable error message."""

value = float(input ("Enter a number in between a 0.0 to 1.0 "))

if 0.9 <= value <= 1:
    print("A")
elif 0.8 <= value <= 1:
    print("B")
elif 0.7 <= value <= 1:
    print("C")
elif 0.6 <= value <= 1:
    print("D")
elif 0.6 > value <= 1:
    print("F")
else:
    print("Input wrong please enter a number in range between 0.0 to 1.o")