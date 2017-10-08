class Classroom:
    '''
    Classroom should be able to store student objects in a dictionary
    Classroom needs to keep track of class name roster of all assignments, and grades
    for every assignment.

    User should be able to add and remove students from roster.
    User should be able to add and remove assignments and calculate class's average grade.

    classroom should be able to assign student id.
    '''
    #Name of classroom
    className = ""

    #Meeting Days
    classDays = ""

    #Meeting Time
    classTimes = ""

    def __init__(self, name, meeting_days, meeting_times):
        self.className = name
        self.classDays = meeting_days
        self.classTimes = meeting_times
        self.classRoster = {}
        self.assignmentList = {}

    def addStudent(self, Student):
        '''
        Create a new student
        '''
        self.classRoster[Student.getID()] = Student
    
    def removeStudent(self, id):
        self.classRoster.pop(id)
    
    def addAssignment(self, name, totalPoints):
        self.assignmentList[name] = totalPoints
    
    def removeAssignment(self, name):
        self.assignmentList.pop(name)
    
    def gradeAssignment(self, studentID, assignmentName, grade):
        self.classRoster[studentID].updateGrade(assignmentName, grade)