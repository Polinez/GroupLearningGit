import pytest
from task1 import edit_students,import_students,add_student,remove_student,export_students,check_students

class TestImportStudents:

    #when
    import_students()

class TestAddStudent:

    #when
    add_student()

class TestZaznaczObecnosc:

    #when
    check_students()

class TestObecnosci:
    def test_edit_students(self):
        # Given
        students_list = {}
        imie = "Jan Kowalski"
        obecnosc = "T"
        # When
        edit_students(students_list, imie, obecnosc)

        # Then
        assert students_list[imie] == True

    def test_edit_students_nieobecny(self):
        # Given
        students_list = {}
        imie = "Jan Kowalski"
        obecnosc = "N"
        # When
        edit_students(students_list, imie, obecnosc)

        # Then
        assert students_list[imie] == False

class TestDeleteStuden:

    #when
    remove_student()

class TestExportStudents:

    #when
    export_students()