class Student:
    '''
        Student class keeps track of attendance, assignments
        Should contain student ID, assignments, grade, attendence
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
       
        for assignment in self.assignmentGrades:
                studentTotal += self.assignmentGrades[assignment]
                assignmentTotal += assigned_assignments[assignment]

        if assignmentTotal == 0:
            return 100
        else:
            return round((studentTotal/assignmentTotal) * 100 , 1)

    def getID(self):
        return self.studentID

    def setAttendance(year, month, day, attendance):
        pass
    
    def getAttendance(year, month, day):
        pass