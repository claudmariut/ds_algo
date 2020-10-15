class College:
    """Represent a College."""
    def __init__(self, name):
        self.institution = name
        self.students = {}
        self.teachers = {}

    def getInstitution(self):
        """Return name of college"""
        print(self.institution)

    def setNewStudent(self, first, last, studentId, *classes):
        """Create new student."""
        username = first[0] + last
        self.students[username.lower()] = {
            "First Name": first,
            "Last Name": last,
            "Student ID": studentId,
            "Classes": classes}

    def getStudentInfo(self, username):
        """Return Student info."""
        for key, value in self.students[username].items():
           print(f"{key}: {value}")


class Person:
    """Represent a person."""
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def getName(self):
        """Return people name."""
        return f"{self.first} {self.last}."


class Student(Person):
    """Represent Student."""
    def __init__(self, first, last, studentId, *classes):
        super().__init__(first, last)

        self.id = studentId
        self.classes = [subject for subject in classes]

    def getStudentId(self):
        """Return student id."""
        return f"Student ID: {self.id}"

    def getClasses(self):
        """Return Student subjects."""
        print("Classes taken:")
        for subject in self.classes:
            print(f"-{subject}")


class Teachers(Person):
    """Represent a Teacher."""
    def __init__(self, first, last, teacherId, *classes):
        super().__init__(first, last)

        self.id = teacherId
        self.classes = [subject for subject in classes]

    def getTeacherId(self):
        """Return student id."""
        return f"Student ID: {self.id}"

    def getClasses(self):
        """Return Student subjects."""
        print("Classes teaching:")
        for subject in self.classes:
            print(f"-{subject}")






