import os
from datetime import datetime


def menu():
    print("Choose an option:")
    print("1. Import students from file")
    print("2. Add a new student")
    print("3. Mark student's attendance")
    print("4. Edit student's attendance")
    print("5. Remove a student from the database")
    print("6. Save students' attendance to a file")
    print("7. Exit")
    wybor = input("Choose an option: ")
    return wybor


def import_students(file_students, students_list):
    try:
        with open(file_students, "r") as file:
            students = file.read().split(",")
            for student in students:
                if student != "":
                    students_list[student] = False
            print("Students list successfully imported.")
            return students_list
    except FileNotFoundError:
        raise FileNotFoundError("The file does not exist. Starting with an empty list.")


def add_student(students_list, name):
    if not name or not isinstance(name, str) or len(name.split()) < 2:
        raise ValueError("Invalid name. Please provide a full name (first and last).")
    else:
        students_list[name] = False
        print("Student successfully added.")
        return students_list


def remove_student(students_list, name):
    if name in students_list:
        students_list.pop(name)
        print("Student successfully removed.")
    else:
        raise ValueError("No such student found in the database.")
    return students_list


def export_students(file_attendance, students_list):
    with open(file_attendance, "r") as file:
        if (
            f"{datetime.now().day} {datetime.now().month} {datetime.now().year}"
            in file.read()
        ):
            raise Exception("The students' attendance has already been saved today.")

    with open(
        file_attendance, "a"
    ) as file:  # "a" mode means appending to the end of the file
        file.write(
            f"{datetime.now().day} {datetime.now().month} {datetime.now().year}\n"
        )  # Writing the current date
        for student, attendance in students_list.items():
            if attendance:
                file.write(f"{student} - present\n")
            else:
                file.write(f"{student} - absent\n")
    print("Students' attendance successfully saved.")


def check_students(students_list):
    for student in students_list:
        print(f"Is {student} present? ")
        presence = input("T/N: ")
        if presence.upper() == "Y":
            students_list[student] = True
        elif presence.upper() == "N":
            students_list[student] = False
        else:
            raise Exception("Invalid input, please edit later.")


def edit_students(students_list: dict, name: str, presence: str):
    if presence.upper() == "Y":
        students_list.update({name: True})
    elif presence.upper() == "N":
        students_list.update({name: False})
    else:
        raise Exception("Invalid input, please edit later.")


# TODO: Go to sleep after this ;)
def main():
    # Path to files
    file_students = "src" + os.sep + "students.txt"  # List of students' names
    file_attendance = (
        "src"
        + os.sep
        + "listOfStudents.txt"  # File where students' attendance will be saved
    )
    students_list = {}

    # Import students from file when the program starts
    students_list = import_students(file_students, students_list)

    while True:
        wybor = menu()  # Display the menu
        if wybor == "1":
            students_list = import_students(
                file_students, students_list
            )  # Import students from file
        elif wybor == "2":
            name = input("Enter the student's full name to add: ")
            students_list = add_student(
                students_list, name
            )  # Add new student to the list
        elif wybor == "3":
            check_students(students_list)  # Mark students attendance
        elif wybor == "4":
            name = input(
                "Enter the student's name: "
            )  # Edit attendance for a specific student
            presence = input("Was the student present? T/N: ")
            edit_students(students_list, name, presence)  # Edit attendance for student
        elif wybor == "5":
            name = input("Enter the student's full name to remove: ")
            students_list = remove_student(
                students_list, name
            )  # Remove a student from list
        elif wybor == "6":
            export_students(
                file_attendance, students_list
            )  # Save students attendance to file
        elif wybor == "7":
            export_students(
                file_attendance, students_list
            )  # Save attendance one last time before exit
            exit()  # Exit the program
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
