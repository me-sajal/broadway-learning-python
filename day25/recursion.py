count = 0
def mes():
    global count
    count += 1
    print("Hello world")

    if count==10:
        return
    mes()
mes()