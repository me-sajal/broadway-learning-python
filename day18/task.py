student = [
    {
        'name': 'sajal',
        'age': 21
    },
    {
        'name': 'sudha',
        'age': 19
    },
    {
        'name': 'prajwol',
        'age': 18
    },
    {
        'name': 'srija',
        'age': 23
    }
]
resultes = filter(lambda data: data["age"] < 20, student)
print("the result is ", list(resultes))

