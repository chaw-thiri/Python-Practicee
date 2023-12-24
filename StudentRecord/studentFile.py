class StudentRecord:
    # store a student's data
    def __init__(self, id=0, firstName=None, lastName=None, classID=0, gpa=0.0):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.classID = classID
        self.GPA = gpa


class StudentFileReader:
    # for reading the records of students

    def __init__(self, source):
        self._source = source  # _ define member variables just like mSource in C++
        self._file = None

    # Open the file in the read format
    def open(self):
        self._file = open(self._source, "r")

    # Close the file
    def close(self):
        self._file.close()
        self._file = None

    # Get individual record
    def fetchRecord(self):
        line = self._file.readline().strip()  # Read the first line and remove leading/trailing whitespace
        if not line:  # Check if the line is empty (end of file)
            return None

        # Fill the data as an object and return it
        student = StudentRecord()
        student.id = int(line)
        student.firstName = self._file.readline().rstrip()
        student.lastName = self._file.readline().rstrip()
        student.classID = int(self._file.readline())
        student.GPA = float(self._file.readline())
        return student

    # get all the records
    def fetchAll(self):
        records = []
        student = self.fetchRecord()
        while student is not None:
            records.append(student)
            student = self.fetchRecord()
        return records


class StudentFileWriter:
    # for write record in the file
    def __init__(self, source):
        self._source = source
        self._file = None

    def open(self):
        self._file = open(self._source, "a")

    def close(self):
        self._file.close()
        self._file = None

    def writeRecord(self, student):
        self._file.write(str(student.id) + "\n")
        self._file.write(student.firstName + "\n")
        self._file.write(student.lastName + "\n")
        self._file.write(str(student.classID) + "\n")
        self._file.write(str(student.GPA) + "\n")
