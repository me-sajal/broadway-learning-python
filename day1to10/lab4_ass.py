a = [(6, 1),(4, 12, 5), (11, 12),(6, 7, 8)]
print(a)
def get_item_at_last(a):
    return a[-1]

a.sort(key=get_item_at_last)
print(a)