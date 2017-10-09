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
        print("Class Assignments: ", assigned_assignments)
        studentTotal = 0
        assignmentTotal = 0
        print(self.assignmentGrades)
        for assignment in self.assignmentGrades:
                print(self.assignmentGrades[assignment])

        if assignmentTotal == 0:
            return 100
        else:
            return round((studentTotal/assignmentTotal), 2)

    def getID(self):
        return self.studentID