student = { 
    'name':'sajal',
    'age':22,
    'dept':'bca'
}
print(student['name'])
print(student['age'])
print(student['dept'])
#print(student['id']) #error aaucha

print(student.get('name'))
print(student.get('id')) #error aaudaina internally error ko thau ma none hunxa
print(student.get('id',1))

print(student.get('name','jane'))

