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

    def __init__(self, name, meeting_days, meeting_times ):
        self.className = name
        self.classDays = meeting_days
        self.classTimes = meeting_times

    def createStudent( id, name ):
        '''
        Create a new student
        '''
        pass
    
