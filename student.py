class Student:
    '''
        Student class keeps track of attendance, assignments
        Should contain

        Student has student ID, assignments, grade, attendence
    '''
    def __init__(self, lastName, firstName, studentID):
        self.lastName = lastName
        self.firstName = firstName
        self.studentID = studentID
        self.attendance = {}
        self.assignmentGrades = {}

    def updateGrade(self, assignment, grade):
        '''
        Create or Update Student Grade
        '''
        self.assignmentGrades[assignment] = grade
    
    def removeAssignment(self, assignment):
        del self.assignmentGrades[assignment]
    
    def getAssignmentGrade(self, assignment):
        return self.assignmentGrades[assignment]

    def getGPA(self, assigned_assignments):
        print(assigned_assignments)
        gradeTotal = 0
        for assignment in assigned_assignments:
            print(assigned_assignments[assignment])

        return gradeTotal

    def getID(self):
        return self.studentID