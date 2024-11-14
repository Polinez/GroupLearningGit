from unittest.mock import patch, mock_open
import pytest
from task1 import edit_students,import_students,add_student,remove_student,export_students,check_students

class TestImportStudents:
    @patch("builtins.open", mock_open(read_data="Jan Kowalski,Anna Nowak"))
    def test_import_students_success(self):
        #given
        file_path = "students.txt"

        # when
        result = import_students(file_path)

        # then
        expected = {"Jan Kowalski": True, "Anna Nowak": True}
        assert result == expected

class TestAddStudent:
    pass
    #when
    #add_student()

class TestZaznaczObecnosc:
    pass
    #when
    #check_students()

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

class TestDeleteStudents:
    pass
    #when
    #remove_student()

class TestExportStudents:
    pass
    #when
    #export_students()