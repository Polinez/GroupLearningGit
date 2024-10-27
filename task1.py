from datetime import datetime
from logging import raiseExceptions


def menu():
        print("Wybierz opcję:")
        print("1. Importuj studentów z pliku")
        print("2. Dodaj nowego studenta")
        print("3. Zaznacz obecność studenta")
        print("4. Edytuj obecność studenta")
        print("5. Usuń studenta z bazy")
        print("6. Zapisz listę studentów do pliku")
        print("7. Wyjdź")
        wybor = input("Wybierz opcję: ")
        return wybor


def import_students(file_path):
    students_list = {}          #import studentow
    try:
        with open(file_path, 'r') as file:
            for line in file:
                students = line.strip().split(',')
                for student in students:
                    if student != "":
                        students_list[student] = True
            print("Lista studentów zaimportowana pomyślnie.")
    except FileNotFoundError:
        print("Plik nie istnieje. Zaczynamy z pustą listą.")
    return students_list

def add_student(students_list):
    with open(file_lista_studentow, "a") as file:          #dodawanie studenta
        imie = input("Podaj imię i nazwisko studenta do dodania: ")
        students_list[imie] = True
        file.write(imie + ",")
    print("Student został dodany pomyślnie")

def remove_student(file_path, students_list):              #usuwanie studenta
    imie = input("Podaj imię i nazwisko studenta do usunięcia: ")
    if imie in students_list:
        students_list.pop(imie)
    else:
        print("Takiego studenta nie ma w bazie")
    with open(file_path, "w") as file:
        for student in students_list.keys():
            file.write(student + ",")
    print("Student został usunięty")

def export_students(file_path2, students_list):
    with open(file_path2, "a") as file:
        file.write(str(datetime.now()) + "\n")          #zapisywanie obecnosci studentow do pliku
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
        elif obecnosc.upper() == 'N':
            students_list[student] = False
        else:
            raise Exception("Błędny wybór, edytuj później.")
            students_list[student] = False


def edit_students(students_list):
    imie = input("Podaj imię studenta: ") # zmiana obecnosci studenta
    obecnosc = input("Czy był obecny? T/N: ")
    if obecnosc.upper() == 'T':
        students_list.update({imie : True})
    else:
        students_list.update({imie : False})


  # Ścieżka do pliku TXT
file_lista_studentow = 'students.txt' #lista nazwisk studentow
file_obecnosc = 'studentsAttendance.txt' #listy obecnosci z datami
students_list = {}


while True:
    wybor = menu()
    if wybor == '1':
        students_list = import_students(file_lista_studentow)    # importowanie studenta z pliku
    elif wybor == '2':
        add_student(students_list)        #  dodawanie studenta do listy
    elif wybor == '3':
        check_students(students_list)       # sprawdzanie obecnosci studenta
    elif wybor == '4':
        edit_students(students_list)         # edytowanie obecnosci studenta
    elif wybor == '5':
        remove_student(file_lista_studentow, students_list)       #usuwanie studenta
    elif wybor == '6':
        export_students(file_obecnosc, students_list)      #zapisywanie obecnosci do pliku
    elif wybor == '7':
        exit()
    else:
        print("Błędny wybór")

