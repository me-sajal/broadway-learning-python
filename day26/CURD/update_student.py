import json
filename = "students.json"


def update(student_id, to_change, changed_data):
    with open(filename, "r+") as fp:
        data = fp.read()
        data = json.loads(data)
        student = list(filter(lambda a: a['id'] == student_id, data))
        if student:
            a = data.index(student[0])
            data[a][to_change] = changed_data
            fp.seek(0)
            fp.write(json.dumps(data, indent=2))
            print("Data Updated")
        else:
            print(" Invalid student id")
    choice = input("continue or not? (y/n)")
    return True if choice.lower() == "y" else False
# json.dump(fp, indent=2)
