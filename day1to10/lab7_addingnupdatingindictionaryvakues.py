student = { 
    'name':'sajal',
    'age':22,
    'dept':'bca'
}
#if the id is not present in the dictionary then it adds the key and assign the value 4

student['id']=2173

print(student)

#if the key id is already prsent in the ditionary then it updayes the 
# value in the id, in this case 2170
student['id']=2170
student['name']='jane' #the name is updated from sajal to jane
further_info = {
    'email' : 'sajalrokka321@gmail.com',
    'address' : 'sanagaun'
}

##################update #####################

student.update(further_info)
print(student)

################## pop #######################

age = student.pop("age")
print(' using pop the age of student is :', age)
print(student)

################### Pop item #################

lastValueAtTheStudent = student.popitem()
print(' using pop item the \n the last value of student is :', lastValueAtTheStudent)
print(student)


#if we try poping the items not aviliable at the dictionary then 
# it throws the exception so we do give default values

#eg: student.pop('height')


print('height =', student.pop('height',5.9))#it provides the height 
#values as 5.9 because there is no height

# del student it deletes the student dictonary 

