d = {
    'ram':23,
    'shyam':45
}
name = input("enter a name")
age = lambda name:d[name]
print(age(name))