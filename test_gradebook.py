import pytest
from student import Student
from classroom import Classroom

#Test that teacher can create a new classroom
def test_class_exists():
    new_class = Classroom("Class Name", ['Mon', 'Wed', 'Fri'], ["11:30", "14:30"] )
    assert new_class

#test that the classroom object has Classroom name
def test_classroom_name():
    new_class = Classroom("Class Name", ['Mon', 'Wed', 'Fri'], ["11:30", "14:30"] )
    assert new_class.className == "Class Name"

#test that classroom contains meeting days
def test_classDays():
    new_class = Classroom("Class Name", ['Mon', 'Wed', 'Fri'], ["11:30", "14:30"] )
    assert new_class.classDays[0] == 'Mon'
    assert new_class.classDays[1] == 'Wed'
    assert new_class.classDays[2] == 'Fri'
    assert len(new_class.classDays) == 3

#test that classroom contains meeting times
def test_classTimes():
    new_class = Classroom("Class Name", ['Mon', 'Wed', 'Fri'], ["11:30", "14:30"] )
    assert new_class.classTimes[0] == '11:30'
    assert new_class.classTimes[1] == '14:30'
    assert len(new_class.classTimes) == 2

#test that student roster class exists
def test_student_class():
    new_student = Student("Last", "First", "I", "345443")
    assert new_student

 

#test that roster of assignments exists

#test that assignment accepts grade

#test that teachers should be able to add and remove students from class

#test that teacher can add and remove assignments from class

#test that assignments can have no grade

#test that teacher can get accurate class gpa