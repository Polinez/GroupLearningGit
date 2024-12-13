from datetime import datetime
from unittest.mock import patch, mock_open
import pytest
from task1 import edit_students, import_students, add_student, remove_student, export_students, check_students


class TestImportStudents:
    @patch("builtins.open", mock_open(read_data="Jan Kowalski,Anna Nowak"))
    def test_import_students_success(self):
        #given
        file_path = "../students.txt"
        students_list = {}

        # when
        result = import_students(file_path,students_list)

        # then
        expected = {"Jan Kowalski": False, "Anna Nowak": False}
        assert result == expected

    def test_import_students_file_not_found(self):
        # given
        file_path = "doesNotExist.txt"
        students_list = {}

        # when
        with pytest.raises(FileNotFoundError):
            import_students(file_path,students_list)

    @patch("builtins.open", mock_open(read_data=""))
    def test_import_students_empty_file(self):
        # given
        file_path = "empty.txt"
        students_list = {}

        # when
        result=import_students(file_path,students_list)

        # then
        expected = {}
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
        mock_file().write.assert_any_call("Jan Kowalski - present\n")
        mock_file().write.assert_any_call("Anna Nowak - absent\n")

    @patch("builtins.open", new_callable=mock_open,
           read_data=f"{datetime.now().day} {datetime.now().month} {datetime.now().year}\nJan Kowalski - present\n")
    def test_export_students_attendance_already_saved_today(self,mock_file):
        # given
        students_list = {"Jan Kowalski": True}

        # when
        with pytest.raises(Exception):
            export_students(mock_file, students_list)

class TestAddStudents:
    def test_add_students_success(self):
        # given
        imie = "Jan Kowalski"
        students_list={}

        # when
        result = add_student(students_list,imie)

        # then
        expected = {"Jan Kowalski": False}
        assert result == expected

    def test_add_students_empty_name(self):
        # given
        imie = ""
        students_list = {}

        # when
        with pytest.raises(ValueError):
            add_student(students_list,imie)

    def test_add_students_single_name_value(self):
        # given
        imie = "Jan"
        students_list = {}

        # when
        with pytest.raises(ValueError):
            add_student(students_list,imie)

class TestRemoveStudents:
    def test_remove_student(self):
        #Given
        imie="Sebastian"
        students_lists={"Sebastian":True,"Jan Kowalski":False}

        #When
        remove_student(students_lists,imie)
        #Then
        assert students_lists == {"Jan Kowalski": False}

    def test_remove_student_not_found(self):
        #Given
        imie="Sebastian"
        students_lists={"Jan Kowalski":False}

        #When
        with pytest.raises(ValueError):
            remove_student(students_lists,imie)

class TestCheckStudents:
    def test_check_students_present(self):
        # given
        students = {"Jan Kowalski": False, "Sebastian Wandzel": False}

        # when
        with patch("builtins.input", side_effect=["Y", "Y"]):
            check_students(students)

        # then
        assert students["Jan Kowalski"] == True
        assert students["Sebastian Wandzel"] == True

    def test_check_students_absent(self):
        # given
        students = {"Jan Kowalski": False, "Sebastian Wandzel": False}

        # when
        with patch("builtins.input", side_effect=["N", "N"]):
            check_students(students)

        # then
        assert students["Jan Kowalski"] == False
        assert students["Sebastian Wandzel"] == False

    def test_check_students_invalid_input(self):
        # given
        students = {"Jan Kowalski": False, "Sebastian Wandzel": False}

        # when
        with patch("builtins.input", side_effect=["X", "T"]):
            with pytest.raises(Exception):
                check_students(students)

class TestEditStudents:
    def test_edit_students(self):
        # Given
        students_list = {}
        imie = "Jan Kowalski"
        obecnosc = "Y"
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

    def test_edit_students_invalid_input(self):
        # given
        students_list = {}
        imie = "Jan Kowalski"
        obecnosc = "X"

        # when
        with pytest.raises(Exception):
            edit_students(students_list, imie, obecnosc)



