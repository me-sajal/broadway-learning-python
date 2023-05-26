import json
filename = "students.json"

def read(student_id):
    with open(filename, "r") as fp:
        data = fp.read()
        data = json.loads(data)
        student =list(filter (lambda a: a['id']==student_id, data ))
        if student:
            print(student[0])
        else:
            print("Invalid student id")
    choice = input("continue or not? (y/n)")
    return True if choice.lower() == "y" else False