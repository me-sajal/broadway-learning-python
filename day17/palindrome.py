# check whether a number is palindrome or not?

num = int(input("enter a number to check whether a number is palindrome or not?"))
# k = 0
# a = []
# while num !=0:
#     a[k] = num/10
#     num =num /10
#     k += 1
# i = 1
# j = -1
# for index, value in enumerate(a):
#     if a [i] == a[j]:
#         if i <= index and j <= -index:
#             i += 1
#             j += 1
#         else:
#             print("the number is palindrome")
#     else:
#         print("the number is not palindrome")
rev = 0
b = num
while num != 0:
    reminder = num% 10
    rev = rev * 10 + reminder
    num = num //10
print("it is palindrome") if rev == b else print("not palindrome")