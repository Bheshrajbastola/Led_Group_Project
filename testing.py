import pytest
from tution_managenment_all_file import*

def main_body():

 ab= show_database_result("admin","admin")
 assert ab=="Pass"


def test_register_student_body():
 pq = show_database_result("ram")
 assert pq == "Pass"

def test_find_student_body():
 rs = show_database_result1("Male", "Ram")
 assert rs == "Pass"

def test_add_course_body():
 dt = show_database_result("C", "100")
 assert dt == "Pass"

def test_Phone():
 vu = show_database_result("9875263528")
 assert vu == "Pass"