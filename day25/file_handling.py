# File modesin python
# r = read
# w = write
# a = append
# x = exclusive write

# write mode
# fp = open("file.txt", "w")
# fp.write("hello from file")
# fp.close()

# file read
# try:
#     fp = open("file.txt", "r")
#     data = fp.read()
#     print(data)
#
# except:
#     pass
#
# finally:
#     fp.close()
#
# file append
# fp = open("file.txt", "a")
# fp.write("\nPython is awsome!")

# fp = open("C:\\Users\\sajal\\OneDrive\\Pictures\\BackgroundImages\\addfoodbg.jpg", "rb")
# data = fp.read()
# print(data)
# fp.close()

# try:
#     fp = open("anc.png", "ab")
#     fp.write(data)
# except:
#     pass
# finally:
#     fp.close()

# x mode
# fp = open("file.txt","x")
# fp.write("file doesn't exist")
# fp.close()

#context manager
with open("file.txt", "r") as fp:
    data = fp.read()
    print(data)

with open("file.txt", "w") as fp:
    data = "hello from file"
    fp.write(data)

with open("file.txt", "a") as fp:
    data = "\n python is awasome"
    fp.write(data)

with open("file.txt", "a+") as fp:
    data = " my words are "
    fp.write(data)
    msg = fp.read()
    print(msg)

# r+ ma suru ma read garey ra matra write garnee
# w+ ma suru ma write garey ra matra read garnee

