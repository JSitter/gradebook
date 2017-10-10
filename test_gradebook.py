import pytest
import random
from student import Student
from classroom import Classroom

#Test that teacher can create a new classroom
def test_classExists():
    '''
        Test if Classroom can be instantiated.
    '''
    new_class = Classroom("Class Name", ['Mon', 'Wed', 'Fri'], ["11:30", "14:30"] )
    assert new_class

#test that the classroom object has Classroom name
def test_classroomName():
    '''
        Test if Classroom can be named.
    '''
    new_class = Classroom("Class Name", ['Mon', 'Wed', 'Fri'], ["11:30", "14:30"] )
    assert new_class.className == "Class Name"

#test that classroom contains meeting days
def test_classDays():
    '''
    test that classroom contains meeting days
    '''
    new_class = Classroom("Class Name", ['Mon', 'Wed', 'Fri'], ["11:30", "14:30"] )
    assert new_class.classDays[0] == 'Mon'
    assert new_class.classDays[1] == 'Wed'
    assert new_class.classDays[2] == 'Fri'
    assert len(new_class.classDays) == 3

def test_classTimes():
    '''
    test that classroom contains meeting times
    '''
    new_class = Classroom("Class Name", ['Mon', 'Wed', 'Fri'], ["11:30", "14:30"] )
    assert new_class.classTimes[0] == '11:30'
    assert new_class.classTimes[1] == '14:30'
    assert len(new_class.classTimes) == 2

def test_studentClass():
    '''
    test that student class exists
    '''
    new_student = Student("Last", "First", "345443")
    assert new_student 


def test_assignmentList():
    '''
    test that roster of assignments exists
    test that student's assignment accepts grade
    '''
    new_student = Student("first", "last", "1")
    new_student.updateGrade("first", 67)
    assert new_student.assignmentGrades["first"] == 67


def test_removeAssignment():
    '''
    test that student gradebook can remove assignment
    '''
    new_student = Student("Test", "Case", 1)
    new_student.updateGrade("first", 67)
    assert len(new_student.assignmentGrades) == 1
    new_student.removeAssignment("first")
    assert not new_student.assignmentGrades


def test_classroomRosterObject():
    '''
    test that classroom roster is object
    '''
    calculus_class = createClassroom()
    assert not calculus_class.classRoster


def testAddRemoveStudent():
    '''
    test that teachers should be able to add and remove students from class
    '''
    classroom = createClassroom()
    classroom.addStudent(createStudent(1))
    assert classroom.classRoster[1].lastName == "Fluffykins"
    classroom.addStudent(createStudent(2))
    assert len(classroom.classRoster) == 2
    classroom.removeStudent(2)
    assert len(classroom.classRoster) == 1


def testAddAssignmentToClassroom():
    '''
    test that teacher can add assignments to class
    '''
    classroom = createClassroom()
    classroom.addAssignment("first assignment", 100)
    assert len(classroom.assignmentList) == 1
    assert classroom.assignmentList["first assignment"] == 100

def testRemoveAssignment():
    '''
    test that teacher can remove assignments from class
    '''
    classroom = createClassroom()
    classroom.addAssignment("first", 100)
    classroom.addAssignment("second", 100)
    classroom.removeAssignment("first")
    assert len(classroom.assignmentList) == 1
    assert classroom.assignmentList["second"] == 100


def testGradeSingleAssignment():
    '''
    test that teacher can assign grade to student
    '''
    classroom = createClassroom()
    classroom.addStudent(createStudent(1))
    classroom.addAssignment("first", 100)
    classroom.gradeAssignment(1, "first", 80)
    assert classroom.classRoster[1].getAssignmentGrade("first") == 80

def test_studentGPA():
    '''
        Test for correct gpa calculation
        test that students can total grades
    '''
    classRoom = createClassroom()
    student = createStudent(1);
    assignmentDict = createStudentAssignmentList()
    for assignment in assignmentDict:
        student.updateGrade( assignment, assignmentDict[assignment] )
    assert student.getGPA(createAssignmentList()) == round((76+56+57+34+41+13)/6, 1)

def test_GPAafterAssignmentRemoval():
    '''
        Test that teacher can remove assignment from student
    '''
    student = createStudent(1)
    student.updateGrade("first", 100)
    student.updateGrade("Second", 100)
    student.removeAssignment("first")
    assert student.getGPA({"first" : 100, "Second":100}) == 100

def test_studentGPAafterClassAssignmentRemoval():
    '''
        Test that teacher can remove assignment after student recieves grade
    '''
    student = createStudent(1)
    assignments = createAssignmentList()
    student.assignmentGrades = assignments
    assignments.pop("first")

    assert student.getGPA(assignments) == 100

def test_setAttendance():
    '''
    Test that teacher can set student attendance
    '''
    student = createStudent(1)
    student.setAttendance(2017, 3, 23, "Present")
    assert student.attendance["20170323"] == "Present"

def test_getAttendance():
    '''
    Test that teacher can get attendance
    '''
    student = createStudent(1)
    student.setAttendance(2017, 3, 23, "Present")
    assert student.getAttendance(2017, 3, 23) == "Present"

#Test gradebook can remove assignment
def test_gradebookRemoveAssignment():
    classroom = createClassroom()
    classroom.assignmentList = createAssignmentList()
    classroom.removeAssignment("first")
    assert len(classroom.assignmentList) == 5

#Test gradebook returns proper class avg
def test_gradebookClassAvg():
    classroom = createClassroom()
    classroom.assignmentList = createAssignmentList()
    classroom.addStudent(createStudent(1))
    classroom.addStudent(createStudent(2))
    classroom.gradeAssignment(1, "first", 80)
    classroom.gradeAssignment(1, "Second", 70)
    classroom.gradeAssignment(1, "Third", 60)
    classroom.gradeAssignment(2, "first", 50)
    classroom.gradeAssignment(2, "Second", 40)
    classroom.gradeAssignment(2, "Third", 30)

    assert classroom.classGPA() == 55

#test gradebook return proper class max

#test gradebook returns propler class min


def createClassroom():
    return Classroom("Calculus", ["Mon", "Wed", "Fri"], ["12:30", "14:45"])

def createStudent(id):
    return Student("Fluffykins", "Rolly Polly", id)

def createStudentAssignmentList():
    return { "first" : 76, "Second" : 56 , "Third": 57, "Fourth" : 34, "Fifth" : 41, "Sixth" : 13}

def createAssignmentList():
    return { "first" : 100, "Second" : 100 , "Third": 100, "Fourth" : 100, "Fifth" : 100, "Sixth" : 100}

def avgAssignments(assignments):
    accumulator = 0
    for key in assignments:
        accumulator += assignments[key]
    return round(accumulator/len(assignments), 1)