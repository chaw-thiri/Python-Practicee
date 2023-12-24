from studentFile import StudentFileReader

fileName = "text.txt"


def main():
    # open the file and reading from the file
    file = StudentFileReader(fileName)
    file.open()
    records = file.fetchAll()
    file.close()

    records.sort(key=lambda x: x._classID)  # key = id of the object
    printRecord(records)


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
              (record._id, \
               record._lastName + ', ' + record._firstName,  # Concatenate first and last name
               className[record._classID],  # Use className to get class name based on ID
               record._GPA))

    # table footer
    print("_" * 50)
    print("Number of students:", len(records))


main()

