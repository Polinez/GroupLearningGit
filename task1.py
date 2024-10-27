from datetime import datetime
from idlelib.editor import keynames
from pkgutil import get_data


def menu():
        print("Wybierz opcję:")
        print("1. Importuj studentów z pliku")
        print("2. Dodaj nowego studenta")
        print("3. Zaznacz obecność studenta")
        print("4. Edytuj obecność studenta")
        print("5. Zapisz listę studentów do pliku")
        print("6. Wyjdź")
        wybor = input("Wybierz opcję: ")
        return wybor


def import_students(file_path):

    students_list = {}          #import studentow
    try:
        with open(file_path, 'r') as file:
            for line in file:
                students = line.strip().split(',')
                for student in students:
                    students_list[student] = True
            print("Lista studentów zaimportowana pomyślnie.")
    except FileNotFoundError:
        print("Plik nie istnieje. Zaczynamy z pustą listą.")
    return students_list

def add_student(students_list):
    with open(file_path, "a") as file:          #dodawanie studenta
        imie = input("Podaj imię i nazwisko studenta: ")
        students_list[imie] = True
        file.write(imie + ",")
    print("Student został dodany pomyślnie")


def export_students(file_path2, students_list):
    with open(file_path2, "a") as file:
        file.write(str(datetime.now()) + "\n")              #zapisywanie studentow do pliku
        for student, attendance in students_list.items():
            if attendance == True:
                file.write(f"{student:30} - obecny\n")
            else:
                file.write(f"{student:30} - nieobecny\n")
    print("Lista studentów zapisana pomyślnie.")


def check_students(students_list):
    for student in students_list:
        print(f"czy {student} jest obecny? ")  # sprawdzanie obecnosci
        obecnosc = input("T/N: ")
        if obecnosc.upper() == 'T':
            students_list[student] = True
        else:
            students_list[student] = False


def edit_students(students_list):
    imie = input("Podaj imię studenta: ") # zmiana obecnosci studenta
    obecnosc = input("Czy był obecny? T/N: ")
    if obecnosc.upper() == 'T':
        students_list.update({imie : True})
    else:
        students_list.update({imie : False})


  # Ścieżka do pliku TXT
file_path = 'students.txt' #lista nazwisk studentow
file_path2 = 'studentsAttendance.txt' #listy obecnosci z datami
students_list = {}


while True:
    wybor = menu()
    if wybor == '1':
        students_list = import_students(file_path)    # importowanie studenta z pliku
    elif wybor == '2':
        add_student(students_list)        #  dodawanie studenta do listy
    elif wybor == '3':
        check_students(students_list)       # sprawdzanie obecnosci studenta
    elif wybor == '4':
        edit_students(students_list)         # edytowanie obecnosci studenta
    elif wybor == '5':
        export_students(file_path2, students_list)      #zapisywanie obecnosci do pliku
    elif wybor == '6':
        exit()
    else:

        print("Błędny wybór")

