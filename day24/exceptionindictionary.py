student = {
    "id":"ST111",
    "name": "Sajal",
    "age": 21,
    "dept":"BCA"
}
try:
    input_from_user = int(input("enter 1 to display id of student, 2 for name, 3 for age and 4 for dept"))
    if (input_from_user == 1):
        print(student.get("id"))
    elif (input_from_user == 2):
        print(student.get("name"))
    elif (input_from_user == 3):
        print(student.get("age"))
    elif (input_from_user == 4):
        print(student.get("dept"))
    elif (input_from_user >4):
        raise ("the error out of index ")
except :
    print("the raised error occured")

#######################################################################################################################

key = input("Enter the info you want to access where id, name, age, dept are available")

try:
    print(f"the value of {key} is ", student[key])
except Exception as e:
    print("error occured :", e)