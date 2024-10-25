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

    students_list = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                student = line.strip().split(',')
                students_list.append([student[0], student[1] == 'True'])
            print("Lista studentów zaimportowana pomyślnie.")
    except FileNotFoundError:
        print("Plik nie istnieje. Zaczynamy z pustą listą.")
    return students_list



def add_student(students_list):
    imie = input("Podaj imię studenta: ")


def export_students(file_path, students_list):

    with open(file_path, 'w') as file:
        for student in students_list:
            file.write(f"{student[0]},{student[1]}\n")
    print("Lista studentów zapisana pomyślnie.")



def check_students(students_list):
    for student in students_list:
        print(f"czy {student} jest obecny? ")  # sprawdzanie obecnosci
        obecnosc = input("T/N: ")
        if obecnosc == 'T':
            student['obecnosc'] = True
        else:
            student['obecnosc'] = False


def edit_students(students_list):
    pass


  # Ścieżka do pliku TXT
file_path = 'students.txt'

students_list = []


while True:
    wybor = menu()
    if wybor == '1':
        students_list = import_students(file_path)     # importowanie studenta z pliku
    elif wybor == '2':
        add_student(students_list)        #  dodawanie studenta do listy
    elif wybor == '3':
        check_students(students_list)       # sprawdzanie obecnosci studenta
    elif wybor == '4':
        edit_students(students_list)         # edytowanie obecnosci studenta
    elif wybor == '5':
        export_students(file_path, students_list)
    elif wybor == '6':
        exit()
    else:

        print("Błędny wybór")

