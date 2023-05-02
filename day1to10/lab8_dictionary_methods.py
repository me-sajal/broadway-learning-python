a = dict()

print(a.fromkeys([1,2,3,4],1))

student = {
    'name':'sajal',
    'age':22,
    'dept':'BCA'
}
s = student.copy()
s.fromkeys([1,2,3,4],'hello world')
print(s.fromkeys([1,2,3,4]))

student.setdefault("name",'harry')
student.setdefault("id",2173)


print(student.items())
print(student.keys()) 



print(student.clear()) #this cleares the student


