from datetime import datetime
from unittest.mock import patch, mock_open
import pytest
from task1 import edit_students, import_students, add_student, remove_student, export_students, check_students, \
    students_list


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

class TestExportStudents:
    @patch("builtins.open", new_callable=mock_open)
    def test_export_students(self,mock_file):
        # given
        file_path = "studentsAttendance.txt"
        students_list={"Jan Kowalski": True, "Anna Nowak": False}
        current_date = f"{str(datetime.now().day)} {str(datetime.now().month)} {str(datetime.now().year)}"

        # when
        export_students(file_path,students_list)

        # then
        mock_file().write.assert_any_call(f"{current_date}\n")
        mock_file().write.assert_any_call("Jan Kowalski - obecny\n")
        mock_file().write.assert_any_call("Anna Nowak - nieobecny\n")

class TestONStudents:
    def test_add_students_success(self):
        # given
        file_path = "students.txt"
        imie = "Jan Kowalski"
        students_list={}

        # when
        result = add_student(students_list,imie)

        # then
        expected = {"Jan Kowalski": True}
        assert result == expected

    def test_removestudent(self):
        #Given
        imie="Sebastian"
        students_lists={"Sebastian":True,"Jan Kowalski":False}

        #When
        remove_student(students_lists,imie)
        #Then
        assert students_lists == {"Jan Kowalski": False}

class TestONApsents:
    def test_check_students_present(self):
        # given
        students = {"Jan Kowalski": False, "Sebastian Wandzel": False}

        # when
        with patch("builtins.input", side_effect=["T", "T"]):
            check_students(students)

        # then
        assert students["Jan Kowalski"] == True
        assert students["Sebastian Wandzel"] == True

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


