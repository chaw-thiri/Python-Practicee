class StudentRecord:
    # store a student's data
    def __init__(self):
        self._id = 0
        self._firstName = None
        self._lastName = None
        self._classID = 0
        self._GPA = 0.0


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
        line = self._file.readline()  # read the first line
        if line == "": return None  # if the file is empty return None
        # fill the data as an object and return it
        student = StudentRecord()
        student._id = int(line)
        student._firstName = self._file.readline().rstrip()
        student._lastName = self._file.readline().rstrip()
        student._classID = int(self._file.readline())
        student._GPA = float(self._file.readline())
        return student

    # get all the records
    def fetchAll(self):
        records = []
        student = self.fetchRecord()
        while student != None:
            records.append(student)
            student = self.fetchRecord()
        return records
