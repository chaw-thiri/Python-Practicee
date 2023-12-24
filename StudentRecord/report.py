from studentFile import StudentFileReader, StudentFileWriter, StudentRecord

fileName = "text.txt"
def main():
    # open the file and reading from the file
    file = StudentFileReader(fileName)
    file.open()
    records = file.fetchAll()
    file.close()

    records.sort(key=lambda x: x.classID)  # key = id of the object
    while True:
        choice =   input("Choose your options: (1) Print out data (2) Add new students(3) Exit the program :").strip()
        if choice == "1":
            printRecord(records)
        elif choice == "2":
            addStudents()
            file.open()
            records = file.fetchAll()
            file.close()
            printRecord(records)
        elif choice == "3":
            break
        else:
            print("Invalid input")





def printRecord(records):
    # class names are stored as integers in the text file so they are converted to the actual names here
    className = [None, "Freshman", "Sophomore", "Junior", "Senior"]
    # table heading
    print(f"List of students\n".center(50))  # add alignment
    print("%-5s %-25s %-10s %-4s " % ('ID', 'NAME', 'CLASS', 'GPA'))
    print("%-5s %-25s %-10s %-4s " % ('-' * 5, '-' * 25, '-' * 10, '-' * 4))
    # table body
    for record in records:
        print("%-5d %-25s %-10s %-4.2f" % \
              (record.id, \
               record.lastName + ', ' + record.firstName,  # Concatenate first and last name
               className[record.classID],  # Use className to get class name based on ID
               record.GPA))

    # table footer
    print("_" * 50)
    print("Number of students:", len(records))
def addStudents():
    studentId = int(input("Enter Student ID: "))
    firstName = input("Enter First Name : ")
    lastName = input("Enter Last Name : ")
    classID = int(input("Enter Class ID: "))
    GPA = float(input("Enter Student GPA: "))
    newStudent = StudentRecord(studentId, firstName,lastName, classID, GPA)
    file = StudentFileWriter(fileName)
    file.open()
    file.writeRecord(newStudent)
    file.close()
    print("Successfully added new student.")









if __name__ == "__main__":
    main()

