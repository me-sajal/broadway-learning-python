from create_student import create
from read_student import read
from update_student import update
from delete_student import delete


def inquiry():
    selection = input("Enter your choice C/R/U/D ")
    selection = selection.lower()
    def exit_msg():
        print("Thankyou see you again")
    if selection == "c":
       contd = create()
       inquiry() if contd else exit_msg()
    elif selection == "r":
        id = input("Enter the id to read")
        contd = read(id)
        inquiry() if contd else exit_msg()
    elif selection == "u":
        id = input("Enter the student id")
        to_change = input("Enter the info you wanted to change among name and age")
        if to_change in['name','age']:
            changed_data = input(f"Enter the new {to_change}")
            contd = update(id, to_change, changed_data)
            inquiry() if contd else exit_msg()
        else:
            print("Invalid input")
            choice = input("continue or not? (y/n)")
            return True if choice.lower() == "y" else False
    elif selection == "d":
        id = input("Enter the student id")
        contd = delete(id)
        inquiry() if contd else exit_msg()
    else:
        print("Invalid Choice")


if __name__ == "__main__":
    inquiry()
