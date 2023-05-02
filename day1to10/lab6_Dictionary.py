#dictionaries are the key value pairs built inside the curly braces 
#separates by commas
#we can also use a dict() function to create a dictionary
a = { } # this is an empty dictionary
student = { 
        'name':'sajal',
        'age':20,
        "dept":"BCA"
}
print(student)
student1 = dict(name='sajal', age=20) # using built in function
print(student1)

print(student1['age'])

print(student.get('sa'))

# accessing dictionary values 
# dictionary values can be accessed using big [] brackets or using () methods

print(student["name"]) #getting using brackets
print(student.get("name")) #gettinh vlues using get () method

#print(student["id"]) #getting vlues using get () method

print(student.get("id")) #getting vlues using get () method




