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

#test that student class exists
def test_student_class():
    new_student = Student("Last", "First", "345443")
    assert new_student 

#test that roster of assignments exists
#test that student's assignment accepts grade
def test_assignment_list():
    new_student = Student("first", "last", "1")
    new_student.updateGrade("first", 67)
    assert new_student.assignmentGrades["first"] == 67

#test that student gradebook can remove assignment
def test_remove_assignment():
    new_student = Student("Test", "Case", 1)
    new_student.updateGrade("first", 67)
    assert len(new_student.assignmentGrades) == 1
    new_student.removeAssignment("first")
    assert not new_student.assignmentGrades

#test that classroom roster is object
def test_classroom_roster_object():
    calculus_class = createClassroom()
    assert not calculus_class.classRoster

#test that teachers should be able to add and remove students from class
def test_add_remove_student():
    classroom = createClassroom()
    classroom.addStudent(createStudent(1))
    assert classroom.classRoster[1].lastName == "Fluffykins"
    classroom.addStudent(createStudent(2))
    assert len(classroom.classRoster) == 2
    classroom.removeStudent(2)
    assert len(classroom.classRoster) == 1

#test that teacher can add assignments to class
def test_add_assignment_to_classroom():
    classroom = createClassroom()
    classroom.addAssignment("first assignment", 100)
    assert len(classroom.assignmentList) == 1
    assert classroom.assignmentList["first assignment"] == 100

#test that teacher can remove assignments from class
def test_remove_assignment():
    classroom = createClassroom()
    classroom.addAssignment("first", 100)
    classroom.addAssignment("second", 100)
    classroom.removeAssignment("first")
    assert len(classroom.assignmentList) == 1
    assert classroom.assignmentList["second"] == 100

#test that teacher can assign grade to student
def test_grade_single_assignment():
    classroom = createClassroom()
    classroom.addStudent(createStudent(1))
    classroom.addAssignment("first", 100)
    classroom.gradeAssignment(1, "first", 80)
    assert classroom.classRoster[1].getAssignmentGrade("first") == 80

#test that students can total grades
def test_grade_summation_control_process_iteratoratron():
    #create student
    omg_mazing_student = Student("Fluffykins", "Rolly Polly", 1)

    #Add Assignments
    omg_mazing_student.updateGrade("first assignmnet", 90)
    omg_mazing_student.updateGrade("second assignment", 80)
    omg_mazing_student.updateGrade("Theird assignment", 75)
    
    #TEST TEST TEST
    assert omg_mazing_student.getGradeTotal() == 81.6

#test that student can have no grade for assignment
    # classroom = createClassroom()
    # classroom.addStudent(createStudent(1))
    # classroom.addAssignment("first", 100)
    # classroom.addAssignment("second", 50)
    # classroom.gradeAssignment(1, "first", 90)

#test that teacher can get accurate class gpa

#Test gradebook returns proper class avg

#test gradebook return proper class max

#test gradebook returns propler class min


def createClassroom():
    return Classroom("Calculus", ["Mon", "Wed", "Fri"], ["12:30", "14:45"])

def createStudent(id):
    return Student("Fluffykins", "Rolly Polly", id)
